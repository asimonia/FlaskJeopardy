from flask import request, redirect, render_template, url_for
from app import db
from ..models import Questions, Game, Tile
from . import main
from .forms import GameForm


@main.route('/', methods=['GET', 'POST'])
def index():
	form = GameForm(request.form)
	if not form.validate_on_submit() or request.method == 'GET':
		return render_template('questions/index.html', form=form)

	# initialize the game
	# initialize the players, scores
	players = form.players.data
	show_number = form.show_number.data
	
	player_names = []
	player_names.append(form.playerone_name.data)
	player_names.append(form.playertwo_name.data)
	player_names.append(form.playerthree_name.data)
	
	player_scores = []
	for player in range(players):
		player_scores.append(0)

	# initialize the gameboard
	categories = Questions.objects(show_number=show_number, current_round='Jeopardy!').distinct(field='category')
	values = Questions.objects(show_number=show_number, current_round='Jeopardy!').distinct(field='value')
	values.sort()
	questions = Questions.objects(show_number=show_number, current_round='Jeopardy!')

	initialize_game = Game(is_playing=True, number_players=players, player_names=player_names,
								current_player=0, player_scores=player_scores, show_number=show_number,
								current_round="Jeopardy!", categories=categories, values=values)

	initialize_game.save()
		
	for question in questions.all():
		tile = Tile(category=question.category, question=question.question, answer=question.answer, 
					value=question.value, exists=True)
		initialize_game.tiles.append(tile)
		initialize_game.save()

	return render_template('questions/game_board.html', game=initialize_game)

@main.route('/game/', methods=['GET'])
def game_board():
	return render_template('questions/game_board.html')