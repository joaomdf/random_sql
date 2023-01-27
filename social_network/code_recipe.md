As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.

----

class Account:
    Used to instanciate Account objects for the user with the args bellow
    __init__ - args - id, email, username - instanciates account with all its data

    __eq__ - args - other - compares if two accounts with same info are the same

    __repr__ - no args - formats the account args into something readable

class AccountRepository:
    Used to create repository of accounts with ability to return list of all acounts, find specific account, delete account and create account
    __init__ - args - connection - connects to accounts database

    all() - no args - returns list of accounts

    find() - args - account_id - returns specific account

    create() - args - id, email, username (same as for Account class. id=None as it should default) - creates account

    delete() - args - account_id - deletes specific account

----
Tests:

Class Account
"""
Test account created with all properties
"""

"""
Test two accounts with same properties are recognized as equal
"""

"""
Test account properties can be returned in nicely formatted format
"""

Class AccountRepository
"""
Test all() returns all the accounts
"""

"""
Test we are returned a specific account record when using find(account_id)
"""

"""
Test that when we create a new account record using create() with all the arguments needed from Account class
it is added to the total list and is also returned when we call all()
"""

"""
Test when we delete an account record using delete(account_id) the account is deleted from the database
and when all() is called it returns a list without the deleted record
"""

----

class Post:
    Used to instanciate Account objects for the user with the args bellow
    __init__ - args - id, title, content, views, account_id - instanciates account with all its data

    __eq__ - args - other - compares if two posts with same info are the same

    __repr__ - no args - formats the post args into something readable

class PostRepository:
    Used to create repository of posts with ability to return list of all posts, find specific post, delete post and create post
    __init__ - args - connection - connects to posts database

    all() - no args - returns list of posts

    find() - args - post_id - returns specific post

    create() - args - id, title, content, views, account_id (same as for Post class. id=None as it should default) - creates post

    delete() - args - post_id - deletes specific post from database

----
Tests:

Class Post
"""
Test post created with all properties
"""

"""
Test two posts with same properties are recognized as equal
"""

"""
Test post properties can be returned in nicely formatted format
"""

Class PostRepository
"""
Test all() returns all the posts
"""

"""
Test we are returned a specific post record when using find(post_id)
"""

"""
Test that when we create a new post record using create() with all the arguments needed from Post class
it is added to the total list and is also returned when we call all()
"""

"""
Test when we delete a post record using delete(post_id) the post is deleted from the database
and when all() is called it returns a list without the deleted record
"""

