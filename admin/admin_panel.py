from flask import Blueprint, render_template, request, redirect, jsonify, make_response
from config.admin_config import admin_panel_route
admin_panel  = Blueprint('admin_panel', __name__)
import sqlite3


@admin_panel.route('/' + admin_panel_route)
def show_login_panel():
    return render_template('login.html', admin_panel_route=admin_panel_route)


@admin_panel.route('/' + admin_panel_route + '/login', methods=['POST'])
def login():
    login_attempt = request.form['login']
    password_attempt = request.form['password']
    conn = sqlite3.connect('db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE Login="' + login_attempt + '"')
    r = c.fetchall()
    if len(r) > 0:
        if r[0][2] == password_attempt:
            resp = make_response( render_template('logged.html',username= r[0][1]))
            resp.set_cookie('user_id', str(r[0][0]))
            resp.set_cookie('username', str(r[0][1]))
            resp.set_cookie('is_logged', 'true')
            return resp

        else:
            return "Nieprawidłowe dane!"
    else:
        return "Nieprawidłowe dane!"

@admin_panel.route('/' + admin_panel_route + '/panel', methods=['GET'])
def display_admin_panel():
    if  request.cookies.get('is_logged') == 'true':
        return render_template('admin_panel.html',username= request.cookies.get('username'))
    else:
        return "Nieprawidłowe dane"

@admin_panel.route('/' + admin_panel_route + '/panel/unpublished_prayers', methods=['GET'])
def list_unpublished_prayers():
    if  request.cookies.get('is_logged') == 'true':
        conn = sqlite3.connect('db')
        c = conn.cursor()
        c.execute('SELECT * FROM prayers WHERE IsPublished=0')
        prayers = c.fetchall()
        return render_template('unpublished_prayers_list.html',username= request.cookies.get('username'), prayers = prayers, route=admin_panel_route)
    else:
        return "Nieprawidłowe dane" 

@admin_panel.route('/' + admin_panel_route + '/panel/published_prayers', methods=['GET'])
def list_published_prayers():
    if  request.cookies.get('is_logged') == 'true':
        conn = sqlite3.connect('db')
        c = conn.cursor()
        c.execute('SELECT * FROM prayers WHERE IsPublished=1')
        prayers = c.fetchall()
        return render_template('published_prayers_list.html',username= request.cookies.get('username'), prayers = prayers, route=admin_panel_route)
    else:
        return "Nieprawidłowe dane" 


@admin_panel.route('/' + admin_panel_route + '/panel/prayers/publish/<id>', methods=['GET'])
def publish_prayer(id):
    if  request.cookies.get('is_logged') == 'true':
        conn = sqlite3.connect('db')
        c = conn.cursor()
        c.execute('UPDATE prayers SET IsPublished=1  WHERE Id=' + id)
        conn.commit()
        c.close()
        return "Opublikowano modlitwe z id: " + id
    else:
        return "Musisz sie zalogowac by to zrobic"


@admin_panel.route('/' + admin_panel_route + '/panel/prayers/delete/<id>', methods=['GET'])
def delete_prayer(id):
    if  request.cookies.get('is_logged') == 'true':
        conn = sqlite3.connect('db')
        c = conn.cursor()
        c.execute('DELETE FROM prayers WHERE id=' + id)
        conn.commit()
        c.close()
        return "Usunieto modlitwe z id: " + id
    else:
        return "Musisz sie zalogowac by to zrobic"