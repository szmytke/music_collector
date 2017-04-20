import csv
def new_album():
    name_art = input('write a name of artist\n')
    name_album = input('write a name of album\n')
    year = input('writa a year of release\n')
    genre = input('write a genre\n')
    length = input('write a length of album\n')
    music = [(name_art,name_album),(year,genre,length)]
    return music

def append_to_file(album_to_write):
    filecsv = open('music2.csv','a')
    to_write = ""
    for x in range(len(album_to_write)):
        for y in range(len(album_to_write[x])):
            to_write += album_to_write[x][y]
            if not (x==(len(album_to_write)-1) and y==(len(album_to_write[x])-1)):
                to_write += " | "
    print(to_write)
    filecsv.write(to_write + '\n')


def load_from_file():
    filecsv = open('music2.csv','r')
    reader = csv.reader(filecsv)
    
    name_art = ""
    name_album = ""
    year = ""
    genre = ""
    length = ""
    albums_list = []
    for row in reader:
        print(row)        
        splitted = str(row).split(' | ')
        name_art = splitted[0].replace('[\'', "").replace('\']', "")
        name_album = splitted[1].replace('[\'', "").replace('\']', "")
        year = splitted[2].replace('[\'', "").replace('\']', "")
        genre = splitted[3].replace('[\'', "").replace('\']', "")
        length = splitted[4].replace('[\'', "").replace('\']', "")

        album = ((name_art,name_album),(year,genre,length))
        albums_list.append(album)

    return albums_list

def find_by_artist(album_list, artist):
    return_albums = []
    for album in album_list:
        if tuple(album)[0][0] == artist:
            return_albums.append(tuple(album))
            print (album)
    return return_albums

def find_by_year(album_list, year):
    return_albums = []
    for album in album_list:
        if tuple(album)[1][0] == year:
            return_albums.append(tuple(album))
            print (album)
    return return_albums

def find_artist_by_album(album_list, album_name):
    return_artist = ""
    for album in album_list:
        if tuple(album)[0][1] == album_name:
            return_artist = tuple(album)[0][0]
            print (tuple(album)[0][0])
    return return_artist

def find_by_genre(album_list, genre):
    return_albums = []
    for album in album_list:
        if tuple(album)[1][1] == genre:
            return_albums.append(tuple(album))
            print (album)
    return return_albums

def find_by_letters(album_list, letters):
    return_albums = []
    for album in album_list:
        if tuple(album)[0][1].lower().startswith(str(letters).lower()):
            return_albums.append(tuple(album))
            print (album)
    return return_albums


choice = input('''Welcome in the CoolMusic! Choose the action:
         1) Add new album
         2) Find albums by artist
         3) Find albums by year
         4) Find musician by album
         5) Find albums by genre
         6) Find albums by letter(s)
         0) Exit\n''')
#music = []
if choice == '1':  
    album = new_album()
    append_to_file(album)
if choice == '2':
    album_list = load_from_file()
    find_by_artist(album_list, input('Artist name : '))
if choice == '3':
    album_list = load_from_file()
    find_by_year(album_list, input('Year : '))
if choice == '4':
    album_list = load_from_file()
    find_artist_by_album(album_list, input('Album name : '))
if choice == '5':
    album_list = load_from_file()
    find_by_genre(album_list, input('Genre : '))
if choice == '6':
    album_list = load_from_file()
    find_by_letters(album_list, input('Leading album name letters : '))


