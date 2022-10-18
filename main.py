import flask
import os
import requests
import json
from dotenv import load_dotenv, find_dotenv
from random import randrange

load_dotenv(find_dotenv()) 

app = flask.Flask(__name__)

@app.route("/")
def home():
    return "<h1>my flask page</h1>"

 
BASE_URL = 'https://api.themoviedb.org/3/movie/'

def index():
    movie_list = ['634649', '557', '324857']
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
    print(weekly_trending_movie_object['title'])
    print(weekly_trending_movie_object['tagline'])
    print(weekly_trending_movie_object['genres'])
    print(weekly_trending_movie_object['poster_path'])
    return flask.render_template("index.html", title=weekly_trending_movie_object['title'])

app.run()
