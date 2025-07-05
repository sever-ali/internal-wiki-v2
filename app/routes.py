from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from .extensions import db, login_manager
from .models import User, WikiArticle

main = Blueprint('main', __name__)

@main.route('/')
def index():
    articles = WikiArticle.query.all()
    return render_template('index.html', articles=articles)

@main.route('/article/<int:article_id>')
def view_article(article_id):
    article = WikiArticle.query.get_or_404(article_id)
    return render_template('view_article.html', article=article)

@main.route('/create', methods=['GET', 'POST'])
@login_required
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_article = WikiArticle(title=title, content=content)
        db.session.add(new_article)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('create_article.html')

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_article(id):
    article = WikiArticle.query.get_or_404(id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.content = request.form['content']
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('edit.html', article=article)

@main.route('/delete/<int:id>', methods=['POST'])
def delete_article(id):
    article = WikiArticle.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    flash('Article deleted!', 'success')
    return redirect(url_for('main.index'))

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('auth.register'))

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user, remember=True)
        return redirect(url_for('main.index'))

    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user, remember=True)
            return redirect(url_for('main.index'))
        else:
            flash('Invalid credentials')

    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))