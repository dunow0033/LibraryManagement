class Book: 
    def __init__(self, title, author): 
        self._title = title 
        self._author = author 
        self._availability = "Available" 
        
    def get_title(self):
        return self._title
    
    def get_availability(self):
        return self._availability
    
    def set_availability(self, status):
        self._availability = status

    def display_info(self): 
        print("Title: " + self._title + "\n") 
        print("Author: " + self._author + "\n")
        print("Availability: " + self._availability + "\n")