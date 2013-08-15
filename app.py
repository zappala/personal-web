import sys

from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html',active='index')

def add(schedule,days,time,item):
    for d in days:
        if d == 'M':
            day = 'Monday'
        if d == 'T':
            day = 'Tuesday'
        if d == 'W':
            day = 'Wednesday'
        if d == 'H':
            day = 'Thursday'
        if d == 'F':
            day = 'Friday'
        schedule[day][time] = item

@app.route('/schedule')
def schedule():
    times = ['9:00','10:00','11:00','12:00','1:00','2:00','3:00','4:00']
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday']
    schedule = {}
    for day in days:
        schedule[day] = {}
        for time in times:
            schedule[day][time] = ''
    add(schedule,'MWF','1:00','CS 660')
    add(schedule,'MWF','3:00','CS 360')
    add(schedule,'MWF','4:00','Office Hours')
    add(schedule,'T','11:00','Devotional')
    add(schedule,'H','11:00','Colloquium')
    return render_template('schedule.html',active='schedule',
                           times=times,days=days,schedule=schedule)


@app.route('/<directory>',defaults={'page':''})
@app.route('/<directory>/<page>')
def show(directory,page):
    if not page:
        return render_template(directory+'.html',active=directory)
    return render_template(directory+"/" + page + '.html',active=directory)
    

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.debug = True
        app.run(port=8080)
