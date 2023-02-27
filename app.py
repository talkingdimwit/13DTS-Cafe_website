from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

DATABASE = "C:/Users/19037/PycharmProjects/13DTS-Cafe_website/smile.db"

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

@app.route('/menu')
def render_menu_page():  # put application's code here
    con = create_connection(DATABASE)
    query = "SELECT name, description, volume, image, price FROM products"
    cur = con.cursor()
    cur.execute(query)
    product_list = cur.fetchall()
    con.close()
    print(product_list)
    return render_template('menu.html')

@app.route('/contact')
def render_contact_page():  # put application's code here
    return render_template('contact.html')

app.run(host='0.0.0.0', debug=True)