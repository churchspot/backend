from flask import Flask
from apis.weather_api import weather_api
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
@app.route('/')
def hello():
    return 'Hello, World!'