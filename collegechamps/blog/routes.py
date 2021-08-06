from io import TextIOWrapper
import os
from slugify import slugify
from re import sub
import secrets
from flask import render_template, url_for, flash, redirect, request, Blueprint, session, request
from flask_login import login_user, current_user, logout_user, login_required
from flask_wtf.recaptcha.widgets import RecaptchaWidget
from collegechamps import db, app
from collegechamps.blog.forms import PostForm
from collegechamps.models import Set, Post
from collegechamps.users.forms import RegistrationForm
from werkzeug.utils import secure_filename
from PIL import Image
import json
from datetime import datetime, timezone

db_username = os.environ.get('DB_USERNAME')
db_pw = os.environ.get('DB_PASSWORD')

with open('mcq.json', 'r') as c:
    params = json.load(c)["params"]

blogs = Blueprint('blogs', __name__)

@blogs.route('/blog_page')
def blog_page():
    side_posts = Post.query.filter_by(others2 = 'sidebar')

    posts = Post.query.filter_by(
        slug='blog', others1='article').order_by(Post.date_posted.desc())
    # notes = Post.query.filter_by(slug = 'note')
    notes = Post.query.filter_by(slug='blog', others1='note')

    return render_template('blog_page.html', background="sc-6", heading='CollegeChamps', sub_header='Blog Page', posts=posts, notes=notes, side_posts = side_posts)


@blogs.route('/post/<int:post_id>/')
def post(post_id):
    feats = Post.query.filter_by(featured='featured')
    post = Post.query.get_or_404(post_id)
    # to_slugify = Post.query.filter_by(title = title).first()
    # slug_title = to_slugify.replace(" ","-")
    return render_template('post.html', title=post.title, post=post, feats=feats)


# @blogs.route('/<url_slug>', methods = ['GET'])
# def spost(url_slug):
#     feats = Post.query.filter_by(featured='featured')
#     post = Post.query.get_or_404(url_slug)
#     # to_slugify = Post.query.filter_by(title = title).first()
#     # slug_title = to_slugify.replace(" ","-")
#     return render_template('post.html', title=post.title, post=post, feats=feats)
# @blogs.route('/<post_id>/<slug>')

# def postp(post_id, slug):

#     """ find the post and then show it """
#     p = Post.query.get(post_id)
#     return render_template("post.html", post=p)


@blogs.route('/post_page')
def post_page():
    return render_template('postpage.html')


@blogs.route('/ioe_entrance/ioe-notes')
def notes():
    notes = Post.query.filter_by(others1='note')
    return render_template('post.html', notes=notes)


@blogs.route('/ioe_entrance/ioe-notes/<int:note_id>')
def note_ids(note_id):
    feats = Post.query.filter_by(featured='featured')
    notes = Post.query.get_or_404(note_id)
    return render_template('notes.html', note=notes, feats=feats)


@blogs.route('/featured')
def featured_posts():
    feats = Post.query.filter_by(featured='featured')
    return render_template('featured.html', feats=feats)

# @blogs.route('/featured')
# def post():
#     feats = Post.query.filter_by(featured = 'featured')
#     return render_template('post.html',feats = feats)


@blogs.route('/featured/<int:feat_id>')
def featured_ids(feat_id):
    feat = Post.query.get_or_404(feat_id)
    feats = Post.query.filter_by(featured='featured')
    return render_template('featured.html', feat=feat, feats=feats)




@blogs.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    form = RegistrationForm()
    if ('user' in session and session['user'] == db_username):
        posts = Post.query.all()
        see_posts = Post.query.filter_by(slug  = 'set_page', subject_title = 'see')
        articles = Post.query.filter_by(slug  = 'blog', others1 = 'article')
        notes = Post.query.filter_by(slug  = 'blog', others1 = 'note')
        return render_template('dashboard.html', posts=posts,see_posts = see_posts,articles = articles,notes=notes)

      

    if request.method == "POST":
        username = form.username.data
        userpass = form.password.data
        if username == db_username and userpass == db_pw:
            session['user'] = username
            posts = Post.query.all()
            see_posts = Post.query.filter_by(slug  = 'index')
            flash('Welcome to the dashboard', 'succes')
            return render_template('dashboard.html', posts=posts,see_posts = see_posts)
        else:
            flash('Retype The password or the username ', 'error')
    return render_template('dashboard_sign_in.html', form=form)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        app.root_path, 'static/profile_pics', picture_fn)

    basewidth = 250
    # output_size = (200, 200)
    i = Image.open(form_picture)
    wpercent = (basewidth/float(i.size[0]))
    hsize = int((float(i.size[1])*float(wpercent)))
    i = i.resize((basewidth,hsize), Image.ANTIALIAS)
    # i.thumbnail(output_size)
    i.save(picture_path)
   

    return picture_fn

# blog Posts


