from flask import Blueprint

questions = Blueprint('questions', __name__, template_folder='templates')

from . import views