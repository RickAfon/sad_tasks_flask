from datetime import datetime
from flask import render_template, request, session, url_for, redirect
from sqlalchemy import delete
from app import app, db
from db_models import Tags, Tasks, Users
from models import Task
from form_models import LoginForm, TagForm, TaskForm


@app.route("/")
def index():
    user = Users.query.filter_by(id=session["logged_user"]).first(
    ) if "logged_user" in session.keys() else None
    tasks = Tasks.query.all()
    return render_template("index.html", tasks=tasks, user=user)


@app.route('/new_task')
def new_task():
    tags = Tags.query.filter_by(user_id=1).all()
    form = TaskForm()
    return render_template("new_task.html", form=form, tags=tags)


@app.route('/save_task', methods=['GET', 'POST'])
def save_task():
    form = TaskForm(request.form)

    if not form.validate_on_submit():
        return redirect("new_task")

    title = form.title.data
    content = form.content.data
    tag_id = int(form.tag_id.data)
    if tag_id == -1:
        tag_id = None

    new_task = Tasks(title=title, content=content,
                     creation_date=datetime.now(), user_id=1, tag_id=tag_id)
    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for("index"))


@app.route("/delete_task/<int:task_id>")
def delete_task(task_id: int):
    task = Tasks.query.filter_by(id=task_id).first()
    if task != None:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for("index"))


@app.route('/tags')
def tags():
    tags = Tags.query.filter_by(user_id=1).all()
    form = TagForm()
    return render_template("tags.html", tags=tags, form=form)


@app.route('/save_tag', methods=["GET", "POST"])
def save_tag():
    form = TagForm(request.form)
    new_tag = Tags(name=form.name.data, user_id=1)
    db.session.add(new_tag)
    db.session.commit()
    return redirect("tags")


@app.route('/delete_tag/<int:tag_id>')
def method_name(tag_id: int):
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
    if user != None and user.password == form.password.data:
        session["logged_user"] = user.id
        print(session["logged_user"])
        return redirect(url_for("index"))
    return redirect(url_for("login_page"))


@app.route('/logout')
def logout():
    if "logged_user" in session.keys():
        del session["logged_user"]
    return redirect("login_page")
