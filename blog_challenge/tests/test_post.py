from lib.post import Post

def test_post_constructs():
    post = Post(1, 'Top 10 anime betrayals', 'I only watched DB and Death Note. Ask a weeb.', None)
    assert post.id == 1
    assert post.title == 'Top 10 anime betrayals'
    assert post.content == 'I only watched DB and Death Note. Ask a weeb.'
    assert post.comments == []

def test_post_formats_nicely():
    post = Post(1, 'Top 10 anime betrayals', 'I only watched DB and Death Note. Ask a weeb.', None)
    assert str(post) == "Post(1, Top 10 anime betrayals, I only watched DB and Death Note. Ask a weeb., [])"

def test_post_are_equal():
    post1 = Post(1, 'Top 10 anime betrayals', 'I only watched DB and Death Note. Ask a weeb.', None)
    post2 = Post(1, 'Top 10 anime betrayals', 'I only watched DB and Death Note. Ask a weeb.', None)
    assert post1 == post2