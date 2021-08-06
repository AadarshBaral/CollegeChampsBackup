# main/routes.py
from flask import render_template, request, Blueprint, redirect
from flask_login import login_required
from collegechamps.models import User,Post


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():

    side_posts = Post.query.filter_by(others2 = 'sidebar')
    posts = Post.query.filter_by(slug = 'index')
    return render_template('index.html',posts = posts ,side_posts = side_posts)

# @main.route('/sidebar_elem/<int:side_id>')
# def sidebar_elem(side_id):
#     side_id = side.

@main.route("/ioe")
def ioe():
    return render_template('ioe.html')


@main.route("/blog_notes")
def blog_notes():
    return render_template('blog_notes.html')

@main.route('/CollegeChamps/privacy-policy/<parameter>')
def privacy_policy(parameter):
    side_posts = Post.query.filter_by(others2 = 'sidebar')
    return render_template('privacy_policy.html',side_posts= side_posts, parameters =parameter)


# @main.route("/mcqsection")
# @login_required
# def mcqsection():
#     return render_template('mcqsection.html')



# @main.route("/about")
# def about():
#     return render_template('about.html', title='About')

