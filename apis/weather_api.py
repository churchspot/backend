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
from config.api_keys import weather_api_key
weather_api = Blueprint('weather_api', __name__)


@weather_api.route('/<city>', methods = ["GET"])
def get_weather(city):
  r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+weather_api_key+'&units=metric&lang=pl')
  if r.ok:
    return r.json()
  elif not r.ok:
    return 'error with request!'


