from lib.album import *
from lib.album_repository import *

"""
When we call AlbumRepository.all()
We get a list of all Album objects reflecting the seed data
"""

def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    albums = repository.all()

    assert albums == [
        Album(1, "Doolittle", 1989, 1),
        Album(2,"Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, "Bossanova", 1990, 1),
        Album(6, "Lover", 2019, 3),
        Album(7, "Folklore", 2020, 3),
        Album(8, "I Put a Spell on You", 1965, 4),
        Album(9, "Baltimore", 1978, 4),
        Album(10, "Here Comes the Sun", 1971, 4),
        Album(11, "Fodder on My Wings", 1982, 4),
        Album(12, "Ring Ring", 1973, 2)
    ]

"""
When we run find() on AlbumRepository we
get the right record back
"""

def test_find_record_one(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    assert repository.find(1) == Album(1, "Doolittle", 1989, 1)

"""
Given couple of new Album objects
when using the create() method to add these records to the album table in the database
are the new records also listed when the all() method is used to gather all the existing records
"""
def test_create_album_records(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repository = AlbumRepository(db_connection)
    repository.create(Album(None, "In Rainbows", 2007, 5))
    assert repository.all() == [
        Album(1, "Doolittle", 1989, 1),
        Album(2,"Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, "Bossanova", 1990, 1),
        Album(6, "Lover", 2019, 3),
        Album(7, "Folklore", 2020, 3),
        Album(8, "I Put a Spell on You", 1965, 4),
        Album(9, "Baltimore", 1978, 4),
        Album(10, "Here Comes the Sun", 1971, 4),
        Album(11, "Fodder on My Wings", 1982, 4),
        Album(12, "Ring Ring", 1973, 2),
        Album(13, "In Rainbows", 2007, 5)
    ]
    repository.create(Album(None, "OK Computer", 1999, 5))
    assert repository.all() == [
        Album(1, "Doolittle", 1989, 1),
        Album(2,"Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, "Bossanova", 1990, 1),
        Album(6, "Lover", 2019, 3),
        Album(7, "Folklore", 2020, 3),
        Album(8, "I Put a Spell on You", 1965, 4),
        Album(9, "Baltimore", 1978, 4),
        Album(10, "Here Comes the Sun", 1971, 4),
        Album(11, "Fodder on My Wings", 1982, 4),
        Album(12, "Ring Ring", 1973, 2),
        Album(13, "In Rainbows", 2007, 5),
        Album(14, "OK Computer", 1999, 5)
    ]

"""
Given a couple of existing records in the albums table in the database 
When using the delete() method to delete these records from the table
is the all() method returnin an updated list of albums according to our deletions
"""
def test_delete_albums(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repository = AlbumRepository(db_connection)
    repository.delete(6)
    assert repository.all() == [
        Album(1, "Doolittle", 1989, 1),
        Album(2,"Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, "Bossanova", 1990, 1),
        Album(7, "Folklore", 2020, 3),
        Album(8, "I Put a Spell on You", 1965, 4),
        Album(9, "Baltimore", 1978, 4),
        Album(10, "Here Comes the Sun", 1971, 4),
        Album(11, "Fodder on My Wings", 1982, 4),
        Album(12, "Ring Ring", 1973, 2)
    ]
    repository.delete(3)
    assert repository.all() == [
        Album(1, "Doolittle", 1989, 1),
        Album(2,"Surfer Rosa", 1988, 1),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, "Bossanova", 1990, 1),
        Album(7, "Folklore", 2020, 3),
        Album(8, "I Put a Spell on You", 1965, 4),
        Album(9, "Baltimore", 1978, 4),
        Album(10, "Here Comes the Sun", 1971, 4),
        Album(11, "Fodder on My Wings", 1982, 4),
        Album(12, "Ring Ring", 1973, 2)
    ]
