from lib.post_repository import PostRepository
from lib.post import Post
from lib.comment import Comment

def test_find_with_comments(db_connection):
    db_connection.seed('seeds/blog_records.sql')
    repo = PostRepository(db_connection)
    assert repo.find_with_comments(1) == Post(1,'Top 10 anime betrayals', 'I only watched DB and Death Note. Ask a weeb.', [Comment(1, 'Something about incels...', 'that_one_alpha_nonsense_guy', 1),Comment(2, 'Something transphobic...', 'MadPetersonFan420', 1)])

