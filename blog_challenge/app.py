from lib.post_repository import PostRepository
from lib.database_connection import DatabaseConnection

class Application:
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/blog_records.sql")

    def run(self):
        repo = PostRepository(self._connection)
        found = repo.find_with_comments(1)
        print(f"Your post ID: {found.id}")
        print(f"Your post title: {found.title}")
        print(f"Your post content: {found.content}\n")
        print("Your post comments:")
        for comment in found.comments:
            print(f"ID: {comment.id}\nAuthor: {comment.author}\nContent: {comment.content}\n")


if __name__ == '__main__':
    app = Application()
    app.run()