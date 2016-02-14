from flask import request, redirect, render_template, url_for
from .. import db
from ..models import Questions
from . import questions
from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form


class ListView(MethodView):

    def get(self):
        questions = Questions.objects.all()
        return render_template('questions/list.html', questions=questions)


# Register the urls
questions.add_url_rule('/', view_func=ListView.as_view('list'))