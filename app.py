from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.movieproject  # 'movieproject'라는 이름의 db를 만듭니다.

@app.route('/')
def home():
    return render_template('index.html')

import requests

for page_num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    url = "https://api.themoviedb.org/3/movie/upcoming?api_key=5f7bf7c14846dfb7be7dcb66ee46a81a&language=ko-KR&page=" + str(page_num)
    response_data = requests.get(url)
    movie_list = response_data.json()
    movie_result = movie_list['results']

    for movie in movie_result:
        title = movie['title']
        overview = movie['overview']
        poster_path = movie['poster_path']
        release_date= movie['release_date']

        movie = {
            'title': title,
            'overview': overview,
            'poster_path': poster_path,
            'release_date' : release_date
        }
        db.movies.insert_one(movie)

@app.route('/movies', methods=['GET'])
def read_movies():
    movies_list=list(db.movies.find({}))
    return jsonify({'result': 'success', 'movies_list':movies_list})