@blogs.route("/postNew/<string:parameter>", methods=['GET', 'POST'])
def postNew(parameter):

    if ('user' in session and session['user'] == db_username):
        posts = Post.query.all()
        form = PostForm()
        if parameter == 'index':
            form.slug.data = 'index'
            # flash_kw = 'index'
            form.content.data = "_"
        if parameter == 'set_page':
            form.slug.data = 'set_page'
            # flash_kw = 'Sets'

        if form.validate_on_submit():
            title = form.title.data
            slug = form.slug.data
            content = form.content.data
            subtitle = form.subtitle.data
            price = form.price.data
            subject_title = form.subject_title.data
            pic = request.files['pic']
            if pic:
                pic = save_picture(request.files['pic'])
            else:
                pic = 'hello.png'
            to_redirect = form.to_redirect.data
            post = Post(title=title, slug=slug, subtitle=subtitle, img=pic,
                        to_redirect=to_redirect, content=content, price=price, subject_title=subject_title)
            db.session.add(post)
            db.session.commit()
            # {flash_kw}
            flash(f'Your post has been created for  page!', 'succes')
            # if parameter =='continue_editing':
            #     return redirect('blogs.update_post',post_id =post.id)
               
            return redirect('blogs.dashboard')
        return render_template('create_post.html', title='You are posting on the index page',
                               form=form, posts =posts ,parameter=parameter)

    return "please login to the dashboard first. Dont try to enter without logging in!"


@blogs.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    posts = Post.query.all()
    if ('user' in session and session['user'] == db_username):
        form = PostForm()
        if form.validate_on_submit():
            post.title = form.title.data
            post.content = form.content.data
            post.slug = form.slug.data
            post.subtitle = form.subtitle.data
            post.to_redirect = form.to_redirect.data
            post.price = form.price.data
            pic = request.files['pic']
            if pic:

                post.img = save_picture(request.files['pic'])
            else:
                pass

            db.session.commit()
            flash('Your post has been updated!', 'succes')
            return redirect(url_for('blogs.dashboard'))
        elif request.method == 'GET':
            form.title.data = post.title
            form.content.data = post.content
            form.slug.data = post.slug
            form.subtitle.data = post.subtitle
            form.to_redirect.data = post.to_redirect
            form.price.data = post.price

        return render_template('create_post.html', title='Update Post',posts=posts,
                               form=form, legend='Update Post')
    return "please login to the dashboard first. Dont try to enter without logging in!"


@blogs.route("/post/<int:post_id>/delete", methods=['GET', 'POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if ('user' in session and session['user'] == db_username):
     
        db.session.delete(post)
        db.session.commit()
        flash('Your post has been deleted!', 'info')
        return redirect(url_for('blogs.dashboard'))

    return "please login to the dashboard first. Dont try to enter without logging in!"

# set posts
# @blogs.route('/set_post/new', methods=['GET', 'POST'])
# def set_post():
#     if ('user' in session and session['user'] == params["username"]):
#         form = PostForm()
#         if form.validate_on_submit():
#             set_card = Set(title=form.title.data, content=form.content.data, price=form.price.data,
#                            mock_title=form.mock_title.data, mock_content=form.mock_content.data)
#             db.session.add(set_card)
#             db.session.commit()
#             flash('Your set has been created!', 'success')
#             return redirect(url_for('blogs.dashboard'))
#         return render_template('create_post.html', title='New Set',
#                                form=form)

#     return "please login to the dashboard first. Dont try to enter without logging in!"


@blogs.route('/set_page')
def set_page():
    sets = Post.query.filter_by(slug='set_page',subject_title = 'see')
    return render_template('sets_page.html', sets=sets, header = '+2 Entrance Preparation',title = '+2 Entrance Preparation')


@blogs.route('/individual_set/<int:set_id>/')
def individual_set(set_id):
    individual_page = Post.query.get_or_404(set_id)
    # limit = Post.query.all(others=25).first()
    return render_template('forms_page.html', individual_page=individual_page,times_limit = 25)

# @blogs.route('/add/<string:parameters>', methods = ['GET', 'POST'])   
# def add(parameters):
#     form = RegistrationForm()
#     if ('user' in session and session['user'] == params["username"]):
#         form = PostForm()
#         if form.validate_on_submit():
#             pic = save_picture(request.files['pic'])
#             post = Post(post_title=form.title.data,post_slug = form.post_slug.data, post_subtitle =form.subtitle.data,mock_title=form.mock_title.data,mock_content=form.mock_content.data, post_content=form.content.data, img=pic)
#             db.session.add(post)
#             db.session.commit()
#             flash('Your post has been created!', 'success')
#             return redirect('blogs.dashboard')
#         return render_template('create_post.html', form = form ,parameter = parameters)
#     return render_template('dashboard_sign_in.html',form = form)


@blogs.route('/test')
def test():
    return render_template('test.html')



