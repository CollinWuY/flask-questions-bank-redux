from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


@app.route("/")
def form():
    return render_template("raw-form.template.html")


@app.route("/", methods=["POST"])
def process_form():
    name = request.form.get("name")
    appetizers = request.form.getlist("appetizers")
    seating = request.form.get("seating")

    total_cost = 0

    if 'seafood' in appetizers:
        total_cost += 3
    
    if 'fries' in appetizers:
        total_cost += 4.50
    
    if 'salad' in appetizers:
        total_cost += 6

    if seating == "vip":
        total_cost += 10

    return render_template('results.template.html',
                           name=name, total_cost=total_cost)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
