from . import db

class Questions(db.Document): 
    category = db.StringField(verbose_name="Category", required=True)
    air_date = db.StringField(verbose_name="Air_Date", required=True)
    question = db.StringField(verbose_name="Question", required=True)
    value = db.IntField(verbose_name="Value", required=True)
    answer = db.StringField(verbose_name="Answer", required=True)
    show_number = db.StringField(verbose_name="Show_Number", required=True)
    current_round = db.StringField(verbose_name="Current_Round", required=True)

class Tile(db.EmbeddedDocument):
	category = db.StringField(verbose_name="Category", required=True)
	question = db.StringField(verbose_name="Question", required=True)
	answer = db.StringField(verbose_name="Answer", required=True)
	value = db.IntField(verbose_name="Value", required=True)
	exists = db.BooleanField(verbose_name="Exists", required=True)

class Game(db.Document):
	is_playing = db.BooleanField(verbose_name="Is_Playing", required=True)
	number_players = db.IntField(verbose_name="Number_Players", required=True)
	player_names = db.ListField(verbose_name="Player_Names", required=True)
	current_player = db.IntField(verbose_name="Current_Player", required=True)
	player_scores = db.ListField(verbose_name="Player_Scores", required=True)
	
	show_number = db.StringField(verbose_name="Current_Show_Number", required=True)
	current_round = db.StringField(verbose_name="Current_Round", required=True)
	categories = db.ListField(verbose_name="Current_Categories", required=True)
	tiles = db.ListField(db.EmbeddedDocumentField('Tile'))




