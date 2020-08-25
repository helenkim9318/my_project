from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.movieproject  # 'movieproject'라는 이름의 db를 만듭니다.

import requests  # requests 라이브러리 설치 필요

for page_num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    url = "https://api.themoviedb.org/3/movie/upcoming?api_key=5f7bf7c14846dfb7be7dcb66ee46a81a&language=ko-KR&page=" + str(page_num)
    response_data = requests.get(url)
    movie_list = response_data.json()
    movie_result = movie_list['results']

    for movie in movie_result:
        title = movie['title']
        overview = movie['overview']
        genre_ids = movie['genre_ids']
        poster_path = movie['poster_path']
        release_date= movie['release_date']

        movie = {
            'title': title,
            'overview': overview,
            'genre_ids': genre_ids,
            'poster_path': poster_path,
            'release_date' : release_date
        }
        db.movies.insert_one(movie)


# api of movie of certain genrre id: https://api.themoviedb.org/3/movie/upcoming?api_key=5f7bf7c14846dfb7be7dcb66ee46a81a&language=ko-KR&with_genres=28
# api of list of genres https://api.themoviedb.org/3/genre/movie/list?api_key=5f7bf7c14846dfb7be7dcb66ee46a81a&language=ko-KR