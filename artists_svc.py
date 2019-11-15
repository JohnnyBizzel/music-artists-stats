import requests
import collections
import time

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

    # first find the number of songs in the database
    url = 'https://musicbrainz.org/ws/2/recording?query=arid:{}&fmt=json&limit=1&offset=0'.format(artist_id)
    print(url)
    resp = requests.get(url)
    resp.raise_for_status()

    artist_data = resp.json()
    songs_found = artist_data.get('count')
    print("Found {} songs in the DB".format(songs_found))

    # Now call the service to retrieve all songs as there is a limit on the API of max 100 records
    num_songs_left = songs_found

    # Calculate number of calls (batches of 100 records needed)
    loops_needed = num_songs_left // 100
    print("\nLooping {} times".format(loops_needed))
    offsetting = 0
    artist_songs = []

    while (loops_needed >= 0):
        url = 'https://musicbrainz.org/ws/2/recording?query=arid:{}&fmt=json&limit=100&offset={}'.format(artist_id,
                                                                                                         offsetting)
        print('Getting data...')
        time.sleep(0.5)
        resp = requests.get(url)
        resp.raise_for_status()
        artist_data = resp.json()
        artist_songs += artist_data.get('recordings')
        loops_needed -= 1
        offsetting += 100

    artist_songs_unique = []
    for item in artist_songs:
        if 'releases' not in item:
            continue
        print(item["releases"][0])
        releases = item["releases"][0]["release-group"]
        if ('secondary-types' in releases and
                ("Compilation" in releases["secondary-types"] or
                    "Remix" in releases["secondary-types"])):
                        print('compilation')
                        continue
        try:
            print(releases)
            if 'primary-type' in releases and releases['primary-type'] == 'Single':
                print(True)
        except Exception as x:
            print("broken...{}".format(x))

        if item["title"] not in artist_songs_unique:
            artist_songs_unique.append(item["title"])

    for song in artist_songs_unique:
        print(song)

    return artist_songs_unique


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
