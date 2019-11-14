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
                results = artists_svc.find_artists(search)
                print(results)
                # print("Found {} movies for search '{}'".format(len(results), search))
		
                #for m in results:
                #    print("{} -- {}".format(m.year, m.title))
        except ValueError:
            print('Search term is missing or invalid')
        except ConnectionError as ce:
            print('Failed to connect to API')
        except Exception as ex:
            print('Error: {}'.format(ex))

    print('>>> exiting')


if __name__ == '__main__':
    main()
