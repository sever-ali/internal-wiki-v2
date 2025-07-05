from flask import Flask
from .extensions import db, login_manager
from .routes import main, auth
from .models import User

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wiki.db'
    app.config['SECRET_KEY'] = 'super-secret-key'

    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    app.register_blueprint(main)
    app.register_blueprint(auth)

    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app

    