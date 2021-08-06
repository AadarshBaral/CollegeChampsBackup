from flask import render_template, Blueprint
# import json
from flask.app import Flask
import flask_wtf
from flask_wtf.form import FlaskForm
from wtforms import RadioField


# import os

quest = Blueprint('quest', __name__)


# with open('json/mcq.json', 'r') as c:
#     json_data = json.load(c)["questions"]


# class Radio(FlaskForm):
#     options = RadioField(choices=[('Option1',json_data["opt1"]),('Option2',json_data["opt2"]),('Option3',json_data["opt3"])])


# @quest.route('/mcqs', methods = ['GET','POST'])
# def mcq_page():
#     form = Radio()
#     return render_template("mcq_page.html",set = json_data, form = form)