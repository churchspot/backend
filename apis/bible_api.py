"""
 
 ██████╗ ██╗██████╗ ██╗     ███████╗     █████╗ ██████╗ ██╗
 ██╔══██╗██║██╔══██╗██║     ██╔════╝    ██╔══██╗██╔══██╗██║
 ██████╔╝██║██████╔╝██║     █████╗      ███████║██████╔╝██║
 ██╔══██╗██║██╔══██╗██║     ██╔══╝      ██╔══██║██╔═══╝ ██║
 ██████╔╝██║██████╔╝███████╗███████╗    ██║  ██║██║     ██║
 ╚═════╝ ╚═╝╚═════╝ ╚══════╝╚══════╝    ╚═╝  ╚═╝╚═╝     ╚═╝
                                                           
 
"""

from flask import Blueprint
import requests

bible_api  = Blueprint('bible_api', __name__)

api_key = 'f806b6a7470452382d626c976b70074b';


@bible_api.route('/get-random')
def get_random_verse():
    r = requests.get('https://api.scripture.api.bible/v1/bibles/1c9761e0230da6e0-01',headers= {
        'api-key': api_key
    })
    if r.ok:
        return r.json()
    else:
        return 'error with request!'