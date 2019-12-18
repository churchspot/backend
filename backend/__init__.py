from flask import Flask
from apis.weather_api import weather_api
from apis.bible_api import bible_api
from apis.yt_api import yt_api
from flask_cors import CORS
from apis.day_info import day_info
from apis.day_info import name_day_info
app = Flask(__name__)

"""
 
 ███╗   ███╗ █████╗ ██╗███╗   ██╗    ███████╗██╗██╗     ███████╗
 ████╗ ████║██╔══██╗██║████╗  ██║    ██╔════╝██║██║     ██╔════╝
 ██╔████╔██║███████║██║██╔██╗ ██║    █████╗  ██║██║     █████╗  
 ██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██╔══╝  ██║██║     ██╔══╝  
 ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ██║     ██║███████╗███████╗
 ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚══════╝╚══════╝
                                                                
 
"""


app.register_blueprint(weather_api, url_prefix='/api/weather/')
app.register_blueprint(bible_api, url_prefix='/api/bible/')
app.register_blueprint(yt_api, url_prefix='/api/yt/')
app.register_blueprint(day_info, url_prefix='/api/day_info')
app.register_blueprint(name_day_info, url_prefix="/api/name_day_info")
CORS(app)
@app.route('/')
def hello():
    return 'Hello, World!'

