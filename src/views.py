from datetime import datetime
from flask import render_template, request, url_for, redirect
from sqlalchemy import delete
from app import app, db
from db_models import Tags, Tasks, Users
from models import Task
from form_models import TaskForm


@app.route("/")
def index():
    tasks = Tasks.query.all()
    return render_template("index.html", tasks=tasks)


@app.route('/new_task')
def new_task():
    form = TaskForm()
    return render_template("new_task.html", form=form)


@app.route('/save_task', methods=['GET', 'POST'])
def save_task():
    form = TaskForm(request.form)

    if not form.validate_on_submit():
        return redirect("new_task")

    title = form.title.data
    content = form.content.data
    
    new_task = Tasks(title=title, content=content, creation_date=datetime.now(), user_id=1)
    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for("index"))


@app.route("/delete_task/<int:task_id>")
def delete_task(task_id: int):
    task = Tasks.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("index"))