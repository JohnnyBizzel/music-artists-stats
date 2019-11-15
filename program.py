import artists_svc
import requests.exceptions


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
                artist_id = artists_svc.find_artist(search)
                songs = artists_svc.find_songs_by_artist(artist_id)
                print("Found {} songs when searching for '{}'".format(len(songs), search))
                # for m in results:
                #    print("{} -- {}".format(m.year, m.title))
                # TODO artists_svc.find_song(artist, search)
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
