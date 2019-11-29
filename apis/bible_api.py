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

import random
bible_api  = Blueprint('bible_api', __name__)

api_key = 'f806b6a7470452382d626c976b70074b';


@bible_api.route('/get-random', methods = ["GET"])
def get_random_verse():
    verses = [ 
    'JER.29.11',
    'PHP.4.13',
    'JHN.3.16',
    'ROM.8.28',
    'ISA.41.10',
    'PSA.46.1',
    'GAL.5.22-23',
    'HEB.11.1',
    '2TI.1.7',
    'PRO.22.6',
    'ISA.40.31',
    'JOS.1.9',
    'HEB.12.2',
    'MAT.11.28',
    ]
    index = random.choice(verses)
    print(index)
    r = requests.get('https://api.scripture.api.bible/v1/bibles/1c9761e0230da6e0-01/verses/'+index,headers= {
        'api-key': api_key
    })
    r = r.json()
    return r