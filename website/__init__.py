from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    #app.config["MAIL_SERVER"] = "smtp-mail.outlook.com"
    #app.config["MAIL_PORT"] = 587
    #app.config["MAIL_USERNAME"] = 'BUssin.supp0rt@outlook.com'
    #app.config["MAIL_PASSWORD"] = 'chaewonfan69'
    #app.config["MAIL_USE_TLS"] = True
    #app.config["MAIL_USE_SSL"] = False
    #app.config['SECRET_KEY'] = 'key'
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #app.config.from_object('config')
    app.config.from_pyfile('config.py')
    mail.init_app(app)
    db.init_app(app)
    app.app_context().push()
    
    
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Review
    
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'views.home'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all()
        print('Created database')
        