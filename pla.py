import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    'imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres'
)

search = input("Search for movies with this keyword:")

url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search)

resp = requests.get(url)
resp.raise_for_status()

movie_data = resp.json()
movies_list = movie_data.get('hits')

movies = []

for md in movies_list:
    # ### Verbose way
    # m = MovieResult(
    #     imdb_code=md.get('imdb_code'),
    #     title=md.get('title'),
    #     duration=md.get('duration'),
    #     director=md.get('duration'),
    #     year=md.get('year', 0),
    #     rating=md.get('rating', 0),
    #     imdb_score=md.get('imdb_score', 0.0),
    #     keywords=md.get('keywords'),
    #     genres=md.get('genres')
    # )
    # ### as md is a dict we can use key word args (**) to extract the arguments...
    m = MovieResult(**md)
    movies.append(m)

# ## Refactored to use list comprehension
movies_list2 = movies_list
movies2 = [
    MovieResult(**md)
    for md in movies_list
]


print("Found {} movies for search '{}'".format(len(movies), search))
for m in movies:
    print("{} -- {}".format(m.title, m.year))

print('--------------------------')
for m in movies2:
    print("{} -- {}".format(m.year, m.title))
