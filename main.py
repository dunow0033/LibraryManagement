from Book import Book
from Library import Library
from Student import Student
from User import User

def register_new_user(lib): 
    print("OK, great, you want to register as a new user.  Are you a student or regular user?\n") 
    print("------------------------------") 
    print("1. Student") 
    print("2. Regular User") 
    choice = input("Enter your choice:  ") 

    if choice == "1": 
        print("Ok, you are a student.  Students can check out up to 6 books at a time.\n") 
        print("What's your name?\n") 
        name = input("") 
        print("What school do you go to?\n") 
        school = input("") 
        print("What grade are you in?\n") 
        grade = input("") 
        student = Student(name, grade, school) 
        lib.add_user(student) 
        return student 

    elif choice == "2": 
        print("Ok, you are a regular user.  Regular users can check out up to 3 books at a time.\n") 
        name = input("What's your name?  ") 
        user = User(name) 
        lib.add_user(user) 
        return user 

def main_menu(lib, ID, book_list):
    for i in lib.get_users():
        if i.get_ID() == ID:
            user = i
            break

    print(f"Welcome {user.get_name()}, what would you like to do today?\n")
    while True:
        print("------------------------------")
        print("1. View current list of books")
        print("2. View a book's information")
        print("3. Checkout a book")
        print("4. Return a book")
        print("5. Donate a book")
        print("6. Logout")

        choice = input("Enter your choice:  ")

        if choice == "1":
            lib.display_books()

        elif choice == "2":
            print("Ok, great, what book would you like more information on?\n")
            book_name = input("")
            book = None
                        
            for available_book in book_list:
                if available_book.get_title() == book_name:
                    book = available_book
                    break
                        
                if book:
                    print("Great, here you go: \n")
                    book.display_info()
                else:
                    print("No book exists with the given name \n")

        elif choice == "3":
            if isinstance(user, Student):
                if len(user.get_borrowedBooks()) >= 6:
                    print("Sorry, students can only check out up to 6 books at a time. Please return 1 book before you check out another.")
                    continue
                            
                elif isinstance(user, User):
                    if len(user.get_borrowedBooks()) >= 3:
                        print("Sorry, regular users can only check out up to 3 books at a time. Please return 1 book before you check out another.")
                        continue

                print("Ok, great, what book would you like to check out?\n")
                book_name = input("")
                book = None
                        
                for available_book in book_list:
                    if available_book.get_title() == book_name:
                        book = available_book
                        break
                        
                    if book:
                        user.borrow_book(book)
                        lib.checkout_book(book)
                    else:
                        print(f"Sorry, we don't currently have that book in our inventory. \n")

        elif choice == "4":
            print("Ok, great, what book would you like to return?\n")
            book_name = input("")
            book = None
                        
            for available_book in book_list:
                if available_book.get_title() == book_name:
                    book = available_book
                    break
                        
                if book:
                    user.return_book(book)
                    lib.return_book(book)
                else:
                    print("Sorry, we don't currently have that book in our inventory!!  Perhaps it's from a different library?\n")

        elif choice == "5":
            print("Ok, great, what is the title of the book you would like to donate?\n")
            title = input("")
            print("And the author?\n")
            author = input("")
            book = Book(title, author)
            lib.add_book(book)

        elif choice == "6":
            break 

