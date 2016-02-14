from . import db

class Questions(db.Document): 
    category = db.StringField(verbose_name="Category", required=True)
    air_date = db.StringField(verbose_name="Air_Date", required=True)
    question = db.StringField(verbose_name="Question", required=True)
    value = db.StringField(verbose_name="Value", required=True)
    answer = db.StringField(verbose_name="Answer", required=True)
    current_round = db.StringField(verbose_name="Current_Round", required=True)
    show_number = db.StringField(verbose_name="Show_Number", required=True)