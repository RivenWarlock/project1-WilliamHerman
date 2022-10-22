import flask
import os
import requests
import json
from dotenv import load_dotenv, find_dotenv
from random import randrange

load_dotenv(find_dotenv()) 

app = flask.Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return index()

 #main url to get values from movie site
BASE_URL = 'https://api.themoviedb.org/3/movie/'
POSTER_CONFIGURATION = 'https://api.themoviedb.org/3/configuration'

def index():
    movie_list = ['634649', '557', '324857'] #values that identify the movies. They are all spiderman.
    the_movie_id = movie_list[randrange(3)]
    
    request_url= f'{BASE_URL}{the_movie_id}'
    print(request_url)
   
    response = requests.get(
        request_url,
    params={
        'api_key': os.getenv('TMDB_API_KEY')
        }
    )

    weekly_trending_movie_object = response.json()
    #make a request for these values in the dictionary.
    print(weekly_trending_movie_object['title'])
    print(weekly_trending_movie_object['tagline'])
    print(weekly_trending_movie_object['genres'])
    print(weekly_trending_movie_object['poster_path'])
    S = requests.Session()
    #Wiki api url link
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "opensearch",
        "search": weekly_trending_movie_object['title'],
        "title": weekly_trending_movie_object['title'],
        "format": "json",
        "prop": "info",
        "inprop": "url"
    }
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    print(DATA)
    print(DATA[3][0]) #this request the specific movie hyperlink address.

    return flask.render_template("index.html", title=weekly_trending_movie_object['title'],
    tagline=weekly_trending_movie_object['tagline'], genres=weekly_trending_movie_object['genres'],
    poster_path=weekly_trending_movie_object['poster_path'], wiki_url=DATA[3][0])

app.run()
print(index())