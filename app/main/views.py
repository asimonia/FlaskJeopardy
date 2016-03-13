from flask import request, redirect, render_template, url_for
from app import db
from ..models import Questionbank, Player, Tile, Category, Game
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
	categories = Questionbank.objects(show_number=show_number, current_round='Jeopardy!').distinct(field='category')
	values = Questionbank.objects(show_number=show_number, current_round='Jeopardy!').distinct(field='value')
	values.sort()
	questions = Questionbank.objects(show_number=show_number, current_round='Jeopardy!')
	init_game = Game(state='playing', show_number=show_number, current_round='Jeopardy!')
	init_game.save()

	# add players and initialize score
	for name, score in zip(player_names, player_scores):
		player_save = Player(name=name, score=score)
		init_game.players.append(player_save)
		init_game.save()

	# add category and value
	for category, value in zip(categories, values):
		category_save = Category(name=category, value=value)
		init_game.categories.append(category_save)
		init_game.save()

	for question in questions.all():
		tile = Tile(round_called=question.current_round, question=question.question, answer=question.answer, 
					value=question.value, state='playing')
		init_game.categories.tiles.append(tile)
		init_game.save()

	return render_template('questions/game_board.html', game=init_game)


@main.route('/game/', methods=['GET'])
def game_board():
	return render_template('questions/game_board.html')


@main.route('/game/<category>/<int:value>/', methods=['GET'])
def show_question(category, value):
	game = Game.objects.all()
	return render_template('questions/show_question.html', category=category, value=value, game=game)