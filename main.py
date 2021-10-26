import os
import pickle
import inspect

class Book:
    def __init__(self):
        self.auther = None
        self.name = None
        self.genre = None
        self.realese = None
        self.recomendated = None
        self.shelf = None
        self.id = None
    
    def lend_book(self):
        pass
    
    def remove_book(self):
        pass
    
    def return_information(self):
        information = []
        
        information.append(self.auther)
        information.append(self.name)
        information.append(self.genre)
        information.append(self.realese)
        information.append(self.recomendated)
        information.append(self.shelf)
        information.append(self.id)
        
        return information
    
class User:
    def __init__(self):
        self.first_name = None
        self.second_name = None
        self.personal_number = None
        self.books_lended = []
        
    def remove_lend_book():
        pass
    
    def print_lend_books():
        pass
    
    def user_information():
        pass
    
hej = Book()
lst = hej.return_information(hej)
print(lst)