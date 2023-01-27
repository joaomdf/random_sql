Challenge 3

User story:
Building from what previously existed in the music library project I'd like to be able to:

create album records to add to my database in the albums table

delete album records from my albums table

----
Layout:

In AlbumRepository class

create() method - args - album (Album object with all its necessary arguments (id = None, title, release_year, artist_id))
    create method creates a new row to add to albums table in database
    no return
    uses placeholders in the SQL line for security reasons

delete() method - args - album_id
    delete method deletes an existing row from the albums table in the database by referencing the specific album_id of that row
    no return
    uses placeholders in the SQL line for security reasons

----
Tests

In existing test_album_repository.py file

"""
Given couple of new Album objects
when using the create() method to add these records to the album table in the database
are the new records also listed when the all() method is used to gather all the existing records
"""

"""
Given a couple of existing records in the albums table in the database 
When using the delete() method to delete these records from the table
is the all() method returnin an updated list of albums according to our deletions
"""