from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

DATABASE ="C:/Users/maxmo/PycharmProjects/13DTS-Cafe_website/smile.db"  #C:/Users/19037/PycharmProjects/13DTS-Cafe_website/smile.db

app = Flask(__name__)

def create_connection(db_file):
    """
    create a connection with a database
    :parameter name of the database
    :return a connection to the file
    """
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None

@app.route('/')
def render_homepage():  # put application's code here
    return render_template('home.html')

@app.route('/menu/<cat_id>')
def render_menu_page(cat_id):  # put application's code here
    con = create_connection(DATABASE)
    query = "SELECT name, description, volume, image, price FROM products WHERE cat_id=?"
    cur = con.cursor()
    cur.execute(query, (cat_id, ))
    product_list = cur.fetchall()
    query = "SELECT id, name FROM category"
    cur = con.cursor()
    cur.execute(query)
    category_list = cur.fetchall()
    con.close()
    print(product_list)
    return render_template('menu.html', products=product_list, categories=category_list)

@app.route('/contact')
def render_contact_page():  # put application's code here
    return render_template('contact.html')

@app.route('/login', methods=['POST', 'GET'])
def render_login_page():  # put application's code here
    return render_template('login.html')

@app.route('/signup', methods=['POST', 'GET'])
def render_signup_page():  # put application's code here
    if request.method = validate(request.form.get('f.name'))
        print(request.form)
    return render_template('signup.html')

app.run(host='0.0.0.0', debug=True)