from flask import Flask
from apis.weather_api import weather_api
from apis.bible_api import bible_api
from apis.yt_api import yt_api
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
@app.route('/')
def hello():
    return 'Hello, World!'