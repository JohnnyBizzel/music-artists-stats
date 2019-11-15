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
                first = artists_svc.find_song(artist_name, songs[0])
                print(first)
                second = artists_svc.find_song(artist_name, songs[1])
                print(second)
                # for s in songs:
                #   print("{} -- {}".format(m.year, m.title))
                #   artists_svc.find_song(artist_name, search)
        except ValueError:
            print('Search term is missing or invalid')
        except ConnectionError as ce:
            print('Failed to connect to API')
        except Exception as ex:
            text = sys.exc_info()
            print('Error: {}'.format(text))

    print('>>> exiting')


if __name__ == '__main__':
    main()
