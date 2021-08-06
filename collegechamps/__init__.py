from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_scss import Scss

from flask_migrate import Migrate
app = Flask(__name__)


Scss(app)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME='gk7125690@gmail.com',
    MAIL_PASSWORD='135?1?3?5'
)


app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

Migrate(app, db)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

login_manager.login_view = 'users.login'

# for information alert
login_manager.login_message_category = 'info'


mail = Mail(app)

from collegechamps.users.routes import users
from collegechamps.errors.handlers import errors
from collegechamps.subjects.subjects import subjects
from collegechamps.main.routes import main
from collegechamps.mcqs.routes import quest
from collegechamps.blog.routes import blogs

app.register_blueprint(users)
app.register_blueprint(main)
app.register_blueprint(errors)
app.register_blueprint(subjects)
app.register_blueprint(quest)
app.register_blueprint(blogs)

from collegechamps.models import User, Post ,Set

admin = Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Set, db.session))

