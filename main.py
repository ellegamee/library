from getpass import getpass
import os
import time
import pickle
import inspect

class Book:
    def __init__(self, data):
        self.auther = data[0]
        self.name = data[1]
        self.genre = data[2]
        self.realese = data[3]
        self.shelf = data[4]
        self.in_stock = data[6]
        self.id = data[5]
    
    def remove_stock(self):
        if self.in_stock != 0:
            self.in_stock -= 1
    
    def return_information(self):
        information = []
        
        information.append(self.auther)
        information.append(self.name)
        information.append(self.genre)
        information.append(self.realese)
        information.append(self.shelf)
        information.append(self.id)
        information.append(self.in_stock)
        
        return information
    
class User:
    def __init__(self, data):
        self.first_name = data[0]
        self.second_name = data[1]
        self.personal_number = data[2]
        self.books_lended = []
        
    def lend_book(self):
        pass

    def remove_lend_book():
        pass
    
    def print_lend_books():
        pass
    
    def user_information():
        pass

library = []
users = []
def wrongOption():
    print('Not an option, try again!')
    time.sleep(1.5)

def searchLibrary():
    searchTerm = input('Search term: ')
    
    count = 0
    for book in library:
        if book.name == searchTerm:
            print(f'{book.return_information()}\n')
            count += 1
    
    if count < 1:
        print('No books found')

def loadBooks():
    if os.path.getsize("library.pkl") != 0:
        dbfile = open('library.pkl', 'rb')
        content = pickle.load(dbfile)
        dbfile.close()
        
        return content
        
def saveBooks():
    dbfile = open('library.pkl', 'wb')
    pickle.dump(library, dbfile)
    dbfile.close()
    
def loadUsers():
    if os.path.getsize("users.pkl") != 0:
        dbfile = open('users.pkl', 'rb')
        content = pickle.load(dbfile)
        dbfile.close()
        
        return content

def saveUsers():
    dbfile = open('users.pkl', 'wb')
    pickle.dump(users, dbfile)
    dbfile.close()

users = loadUsers()
library = loadBooks()
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\t\tLogin Page\t\t')
    print('1. Student')
    print('2. Admin')
    print('3. Exit')
    loginChoice = input('\nWhat option: ')
    
    if loginChoice == '1':
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\t\tLibrary System (Student)\t\t')
            print('1. All books')
            print('2. Go back')
            
            studentChoice = input('\nWhat option: ')
            os.system('cls' if os.name == 'nt' else 'clear')
            
            if studentChoice == '1':
                if library == []:
                    print('Sorry! No books in the library system.')
                    input('\nPress Enter to Continue...')

                else:
                    for book in library:
                        data = book.return_information()
                        print(f'\t{data[1]}')
                        print(f'Auther: {data[0]}\t Year: {data[3]}')
                        print(f'Genre: {data[2]}\t Shelf: {data[4]}')
                        print(f'Stock: {data[6]}\n')
                    
                    input('Press Enter to Continue...')

            elif studentChoice == '2':
                break
            
            else:
                wrongOption()
            
    elif loginChoice == '2':
        adminPassword = getpass()
        
        if adminPassword == 'admin':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\t\tLibrary System (Admin)\t\t')
                print('1. Add book to system')
                print('2. Logout')
                
                adminChoice = input('\nWhat option: ')
                os.system('cls' if os.name == 'nt' else 'clear')
                
                if adminChoice == '1':
                    auther = input('Auther: ')
                    name = input('Name: ')
                    genre = input('Genre: ')
                    realese = input('Realese year: ')
                    shelf = input('Shelf: ')
                    bookID = len(library) + 1
                    stock = 1
                    
                    data = [auther, name, genre, realese, shelf, bookID, stock]
                    
                    library.append(Book(data))
                    saveBooks()
                
                elif adminChoice == '2':
                    print('You logged out...')
                    time.sleep(1.5)
                    break
                
                else:
                    wrongOption()
    
    elif loginChoice == '3':
        saveBooks()
        break
    
    else:
        wrongOption()