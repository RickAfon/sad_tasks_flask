from datetime import datetime
from types import NoneType
from typing import Union
from flask_bcrypt import check_password_hash, generate_password_hash
from flask import flash, render_template, request, session, url_for, redirect
from app import app, db
from db_models import Tags, Tasks, Users
from form_models import LoginForm, SignUpForm, TagForm, TaskForm


def get_logged_user() -> Union[NoneType, Users]:
    user = Users.query.filter_by(id=session.get("logged_user")).first()
    return user


@app.route("/")
def index():
    user = get_logged_user()
    if user == None:
        return redirect(url_for("login_page"))
    tasks = Tasks.query.filter_by(user_id=user.id).all()
    return render_template("index.html", tasks=tasks, user=user)


@app.route('/new_task')
def new_task():
    user = get_logged_user()
    if user == None:
        return redirect(url_for("login_page"))
    tags = Tags.query.filter_by(user_id=user.id).all()
    form = TaskForm()
    return render_template("new_task.html", form=form, tags=tags)


@app.route('/save_task', methods=['GET', 'POST'])
def save_task():
    user = get_logged_user()
    if user == None:
        return redirect(url_for("login_page"))
    form = TaskForm(request.form)

    if not form.validate_on_submit():
        return redirect("new_task")

    title = form.title.data
    content = form.content.data
    tag_id = int(form.tag_id.data)
    if tag_id == -1:
        tag_id = None

    new_task = Tasks(title=title, content=content,
                     creation_date=datetime.now(), user_id=user.id, tag_id=tag_id)
    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for("index"))


@app.route("/delete_task/<int:task_id>")
def delete_task(task_id: int):
    user = get_logged_user()
    if user == None:
        return redirect(url_for("login_page"))
    task = Tasks.query.filter_by(id=task_id).first()
    if task != None:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for("index"))


@app.route('/tags')
def tags():
    user = get_logged_user()
    if user == None:
        return redirect(url_for("login_page"))
    tags = Tags.query.filter_by(user_id=user.id).all()
    form = TagForm()
    return render_template("tags.html", tags=tags, form=form)


@app.route('/save_tag', methods=["GET", "POST"])
def save_tag():
    user = get_logged_user()
    if user == None:
        return redirect(url_for("login_page"))
    form = TagForm(request.form)
    new_tag = Tags(name=form.name.data, user_id=user.id)
    db.session.add(new_tag)
    db.session.commit()
    return redirect("tags")


@app.route('/delete_tag/<int:tag_id>')
def delete_tag(tag_id: int):
    user = get_logged_user()
    if user == None:
        return redirect(url_for("login_page"))
    tag = Tags.query.filter_by(id=tag_id).first()
    if tag != None:
        db.session.delete(tag)
        db.session.commit()
    return redirect(url_for("tags"))


@app.route('/login_page')
def login_page():
    form = LoginForm()
    return render_template("login_page.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    user = Users.query.filter_by(email=form.email.data).first()
    if user != None and check_password_hash(user.password, form.password.data):
        session["logged_user"] = user.id
        print(session["logged_user"])
        return redirect(url_for("index"))
    return redirect(url_for("login_page"))


@app.route('/logout')
def logout():
    if "logged_user" in session.keys():
        del session["logged_user"]
    return redirect("login_page")


@app.route("/sign_up")
def sign_up():
    form = SignUpForm()
    return render_template("sign_up.html", form=form)


@app.route("/create_user", methods=["GET", "POST"])
def create_user():
    form = SignUpForm(request.form)
    already_exists = Users.query.filter_by(
        email=form.email.data).first() != None

    if already_exists:
        flash("E-mail already in use")
        return redirect(url_for("sign_up"))

    if form.password.data != form.confirm_password.data:
        flash("Passwords do not match")
        return redirect(url_for("sign_up"))

    password_hash = generate_password_hash(form.password.data).decode("utf-8")
    new_user = Users(name=form.name.data, email=form.email.data,
                     password=password_hash)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("login_page"))
