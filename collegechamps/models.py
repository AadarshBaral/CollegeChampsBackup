from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from collegechamps import db, login_manager, app
from datetime import datetime,timezone
from slugify import slugify

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    # posts = db.relationship('Post', backref='author', lazy=True)

# the token for emailreset 1800 means the token will expire in 30mins
    # def get_reset_token(self,expires_sec=1800):
    #     s = Serializer(app.config['SECRET_KEY'],expires_sec)
    #     return s.dumps({'user_id': self.id}).decode('utf-8')

    # @staticmethod
    # def verify_reset_token(token):
    #     s = Serializer(app.config['SECRET_KEY'])
    #     try:
    #         user_id = s.loads(token)['user_id']
    #     except:
    #         return None
    #     return User.query.get(user_id)

    # def __repr__(self):
    #     return f"User('{self.username}', '{self.email}')"


# for comments.. implementation in the future
class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), nullable = False)
    subtitle = db.Column(db.Text, nullable = False)
    content = db.Column(db.Text, nullable=False)
    img = db.Column(db.Text, nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    to_redirect = db.Column(db.String(20),nullable = True)
    image_file = db.Column(db.String(20), nullable=True)
    mock_title = db.Column(db.String(20), nullable = True)
    mock_content=db.Column(db.String(200), nullable = True)
    price  = db.Column(db.String(),nullable  = True)
    to_redirect = db.Column(db.String(20),nullable = True)
    featured = db.Column(db.String(20), nullable = True)
    subject_title  = db.Column(db.String(20),nullable = True)
    others1 = db.Column(db.String(20), nullable = True)
    others2 = db.Column(db.String(20), nullable = True)
    time_limit1 = db.Column(db.Integer())
    time_limit2 = db.Column(db.Integer())
    url_slug = db.Column(db.String(255))

    def __init__(self, *args, **kwargs):
        if not 'url_slug' in kwargs:
            kwargs['url_slug'] = slugify(kwargs.get('title', ''))
        super().__init__(*args, **kwargs)

class Set(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    pass