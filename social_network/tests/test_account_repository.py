from lib.account_repository import *

"""
Test all() returns all the accounts
"""
def test_account_all(db_connection):
    db_connection.seed('seeds/social_network.sql')
    account_repository = AccountRepository(db_connection)
    assert account_repository.all() == [
        Account(1,'me@thingy','me'),
        Account(2,'you@whatchamacallit','you'),
        Account(3,'them@musknetworks','them')
    ]

"""
Test we are returned a specific account record when using find(account_id)
"""
def test_account_find(db_connection):
    db_connection.seed('seeds/social_network.sql')
    account_repository = AccountRepository(db_connection)
    assert account_repository.find(2) == Account(2,'you@whatchamacallit','you')
    assert account_repository.find(3) == Account(3,'them@musknetworks','them')

"""
Test that when we create a new account record using create() with all the arguments needed from Account class
it is added to the total list and is also returned when we call all()
"""
def test_account_create(db_connection):
    db_connection.seed('seeds/social_network.sql')
    account_repository = AccountRepository(db_connection)
    account_repository.create(Account(None,'new_email@fresh.com','fresh_username'))
    assert account_repository.all() == [
        Account(1,'me@thingy','me'),
        Account(2,'you@whatchamacallit','you'),
        Account(3,'them@musknetworks','them'),
        Account(4,'new_email@fresh.com', 'fresh_username')
    ]

"""
Test when we delete an account record using delete(account_id) the account is deleted from the database
and when all() is called it returns a list without the deleted record
"""

def test_account_delete(db_connection):
    db_connection.seed('seeds/social_network.sql')
    account_repository = AccountRepository(db_connection)
    account_repository.delete(3)
    assert account_repository.all() == [
        Account(1,'me@thingy','me'),
        Account(2,'you@whatchamacallit','you')
    ]