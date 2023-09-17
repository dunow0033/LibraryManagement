class Library: 

    def __init__(self, listOfBooks, listOfUsers): 
        self._books = listOfBooks 
        self._users = listOfUsers 
        self._borrowedBooks = []

    def display_all_books(self): 
        print(f"\nCURRENT LIST OF ALL BOOKS: ") 
        for book in self._books: 
            print(" ♦-- " + book.get_title()) 
        print("\n") 

    def display_available_books(self): 
        print(f"\nCURRENT LIST OF ALL AVAILABLE BOOKS: ") 
        for book in self._books: 
            if book not in self._borrowedBooks:
                print(" ♦-- " + book.get_title()) 
        print("\n")    

    def add_book(self, book): 
        self._books.append(book) 

    def checkout_book(self, book):  
        self._borrowedBooks.append(book) 

    def return_book(self, book):  
        if book not in self._borrowedBooks:
            return
        self._borrowedBooks.remove(book)

    def get_borrowed_books(self):
        return self._borrowedBooks
    
    def get_books(self):
        return self._books
            
    def get_users(self):
        return self._users
    
    def add_user(self, user):
        self._users.append(user)