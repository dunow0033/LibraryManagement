class Library: 

    def __init__(self, listOfBooks, listOfUsers): 
        self._books = listOfBooks 
        self._users = listOfUsers 
        self._borrowedBooks = []

    def display_books(self): 
        print(f"\n{len(self._books)} CURRENT LIST OF BOOKS ARE: ") 
        for book in self._books: 
            if book not in self._borrowedBooks:
                print(" ♦-- " + book.get_title()) 
        print("\n") 

    def add_book(self, book): 
        self._books.append(book) 

    def checkout_book(self, book): 
        # if book not in self._books: 
        #     print(f"Eastbrook library doesn't currently have {book.get_title()} in it's inventory.  Sorry.\n") 
        if book in self._borrowedBooks: 
            print(f"{book.get_title()} is currently being borrowed by someone else.  Sorry.\n") 
        else: 
            self._borrowedBooks.append(book) 

    def return_book(self, book): 
        # if book not in self._books: 
        #     print(f"Eastbrook library doesn't currently have {book.get_title()} in it's inventory.\n  Try returning it to a different library.\n") 
        # else: 
        if book not in self._borrowedBooks:
            return
        self._borrowedBooks.remove(book) 
            
    def get_users(self):
        return self._users
    
    def add_user(self, user):
        self._users.append(user)