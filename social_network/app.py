from lib.database_connection import DatabaseConnection
from lib.account_repository import *
from lib.post_repository import *


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/social_network.sql")

account_repo = AccountRepository(connection)
post_repo = PostRepository(connection)

accounts = account_repo.all()
posts = post_repo.all()

for account in accounts:
    print(account)

for post in posts:
    print(post)

account_repo.delete(3)

accounts = account_repo.all()
posts = post_repo.all()

for account in accounts:
    print(account)

for post in posts:
    print(post)