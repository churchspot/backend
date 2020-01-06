from flask import Blueprint
import time
import requests 
from bs4 import BeautifulSoup

day_info = Blueprint("day_info", __name__)
name_day_info = Blueprint("name_day_info", __name__)

@day_info.route("/", methods = ["GET"])
def get_date():
    return time.strftime("%d/%m/%Y" + " %H:%M:%S")

@name_day_info.route("/", methods = ["GET"])
def get_name_day():
    r = requests.get('https://api.abalin.net/today?country=pl')
    if r.ok:
        return r.json()
    elif not r.ok:
        return 'error with request!'
    # r = requests.get("https://imienniczek.pl/widget/js")
    # if r.ok:
    #     string = r.text[16:]
    #     new_string = string.replace("'", "")
    #     new_string = new_string.replace(")", "")
    #     new_string = new_string.replace(";", "")
    #     html = new_string
    #     p = BeautifulSoup(html)
    #     list_of_a = p.find_all("a")
    #     string = ''
    #     for x in list_of_a:
    #         string += x.text + " "
    #     return string
    # elif not r.ok:
    #     return 'error with request!'

