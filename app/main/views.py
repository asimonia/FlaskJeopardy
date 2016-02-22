from flask import request, redirect, render_template, url_for
from .. import db
from ..models import Questions, Game, Tile
from . import main
from .forms import GameForm


@main.route('/', methods=['GET', 'POST'])
def index():
	form = GameForm()
	if form.validate_on_submit():
		# initialize the game
		# initialize the players
		players = form.players.data
		playernames = []
		playernames.append(form.playerone_name.data)
		playernames.append(form.playertwo_name.data)
		playernames.append(form.playerthree_name.data)
		players_dict = {}
		players_scores = {}
		for player in range(1, players):
			players_dict[player] = playernames[player - 1]
			players_scores[player] = 0

		# initialize the gameboard
		categories = Questions.objects(show_number=form.show_number.data, current_round='Jeopardy!').distinct(field='category')
		questions = Questions.objects(show_number=form.show_number.data, current_round='Jeopardy!')

		tile = Tile()

		for question in questions:
			tile.category = question.category
			tile.question = question.question
			tile.answer = question.answer
			tile.value = question.value
			tile.exists = True
			tile.save()
			
			
		initialize_game = Game(is_playing=True, number_players=players, player_names=players_dict,
								current_player=1, player_scores=players_scores, show_number=form.show_number.data,
								current_round="Jeopardy!", categories=categories, tiles="").save()
		
		return redirect(url_for('game_board'))
	return render_template('questions/index.html', form=form)


@main.route('/game/', methods=['GET', 'POST'])
def game_board():
	return render_template('questions/game_board.html')

