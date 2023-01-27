from lib.account import *

"""
Test account created with all properties
"""
def test_account_args():
    account = Account(1, 'email@email.com', 'funny_pun')
    assert account.id == 1
    assert account.email == 'email@email.com'
    assert account.username == 'funny_pun'

"""
Test two accounts with same properties are recognized as equal
"""
def test_account_eq():
    account1 = Account(1, 'email@email.com', 'funny_pun')
    account2 = Account(1, 'email@email.com', 'funny_pun')
    assert account1 == account2
"""
Test account properties can be returned in nicely formatted format
"""

def test_account_formatting():
    account = Account(1, 'email@email.com', 'funny_pun')
    assert str(account) == 'Account(1, email@email.com, funny_pun)'