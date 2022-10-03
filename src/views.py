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

    if not form.validate_on_submit():
        return redirect("new_task")

    title = form.title.data
    content = form.content.data
    
    new_task = Tasks(title=title, content=content, creation_date=datetime.now(), user_id=1)
    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for("index"))
