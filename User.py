import random
class User: 

    def __init__(self, name): 
        self._name = name 
        self._ID = random.randint(0, 500)
        self._borrowedBooks = []  

    def get_ID(self): 
        return self._ID 
    
    def get_name(self):
        return self._name 

    def borrow_book(self, book): 
        self._borrowedBooks.append(book) 
        book.availability = "Unavailable" 
        print(f"{self._name} has checked out {book.get_title()}.\n") 

    def return_book(self, book):
        if book not in self._borrowedBooks:
            print(f"You have not borrowed {book.get_title()}, so you cannot return this book")
            return
        self._borrowedBooks.remove(book) 
        book.availability = "Available" 
        print(f"Thank you {self._name}.  {book.get_title()} is now available!!\n")
        
    def get_borrowedBooks(self):
        return self._borrowedBooks