def main():
    book_list = [
        Book("python", "Alex"),
        Book("advance cpp", "Ryan"),
        Book("dsa", "John Doe"),
        Book("java", "Jane Smith"),
        Book("the great gatsby", "Robert Johnson"),
        Book("to kill a mockingbird", "Emily Davis"),
        Book("complete history of the world", "Michael Anderson"),
        Book("the da vinci code", "Sarah Thompson"),
        Book("the count of monte cristo", "David Wilson"),
        Book("how to win friends and influence people", "Laura Brown"),
        Book("the catcher in the rye", "Daniel Taylor"),
        Book("a tale of two cities", "Sophia Martinez")
    ]

    names = []
    IDin = False
    user = ""

    lib = Library(book_list, names)
    running = True
    while running:
        print("------------------------------")
        print("Welcome to Eastbrook library")
        print("------------------------------")
        print("1. Login")
        print("2. Register As New User")
        print("3. Quit")
        choice = input("Enter your choice:  ")

        if choice == "1":
            ID = int(input("Ok, please enter your ID:  "))
            for i in lib.get_users():
                if i.get_ID() == ID:
                    IDin = True
                    user = i
                    break

            if IDin:
                main_menu(lib, ID, book_list)
                # print(f"Welcome {user.get_name()}, what would you like to do today?\n")
                # while True:
                #     print("------------------------------")
                #     print("1. View current list of books")
                #     print("2. View a book's information")
                #     print("3. Checkout a book")
                #     print("4. Return a book")
                #     print("5. Donate a book")
                #     print("6. Logout")

                #     choice = input("Enter your choice:  ")

                #     if choice == "1":
                #         lib.display_books()

                #     elif choice == "2":
                #         print("Ok, great, what book would you like more information on?\n")
                #         book_name = input("")
                #         book = None
                        
                #         for available_book in book_list:
                #             if available_book.get_title() == book_name:
                #                 book = available_book
                #                 break
                        
                #         if book:
                #             print("Great, here you go: \n")
                #             book.display_info()
                #         else:
                #             print("No book exists with the given name \n")

                #     elif choice == "3":
                        
                #         if isinstance(user, Student):
                #             if len(user.get_borrowedBooks()) >= 6:
                #                 print("Sorry, students can only check out up to 6 books at a time. Please return 1 book before you check out another.")
                #                 continue
                            
                #         elif isinstance(user, User):
                #             if len(user.get_borrowedBooks()) >= 3:
                #                 print("Sorry, regular users can only check out up to 3 books at a time. Please return 1 book before you check out another.")
                #                 continue

                #         print("Ok, great, what book would you like to check out?\n")
                #         book_name = input("")
                #         book = None
                        
                #         for available_book in book_list:
                #             if available_book.get_title() == book_name:
                #                 book = available_book
                #                 break
                        
                #         if book:
                #             user.borrow_book(book)
                #             lib.checkout_book(book)
                #         else:
                #             print(f"Sorry, we don't currently have that book in our inventory. \n")

                #     elif choice == "4":
                #         print("Ok, great, what book would you like to return?\n")
                #         book_name = input("")
                #         book = None
                        
                #         for available_book in book_list:
                #             if available_book.get_title() == book_name:
                #                 book = available_book
                #                 break
                        
                #         if book:
                #             user.return_book(book)
                #             lib.return_book(book)
                #         else:
                #             print("Sorry, we don't currently have that book in our inventory!!  Perhaps it's from a different library?\n")

                #     elif choice == "5":
                #         print("Ok, great, what is the title of the book you would like to donate?\n")
                #         title = input("")
                #         print("And the author?\n")
                #         author = input("")
                #         book = Book(title, author)
                #         lib.add_book(book)

                #     elif choice == "6":
                #         break

            else:
                print("Sorry, that user ID was not found in our system. You can register as a new user or exit.\n")
                print("------------------------------")
                print("1. Register As New User")
                print("2. Exit")
                print()
                choice = input("Please enter your choice:  ")

                if choice == "1":
                    new_user = register_new_user(lib)
                    ID = new_user.get_ID()
                    print(f"Thank you. Here is your ID: {ID}.")
                    main_menu(lib, ID, book_list)
                    #continue

                else:
                    print("Thank you. Bye-bye.")
                    break

        elif choice == "2":
            new_user = register_new_user(lib)
            ID = new_user.get_ID()
            print(f"Thank you. Here is your ID: {ID}.")
            main_menu(lib, ID, book_list)
            #continue
            # for i in lib.get_users():
            #     if i.get_ID() == ID:
            #         user = i
            #         break
            # print(f"Welcome {user.get_name()}, what would you like to do today?\n")
            # while True:
            #         print("------------------------------")
            #         print("1. View current list of books")
            #         print("2. View a book's information")
            #         print("3. Checkout a book")
            #         print("4. Return a book")
            #         print("5. Donate a book")
            #         print("6. Logout")

            #         choice = input("Enter your choice:  ")

            #         if choice == "1":
            #             lib.display_books()

            #         elif choice == "2":
            #             print("Ok, great, what book would you like more information on?\n")
            #             book_name = input("")
            #             book = None
                        
            #             for available_book in book_list:
            #                 if available_book.get_title() == book_name:
            #                     book = available_book
            #                     break
                        
            #             if book:
            #                 print("Great, here you go: \n")
            #                 book.display_info()
            #             else:
            #                 print("No book exists with the given name \n")

            #         elif choice == "3":
                        
            #             if isinstance(user, Student):
            #                 if len(user.get_borrowedBooks()) >= 6:
            #                     print("Sorry, students can only check out up to 6 books at a time. Please return 1 book before you check out another.")
            #                     continue
                            
            #             elif isinstance(user, User):
            #                 if len(user.get_borrowedBooks()) >= 3:
            #                     print("Sorry, regular users can only check out up to 3 books at a time. Please return 1 book before you check out another.")
            #                     continue

            #             print("Ok, great, what book would you like to check out?\n")
            #             book_name = input("")
            #             book = None
                        
            #             for available_book in book_list:
            #                 if available_book.get_title() == book_name:
            #                     book = available_book
            #                     break
                        
            #             if book:
            #                 user.borrow_book(book)
            #                 lib.checkout_book(book)
            #             else:
            #                 print(f"Sorry, we don't currently have that book in our inventory. \n")

            #         elif choice == "4":
            #             print("Ok, great, what book would you like to return?\n")
            #             book_name = input("")
            #             book = None
                        
            #             for available_book in book_list:
            #                 if available_book.get_title() == book_name:
            #                     book = available_book
            #                     break
                        
            #             if book:
            #                 user.return_book(book)
            #                 lib.return_book(book)
            #             else:
            #                 print("Sorry, we don't currently have that book in our inventory!!  Perhaps it's from a different library?\n")

            #         elif choice == "5":
            #             print("Ok, great, what is the title of the book you would like to donate?\n")
            #             title = input("")
            #             print("And the author?\n")
            #             author = input("")
            #             book = Book(title, author)
            #             lib.add_book(book)

            #         elif choice == "6":
            #             break

        elif choice == "3":
            break

        else:
            print("Invalid selection, please try again!!!\n")
            continue

    print("Thank you!!!  Bye-bye!!")


if __name__ == "__main__":
    main()