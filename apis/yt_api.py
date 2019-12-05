"""
 
 ██╗   ██╗████████╗     █████╗ ██████╗ ██╗    ██╗  ██╗███████╗██████╗ ███████╗
 ╚██╗ ██╔╝╚══██╔══╝    ██╔══██╗██╔══██╗██║    ██║  ██║██╔════╝██╔══██╗██╔════╝
  ╚████╔╝    ██║       ███████║██████╔╝██║    ███████║█████╗  ██████╔╝█████╗  
   ╚██╔╝     ██║       ██╔══██║██╔═══╝ ██║    ██╔══██║██╔══╝  ██╔══██╗██╔══╝  
    ██║      ██║       ██║  ██║██║     ██║    ██║  ██║███████╗██║  ██║███████╗
    ╚═╝      ╚═╝       ╚═╝  ╚═╝╚═╝     ╚═╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
                                                                              
 
"""


from flask import Blueprint
import requests

yt_api = Blueprint('yt_api', __name__)
from config.api_keys import yt_api_key
from config.yt_channels import yt_channels
import json
# https://www.googleapis.com/youtube/v3/search?key=AIzaSyCIhIfjiJD1jX7sI9g8OXNlFXIaA9aLliA&channelId=UC5KNKlhUr1Cy7fKuO4LRsaQ&part=snippet,id&order=date&maxResults=1


@yt_api.route('/', methods = ["GET"])
def get_newest_films():
    data = []
    for channel in yt_channels:
        r = requests.get('https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=1'.format(api_key=yt_api_key, channel_id=channel))
        if r.ok:
            data.append(r.json());
        elif not r.ok:
            return 'error with request!'
    return json.dumps(data)


