from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.template.html')


@app.route('/',methods=["POST"])
def process_form():
    print(request.form)
    input_value = int(request.form.get("input_value"))
    if input_value == 1:
        image_display = 1
    elif input_value == 2:
        image_display = 2
    else:
        image_display = 3
    return render_template('form.template.html', image_display=image_display)

@app.route('/contact-us')
def show_contact_form():
    return render_template("form.template.html")

@app.route('/contact-us', methods=["POST"])
def process_contact_form():
    print(request.form)
    name = request.form.get("name")
    gender = request.form.get("sex")
    comments = request.form.get("comment")
    can_contact = request.form.get("can-contact")
    accept = "democheckbox" in request.form
    return render_template("display_results.template.html", name=name,
                           gender=gender, comments=comments,
                           can_contact=can_contact, accept=accept)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
