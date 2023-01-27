from lib.comment import Comment

def test_comment_constructs():
    comment = Comment(1, 'Something about incels...', 'that_one_alpha_nonsense_guy', 1)
    assert comment.id == 1
    assert comment.content == "Something about incels..."
    assert comment.author == "that_one_alpha_nonsense_guy"
    assert comment.post_id == 1

def test_comment_formats_nicely():
    comment = Comment(1, 'Something about incels...', 'that_one_alpha_nonsense_guy', 1)
    assert str(comment) == "Comment(1, Something about incels..., that_one_alpha_nonsense_guy, 1)"

def test_comment_are_equal():
    comment1 = Comment(1, 'Something about incels...', 'that_one_alpha_nonsense_guy', 1)
    comment2 = Comment(1, 'Something about incels...', 'that_one_alpha_nonsense_guy', 1)
    assert comment1 == comment2