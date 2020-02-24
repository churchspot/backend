from flask import Blueprint, request
import sqlite3
prayers_api = Blueprint('prayers_api', __name__)

@prayers_api.route('/', methods = ["GET"])
def get_prayers():
    return 'modlitwy!'

@prayers_api.route('/add', methods=['POST'])
def add_prayer():
    conn = sqlite3.connect('db')
    c = conn.cursor()
    c.execute('INSERT INTO prayers(Content, Auhtor, IsPublished) VALUES ("' + request.form['content'] +  '","'+ request.form['author'] +'",0)')
    conn.commit()
    c.close()
    return 'Dodano modlitwe'
#INSERT INTO prayers(Content, Auhtor, IsPublished) VALUES ("lorem ipsum dolor sit amet sratara twoja stara jest dupiata", "do usuniecia", 0);