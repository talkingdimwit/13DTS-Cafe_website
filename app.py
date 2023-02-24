from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_homepage():  # put application's code here
    return render_template('home.html')

@app.route('/menu')
def render_menu_page():  # put application's code here
    return render_template('menu.html')

@app.route('/contact')
def render_contact_page():  # put application's code here
    return render_template('contact.html')

app.run(host='0.0.0.0', debug=True)