import artists_svc
import requests.exceptions
import sys


def main():
    print_header()
    search_event_loop()


def print_header():
    print('----------------------------------')
    print('     MUSIC ARTIST API SEARCH')
    print('----------------------------------')
    print()


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            search = input("Search for an artist (enter x to eXit):")
            if search != 'x':
                artist_dict = artists_svc.find_artist(search)
                if artist_dict == "x":  # user did not choose an artist
                    continue
                artist_name = list(artist_dict.keys())[0]
                songs = artists_svc.find_songs_by_artist(artist_dict[artist_name])
                print("Found {} songs for '{}'".format(len(songs), artist_name))
                words_in_song = []
                lyrics_list = []
                for s in songs:
                    print("\nANALYSING SONG -- {}".format(s))
                    words = artists_svc.find_song(artist_name, s)
                    if words is not None and words["count"] is not None and words["count"] > 0:
                        if words["lyrics"] is not None and words["lyrics"] not in lyrics_list:
                            lyrics_list.append(words["lyrics"])
                            words_in_song.append(words["count"])
                print("\nNumber of song lyrics found {}".format(len(words_in_song)))
                print("\nAverage words in a song {:.1f}".format(sum(words_in_song) / len(words_in_song)))
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
