from datetime import datetime
from flask import render_template
from app import app
from models import Task

@app.route("/")
def index():
    tasks = [
        Task('Do something','School', '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas facilisis sed sapien eget
                        lacinia. Aenean enim est, laoreet eu mauris vel, pharetra elementum leo. Sed pellentesque eget
                        mi vitae imperdiet. Donec nec odio leo. Aliquam interdum at orci id tincidunt. Maecenas ante
                        ligula, dignissim et finibus a, malesuada ac ex.''', datetime.now()),
        Task('Do something','Work', '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas facilisis sed sapien eget
                        lacinia. Aenean enim est, laoreet eu mauris vel, pharetra elementum leo. Sed pellentesque eget
                        mi vitae imperdiet. Donec nec odio leo. Aliquam interdum at orci id tincidunt. Maecenas ante
                        ligula, dignissim et finibus a, malesuada ac ex.''', datetime.now()),
        Task('Do something', None, '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas facilisis sed sapien eget
                        lacinia. Aenean enim est, laoreet eu mauris vel, pharetra elementum leo. Sed pellentesque eget
                        mi vitae imperdiet. Donec nec odio leo. Aliquam interdum at orci id tincidunt. Maecenas ante
                        ligula, dignissim et finibus a, malesuada ac ex.''', datetime.now()),
        Task('Do something','School', '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas facilisis sed sapien eget
                        lacinia. Aenean enim est, laoreet eu mauris vel, pharetra elementum leo. Sed pellentesque eget
                        mi vitae imperdiet. Donec nec odio leo. Aliquam interdum at orci id tincidunt. Maecenas ante
                        ligula, dignissim et finibus a, malesuada ac ex.''', datetime.now()),
        Task('Do something','School', None, datetime.now()),
        Task('Do something',None, None, datetime.now())
    ]
    return render_template("index.html", tasks=tasks)