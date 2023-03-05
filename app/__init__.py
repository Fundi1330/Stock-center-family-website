from flask import Flask, render_template, flash, redirect, request, url_for
from app.models import db
from flask_migrate import Migrate

from datetime import datetime
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from app.forms import RegestrationForm, LoginForm, AddGoodForm
from app.models import User, Goods
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)
app.config["SECRET_KEY"] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.app_context().push()


db.init_app(app)
migrate = Migrate(app, db)

login = LoginManager(app)


@app.before_first_request
def create_tables():
    db.create_all()

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
@app.route('/index')
def index():
    aunteficated = True
    if current_user.is_authenticated:
        aunteficated = False
    latest_good_list = Goods.query.order_by(Goods.publish_date).all()[0:3]
    return render_template('index.html', title='Головна', aunteficated=aunteficated, latest_good_list=latest_good_list)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
       return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Неправильний логін або пароль")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("index"))
    
    return render_template("login.html", title="Sign in", form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegestrationForm()
    if form.validate_on_submit():
        flash("Ви успішно зареєструвалися!")
        user = User(username=form.username.data, email=form.email.data, password_hash=form.password.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/cart/<username>')
@login_required
def cart(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('cart.html', user=user)

@app.route('/good/<goodname>', methods=['GET', 'POST'])
def good(goodname):
    good = Goods.query.filter_by(name=goodname).first()
    return render_template('good.html', good=good)

@app.route('/goods')
def goods():
    good_list = Goods.query.all()
    return render_template('goods.html', title='Каталог', good_list=good_list)

@app.route('/add_good', methods=["GET", "POST"])
def add_good():
    form = AddGoodForm()
    if form.validate_on_submit():
        good = Goods(name=form.name.data, descreption=form.descreption.data,
        price=form.price.data, size=form.size.data, matherial=form.matherial.data,
        type=request.form['type'], quantity=form.quantity.data, in_stock=request.form['in_stock'], image_name=form.name.data, datetime=datetime.now())
        db.session.add(good)
        db.session.commit()
        flash('Товар успішно доданий на сайт')
        return redirect(url_for("index"))
    return render_template('add_good.html', title='Add good', form=form)