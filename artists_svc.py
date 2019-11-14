import requests
import collections

SearchResults = collections.namedtuple(
    'MovieResult',
    'lyrics')

def find_artist(search_keyword):

    if not search_keyword or not search_keyword.strip():
        raise ValueError("Search term required!")

    url = 'https://musicbrainz.org/ws/2/artist/?query=artist:{}&limit=1&fmt=json'.format(search_keyword)

    resp = requests.get(url)
    resp.raise_for_status()

    artist_data = resp.json()
    artists_list = artist_data.get('artists')
    
    print("{} {}".format(artists_list[0]["name"], artists_list[0]["id"]))

    # word_length = len(artists_list.split());
    # word_count_text = "\nNumber of words = {}".format(word_length);

    # artists.sort(key=lambda m: -m.year)  # minus sorts descending

    return artists_list[0]["id"]
    

def find_songs_by_artist(artist_id):

    if not artist_id:
        raise ValueError("Artist not found :(")

    url = 'https://musicbrainz.org/ws/2/recording?query=arid:{}&fmt=json&limit=100&offset=1'.format(artist_id)
    print(url)
    resp = requests.get(url)
    resp.raise_for_status()

    artist_data = resp.json()
    artists_recs = artist_data.get('recordings')
    print(len(artists_recs))
    # lyric_words = artists_list.split()
    
    for song in artists_recs:
        print(song["title"])

    # word_length = len(artists_list.split());
    # word_count_text = "\nNumber of words = {}".format(word_length);
    # artists.sort(key=lambda m: -m.year)  # minus sorts descending

    return len(artists_recs)


def find_song(artist, search_keyword):

    if not search_keyword or not search_keyword.strip():
        raise ValueError("Search term required!")

    url = 'https://api.lyrics.ovh/v1/{}/{}'.format(artist, search_keyword)

    resp = requests.get(url)
    resp.raise_for_status()

    artist_data = resp.json()
    artists_list = artist_data.get('lyrics')

    lyric_words = artists_list.split()
    
    for md in lyric_words:
        print(md)

    word_length = len(artists_list.split());
    word_count_text = "\nNumber of words in song = {}".format(word_length);

    # artists.sort(key=lambda m: -m.year)  # minus sorts descending

    return word_count_text

