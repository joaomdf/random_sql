from lib.post_repository import *

"""
Test all() returns all the posts
"""
def test_post_all(db_connection):
    db_connection.seed('seeds/social_network.sql')
    post_repository = PostRepository(db_connection)
    assert post_repository.all() == [
        Post(1, 'My title', 'My content', 45, 1),
        Post(2, 'My title 2: Electric Boogaloo', 'Sequel shit', 2000, 1),
        Post(3, 'Your title', 'Your content', 2, 2),
        Post(4, 'Your title 2: Electric Boogaloo', 'Sequel shit plagiarism', 35, 2),
        Post(5, 'Megalomaniac title', 'I am great and all that', 5000, 3)
    ]

"""
Test we are returned a specific post record when using find(post_id)
"""
def test_post_find(db_connection):
    db_connection.seed('seeds/social_network.sql')
    post_repository = PostRepository(db_connection)
    assert post_repository.find(1) == Post(1, 'My title', 'My content', 45, 1)
    assert post_repository.find(4) == Post(4, 'Your title 2: Electric Boogaloo', 'Sequel shit plagiarism', 35, 2)

"""
Test that when we create a new post record using create() with all the arguments needed from Post class
it is added to the total list and is also returned when we call all()
"""
def test_post_create(db_connection):
    db_connection.seed('seeds/social_network.sql')
    post_repository = PostRepository(db_connection)
    post_repository.create(Post(None,'Fresh post', 'Fresh content of post', 1, 2))
    assert post_repository.all() == [
        Post(1, 'My title', 'My content', 45, 1),
        Post(2, 'My title 2: Electric Boogaloo', 'Sequel shit', 2000, 1),
        Post(3, 'Your title', 'Your content', 2, 2),
        Post(4, 'Your title 2: Electric Boogaloo', 'Sequel shit plagiarism', 35, 2),
        Post(5, 'Megalomaniac title', 'I am great and all that', 5000, 3),
        Post(6,'Fresh post', 'Fresh content of post', 1, 2)
    ]
"""
Test when we delete a post record using delete(post_id) the post is deleted from the database
and when all() is called it returns a list without the deleted record
"""
def test_post_delete(db_connection):
    db_connection.seed('seeds/social_network.sql')
    post_repository = PostRepository(db_connection)
    post_repository.delete(5)
    assert post_repository.all() == [
        Post(1, 'My title', 'My content', 45, 1),
        Post(2, 'My title 2: Electric Boogaloo', 'Sequel shit', 2000, 1),
        Post(3, 'Your title', 'Your content', 2, 2),
        Post(4, 'Your title 2: Electric Boogaloo', 'Sequel shit plagiarism', 35, 2)
    ]
