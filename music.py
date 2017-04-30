import csv
import random


def new_album():
    # create list of tuples with the data given by the user

    name_art = input('write a name of artist\n')
    name_album = input('write a name of album\n')
    year = input('writa a year of release\n')
    genre = input('write a genre\n')
    length = input('write a length of album\n')
    music = [(name_art, name_album), (year, genre, length)]
    return music


def append_to_file(album_to_write):
    # add album to csv file

    filecsv = open('music.csv', 'a')
    to_write = ""
    for x in range(len(album_to_write)):
        for y in range(len(album_to_write[x])):
            to_write += album_to_write[x][y]
            if not (x == (len(album_to_write)-1) and y == (len(album_to_write[x])-1)):
                to_write += " | "
    filecsv.write(to_write + '\n')


def load_from_file():
    # function loads data from csv file in to list of tuples of tuples 

    filecsv = open('music2.csv', 'r')
    reader = csv.reader(filecsv)
    name_art = ""
    name_album = ""
    year = ""
    genre = ""
    length = ""
    albums_list = []
    for row in reader:
        splitted = str(row).split(' | ')
        name_art = splitted[0].replace('[\'', "").replace('\']', "")
        name_album = splitted[1].replace('[\'', "").replace('\']', "")
        year = splitted[2].replace('[\'', "").replace('\']', "")
        genre = splitted[3].replace('[\'', "").replace('\']', "")
        length = splitted[4].replace('[\'', "").replace('\']', "")

        album = ((name_art, name_album), (year, genre, length))
        albums_list.append(album)
    return albums_list


def find_by_artist(album_list, artist):
    # function search for artist in list album_list and return list of found albums

    return_albums = []
    artist_list = []
    for album in album_list:
        if tuple(album)[0][0] == artist:
            return_albums.append(tuple(album))
    if len(return_albums) == 0:
        print('Artist not found! ')
    return return_albums


def find_by_year(album_list, year):
    # function search for year in list album_list and return list of found albums

    return_albums = []
    for album in album_list:
        if tuple(album)[1][0] == year:
            return_albums.append(tuple(album))
    if len(return_albums) == 0:
        print('Artist not found! ')
    return return_albums


def find_artist_by_album(album_list, album_name):
    # function search for album_name in list album_list and return artist name

    return_artist = ""
    for album in album_list:
        if tuple(album)[0][1] == album_name:
            return_artist = tuple(album)[0][0]
    return return_artist


def find_by_letters(album_list, letters):
    # function search for first ltters in album name in list album_list and return list of found albums

    return_albums = []
    for lett in album_list:
        if tuple(lett)[0][1].lower().startswith(str(letters).lower()):
            return_albums.append(tuple(lett))
    return return_albums


def find_by_genre(album_list, genre):
    # function search for genre in list album_list and return list of found albums

    return_albums = []
    for album in album_list:
        if tuple(album)[1][1] == genre:
            return_albums.append(tuple(album))
    return return_albums


def calculate_age_all_albums(album_list):
    # function calculate ages of albums in list album_list and return sum of ages

    return_age = []
    for album in album_list:
        return_age += [2017 - int((album)[1][0])]
    print('Age of all albus is: %d years' % sum(return_age))


def choose_random_album_by_genre(album_list, genre):
    # function randomize album from list album_list with specified genre

    list_albums = find_by_genre(album_list, genre)
    los = random.randint(0, len(list_albums)-1)
    print(" Albums: " + list_albums[los][0][1], " Artist: " + list_albums[los][0][0])


def longest_time_album(album_list):
    # function search for album with longest duration

    max = album_list[0]
    for x in album_list:
        res = compare(x[1][2], max[1][2])
        if(res == 'a'):
            max = x
    return max


def compare(a, b):
    # function compares two durations and returns indicator whitch one is longer

    A = a.split(':')
    B = b.split(':')
    if A[0] > B[0]:
        return 'a'
    elif A[0] == B[0]:
        if A[1] > B[1]:
            return 'a'
        elif A[1] == B[1]:
            return 'a'
        else:
            return 'b'
    else:
        return 'b'


def main():
    print('Welcome in the CoolMusic!')
    while True:
        choice = input('''Choose the action:
            1) Add new album
            2) Find albums by artist
            3) Find albums by year
            4) Find musician by album
            5) Find albums by letter(s)
            6) Find albums by genre
            7) Calculate the age of all albums
            8) Choose a random album by genre
            9) Show the amount of albums by an artist
            10) Find the longest-time album
            0) Exit\n''')

        if choice == '1':
            album = new_album()
            append_to_file(album)
        elif choice == '2':
            album_list = load_from_file()
            looking_artist = input('Artist name : ')
            album_list = find_by_artist(album_list, looking_artist)
            for album in album_list:
                print(" Album: " + album[0][1], " Artist: " + album[0][0])
        elif choice == '3':
            album_list = load_from_file()
            album_list = find_by_year(album_list, input('Year : '))
            for album in album_list:
                print(" Album: " + album[0][1], " Artist: " + album[0][0])
        elif choice == '4':
            album_list = load_from_file()
            artist = find_artist_by_album(album_list, input('Album name : '))
            print('Artist: ' + artist)
        elif choice == '5':
            album_list = load_from_file()
            album_list = find_by_letters(album_list, input('Leading album name letters : '))
            for album in album_list:
                print(" Album: " + album[0][1], " Artist: " + album[0][0])
        elif choice == '6':
            album_list = load_from_file()
            album_list = find_by_genre(album_list, input('Genre : '))
            for album in album_list:
                print(" Album: " + album[0][1], " Artist: " + album[0][0])
        elif choice == '7':
            album_list = load_from_file()
            calculate_age_all_albums(album_list)
        elif choice == '8':
            album_list = load_from_file()
            choose_random_album_by_genre(album_list, input('Put genre:'))
        elif choice == '9':
            album_list = load_from_file()
            album_list = find_by_artist(album_list, input('Artist: '))
            print(len(album_list))
        elif choice == '10':
            album_list = load_from_file()
            album = longest_time_album(album_list)
            print(" Album: " + album[0][1], " Artist: " + album[0][0])
        elif choice == '0':
            exit()
        else:
            print('Invalid choice!')

main()


