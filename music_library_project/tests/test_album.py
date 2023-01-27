from lib.album import *

"""
Album constructs with an id, title, release_year and artist_id
"""

def test_album_constructs():
    album = Album(1,"OK Computer",1997,1)
    assert album.id == 1
    assert album.title == "OK Computer"
    assert album.release_year == 1997
    assert album.artist_id == 1

"""
Album can format albums to strings nicely
"""

def test_album_formats_nicely():
    album = Album(1,"OK Computer",1997,1)
    assert str(album) == "Album(1, OK Computer, 1997, 1)"

"""
Album can compare two identical albums
And have them be equal
"""

def test_albums_are_equal():
    album1 = Album(1,"OK Computer",1997,1)
    album2 = Album(1,"OK Computer",1997,1)
    assert album1 == album2