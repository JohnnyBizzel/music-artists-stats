import requests
import collections

SearchResults = collections.namedtuple(
    'MovieResult',
    'lyrics')


def find_artists(search_keyword):

    if not search_keyword or not search_keyword.strip():
        raise ValueError("Search term required!")

    url = 'https://api.lyrics.ovh/v1/Mariah Carey/{}'.format(search_keyword)

    resp = requests.get(url)
    resp.raise_for_status()

    artist_data = resp.json()
    artists_list = artist_data.get('lyrics')

    lyric_words = artists_list.split()
    
    for md in lyric_words:
        print(md)

    word_length = len(artists_list.split());
    word_count_text = "\nNumber of words = {}".format(word_length);

    # artists.sort(key=lambda m: -m.year)  # minus sorts descending

    return word_count_text

