'''
Welcome Adriano de Pinho Tavares from Using Databases with Python

To get credit for this assignment, perform the instructions below and upload your SQLite3 database here:
(Must have a .sqlite suffix)

You do not need to export or convert the database - simply upload the .sqlite file that your program creates. 
See the example code for the use of the connect() statement.

Musical Track Database
This application will read an iTunes export file in CSV format and produce a properly normalized database with this structure:

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/tracks.zip. 
The ZIP file contains the tracks.csv file to be used for this assignment. You can export your own tracks from iTunes and create
a database, but for the database that you turn in for this assignment, only use the tracks.csv data that is provided. 
You can adapt the tracks_csv.py application in the zip file to complete the assignment.

To grade this assignment, the program will run a query like this on your uploaded database and look for the data it expects to see:

SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
    
The expected result of the modified query on your database is: (shown here as a simple HTML table with titles)

Track	                                    Artist	    Album	            Genre
Chase the Ace	                            AC/DC	    Who Made Who	    Rock
D.T.	                                    AC/DC	    Who Made Who	    Rock
For Those About To Rock (We Salute You)	    AC/DC	    Who Made Who	    Rock

'''
import sqlite3

conn = sqlite3.connect('./db/tracksdb.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

handle = open('tracks.csv')

# Another One Bites The Dust,Queen,Greatest Hits,55,100,217103
#   0                          1      2           3  4   5

'''
Another One Bites The Dust,Queen,Greatest Hits,55,100,217103,Rock
Asche Zu Asche,Rammstein,Herzeleid,79,100,231810,Industrial
Beauty School Dropout,Various,Grease,48,100,239960,Soundtrack
'''


for line in handle:
    line = line.strip();
    pieces = line.split(',')
    if len(pieces) < 6 : continue

    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6]

    print(name, artist, album, count, rating, length, genre)

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id, length, rating, count ) )

    conn.commit()
