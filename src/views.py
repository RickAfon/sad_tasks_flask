from datetime import datetime
from flask import render_template, request, url_for, redirect
from app import app, db
from db_models import Tags, Tasks, Users
from models import Task
from form_models import TaskForm


@app.route("/")
def index():
    tasks = Tasks.query.all()
    print(tasks[0].creation_date.strftime('%d/%m/%y'))
    return render_template("index.html", tasks=tasks)


@app.route('/new_task')
def new_task():
    form = TaskForm()
    return render_template("new_task.html", form=form)


@app.route('/save_task', methods=['GET', 'POST'])
def save_task():
    form = TaskForm(request.form)
    return redirect(url_for("new_task"))
