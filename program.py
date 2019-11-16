import artists_svc
import requests.exceptions
import sys


def main():
    print_header()
    search_event_loop()


def print_header():
    print('----------------------------------')
    print('        ARTIST API SEARCH')
    print('----------------------------------')
    print()


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            search = input('Search term (enter x to eXit):')
            if search != 'x':
                artist_d = artists_svc.find_artist(search)
                print(artist_d)
                artist_name = list(artist_d.keys())[0]
                songs = artists_svc.find_songs_by_artist(artist_d[artist_name])
                print("Found {} songs when searching for '{}'".format(len(songs), artist_name))
                words_in_song = []
                for s in songs:
                    print("\nANALYSING SONG -- {}".format(s))
                    words = artists_svc.find_song(artist_name, s)
                    if words is not None and words["count"] is not None and words["count"] > 0:
                        words_in_song.append(words["count"])
                print("\nNum words list {}".format(words_in_song))
                print(sum(words_in_song) / len(words_in_song))
        except ValueError:
            print('Search term is missing or invalid')
        except ConnectionError as ce:
            print('Failed to connect to API')
        except Exception as ex:
            text = sys.exc_info()
            print('Error: {}'.format(text))

    print('>>> exiting')


def mean(lst):
    return sum(lst) / len(lst) 


if __name__ == '__main__':
    main()
