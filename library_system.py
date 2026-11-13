from dataclasses import dataclass
import pandas as pd
from difflib import get_close_matches
@dataclass
class Book:
    title: str
    author: str
    amount: int = 1

#Users class to store user data
@dataclass
class Client:
    name: str
    username: str
    password: str
    email:  str
    phone_number: str

class Library:
    @staticmethod
    def add_user(data):
        users = pd.read_json('users.json')
        uid = int(users['uid'].iloc[-1]) 
        data = {'uid': uid+1, **data} # (| data) also correct if you python 3.9 or higher 
        data = pd.DataFrame([data])
        users = pd.concat([users,data], ignore_index=True)
        users.to_json('users.json', orient='records', indent=4)

    @staticmethod
    def add_book(book):
        books = pd.read_json('books.json')
        book = pd.DataFrame([book])
        #adding book_id
        book_id = int(books['book_id'].iloc[-1]) 
        book = {'book_id': book_id+1, **book} # (| data) also correct if you're using Python 3.9 or higher
        books = pd.concat([books,book], ignore_index=True)
        books.to_json('books.json', orient='records', indent=4)

    @staticmethod
    def search(book):
        book_shelf = pd.read_json('books.json')
        titles = book_shelf['title'].to_list()
        books_match = get_close_matches( # get closest titles from user input & titles we get
            book,
            titles,
            n=6,
            cutoff=.25
        ) 
        return books_match
    
    @staticmethod
    def borrow_book(search_result,uid):
        borrow_list = pd.read_json("borrowed_list.json")
        user = borrow_list[borrow_list['uid'] == uid]
        book_list = list(user['bid'])[0]
        # if user not found in database
        if len(book_list) == 0:
            new_order = {
                "uid": uid,
                "bid": []
            }
            new_order["bid"].append(search_result)
            new_order = pd.DataFrame([new_order])
            new_order = pd.concat([borrow_list, new_order], ignore_index=True)
        else:
            #checking if user has reached the limit of borrowed books
            if len(book_list) == 3:
                return "Sorry, you have reached the limit of borrowed books."
            else:
                book_list.append(search_result)
                user['bid'] = [book_list]
                borrow_list.update(user)
                return "nice to meet you"

    @staticmethod
    def return_book(uid, bid):
        borrow_list = pd.read_json("borrowed_list.json")
        user = borrow_list[borrow_list['uid'] == uid]
        book_list = list(user['bid'])[0]
        if len(book_list) == 0:
            return "you have no borrowed books"
        else:
            book_list.remove(bid)
            user['bid'] = [book_list]
            borrow_list.update(user)
            return "Book returned successfully"
