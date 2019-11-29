"""
 
 ██╗    ██╗███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗      █████╗ ██████╗ ██╗    ██╗  ██╗███████╗██████╗ ███████╗
 ██║    ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗    ██╔══██╗██╔══██╗██║    ██║  ██║██╔════╝██╔══██╗██╔════╝
 ██║ █╗ ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝    ███████║██████╔╝██║    ███████║█████╗  ██████╔╝█████╗  
 ██║███╗██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗    ██╔══██║██╔═══╝ ██║    ██╔══██║██╔══╝  ██╔══██╗██╔══╝  
 ╚███╔███╔╝███████╗██║  ██║   ██║   ██║  ██║███████╗██║  ██║    ██║  ██║██║     ██║    ██║  ██║███████╗██║  ██║███████╗
  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝     ╚═╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
                                                                                                                       
 
"""

from flask import Blueprint
import requests

weather_api = Blueprint('weather_api', __name__)
api_key = '8004ec5d469862255ead99a28fafbe12'

@weather_api.route('/<city>', methods = ["GET"])
def get_weather(city):
  r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+api_key+'&units=metric&lang=pl')
  if r.ok:
    return r.json()
  elif not r.ok:
    return 'error with request!'


