from datetime import datetime
from urllib.robotparser import RequestRate
from flask import render_template, request, url_for, redirect
from app import app
from models import Task, TaskForm


@app.route("/")
def index():
    tasks = [
        Task('Do something', 'School', '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas facilisis sed sapien eget
                        lacinia. Aenean enim est, laoreet eu mauris vel, pharetra elementum leo. Sed pellentesque eget
                        mi vitae imperdiet. Donec nec odio leo. Aliquam interdum at orci id tincidunt. Maecenas ante
                        ligula, dignissim et finibus a, malesuada ac ex.''', datetime.now()),
        Task('Do something', 'Work', '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas facilisis sed sapien eget
                        lacinia. Aenean enim est, laoreet eu mauris vel, pharetra elementum leo. Sed pellentesque eget
                        mi vitae imperdiet. Donec nec odio leo. Aliquam interdum at orci id tincidunt. Maecenas ante
                        ligula, dignissim et finibus a, malesuada ac ex.''', datetime.now()),
        Task('Do something', None, '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas facilisis sed sapien eget
                        lacinia. Aenean enim est, laoreet eu mauris vel, pharetra elementum leo. Sed pellentesque eget
                        mi vitae imperdiet. Donec nec odio leo. Aliquam interdum at orci id tincidunt. Maecenas ante
                        ligula, dignissim et finibus a, malesuada ac ex.''', datetime.now()),
        Task('Do something', 'School', '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas facilisis sed sapien eget
                        lacinia. Aenean enim est, laoreet eu mauris vel, pharetra elementum leo. Sed pellentesque eget
                        mi vitae imperdiet. Donec nec odio leo. Aliquam interdum at orci id tincidunt. Maecenas ante
                        ligula, dignissim et finibus a, malesuada ac ex.''', datetime.now()),
        Task('Do something', 'School', None, datetime.now()),
        Task('Do something', None, None, datetime.now())
    ]
    return render_template("index.html", tasks=tasks)


@app.route('/new_task')
def new_task():
    form = TaskForm()
    return render_template("new_task.html", form=form)


@app.route('/save_task', methods=['GET', 'POST'])
def save_task():
    form = TaskForm(request.form)
    return redirect(url_for("new_task"))
