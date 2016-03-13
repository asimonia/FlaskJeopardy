from . import db

class Questionbank(db.Document): 
	category = db.StringField(verbose_name="Category", required=True)
	air_date = db.StringField(verbose_name="Air_Date", required=True)
	question = db.StringField(verbose_name="Question", required=True)
	value = db.IntField(verbose_name="Value", required=True)
	answer = db.StringField(verbose_name="Answer", required=True)
	show_number = db.StringField(verbose_name="Show_Number", required=True)
	current_round = db.StringField(verbose_name="Current_Round", required=True)

class Player(db.EmbeddedDocument):
	name = db.StringField(verbose_name="Player", required=True)
	score = db.IntField(verbose_name="Score", required=True)

class Tile(db.EmbeddedDocument):
	round_called = db.StringField(verbose_name="Round_Called", required=True)
	question = db.StringField(verbose_name="Question", required=True)
	answer = db.StringField(verbose_name="Answer", required=True)
	value = db.IntField(verbose_name="Value", required=True)
	state = db.StringField(verbose_name="State", required=True)
	player_ticked = db.StringField(verbose_name="Player_Ticked", required=True)
	player_won = db.StringField(verbose_name="Player_Won", required=True)

class Category(db.EmbeddedDocument):
	name = db.StringField(verbose_name="Name", required=True)
	value = db.IntField(verbose_name="Value", required=True)
	tiles = db.ListField(db.EmbeddedDocumentField('Tile'))

class Game(db.Document):
	players = db.ListField(db.EmbeddedDocumentField('Player'))
	state = db.StringField(verbose_name="State", required=True)
	show_number = db.StringField(verbose_name="Current_Show_Number", required=True)
	current_round = db.StringField(verbose_name="Current_Round", required=True)
	categories = db.ListField(db.EmbeddedDocumentField('Category'))

"""
usage:
    game = get_or_start_game()

    for i in num_tiles: # this is pre-defined
        for category in game.categories:
            if tile state is unvisited:
                write html with value
            if tile state is active:
                html answer
            else: #spent
                html empty tile

tile = categories.tiles[i]
"""




