from flask import Flask, render_template, request, redirect, url_for
import os
import json

app = Flask(__name__)

database = []
with open('database.json', 'r') as fp:
    database = json.load(fp)


@app.route('/')
def home():
    return "Home page"


@app.route('/new_sighting')
def new_sightning():
    return render_template('new_sighting.template.html')


@app.route('/new_sighting', methods=['POST'])
def process_new_sightning():
    new_sighting = {
        "title": request.form.get("title"),
        "date": request.form.get("date"),
        "time": request.form.get("time"),
        "email": request.form.get("email"),
        "duration": request.form.get("duration"),
        "latitude": request.form.get("latitude"),
        "longtitude": request.form.get("longtitude"),
        "description": request.form.get("description"),
    }
    database.append(new_sighting)
    with open('database.json', 'w') as fp:
        json.dump(database, fp)

    return redirect(url_for('show_sighting'))


@app.route('/show_sighting')
def show_sighting():
    return render_template('show_sighting.template.html', database=database)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=8080,
            debug=True)
