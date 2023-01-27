from lib.post import *

"""
Test post created with all properties
"""
def test_post_args():
    post = Post(1, 'Scream into the void', 'This is my void scream', 30, 2)
    assert post.id == 1
    assert post.title == 'Scream into the void'
    assert post.content == 'This is my void scream'
    assert post.views == 30
    assert post.account_id == 2

"""
Test two posts with same properties are recognized as equal
"""
def test_post_eq():
    post1 = Post(1, 'Scream into the void', 'This is my void scream', 30, 2)
    post2 = Post(1, 'Scream into the void', 'This is my void scream', 30, 2)
    assert post1 == post2

"""
Test post properties can be returned in nicely formatted format
"""
def test_post_formatting():
    post = Post(1, 'Scream into the void', 'This is my void scream', 30, 2)
    assert str(post) == 'Post(1, Scream into the void, This is my void scream, 30, 2)'