from library_management import inventory

class User_Inputs():
    def __init__(self, library_management):
        self.library_management = library_management
        
    def greeting(self):
        print("Bolduc Correctional Facility")
        print("Library Management systems")
        
    def add_book(self):
        while True:
            #Get the current list of books
            books = self.library_management.get_books()
            
            if not books:
                print("No books added.")
                print("Would you like to add a book?")
                choice = input("y/n: ")
                match choice:
                    case 'y':
                        option = input("ISBN or DDS")
                        try:
                            if option == "ISBN":
                                ISBN = int(input("Enter ISBN: "))
                                AUTH_LAST = input("Enter Author Last Name: ")
                                AUTH_FIRST = input("Enter Author First Name ")
                                TITLE = input("Enter Title")
                                CLASS = input("Enter Classification")
                                LOCATION = input('Enter designated location')
                                if ISBN in self.library_management.get_books():
                                    choice = input("Book already in the system. Would you like to add to QTY?y/n: ")
                                    if choice == 'y':
                                        print("Verify that the following information is correct:")
                                        print(f"ISBN: {ISBN}\n Last Name: {AUTH_LAST}\n First Name: {AUTH_FIRST}\n Title: {TITLE}\n Classification: {CLASS}\n Location: {LOCATION}")
                                        choice = input("Is the information correct?y/n: ")
                                        if choice == 'y':
                                            break
                                        elif choice == 'n':
                                            print("Please choose the option you wish to update: ")
                                        # self.library_management.add_book(ISBN, AUTH_LAST, AUTH_FIRST, TITLE, CLASS)
                                        # print(f"Book {ISBN}/{TITLE} by {AUTH_FIRST} {AUTH_LAST} added successfully")
                                    else:
                                        break
                                elif not self.library_management.get_books():
                                    pass
                                    
                            elif option == "DDS":
                                DDSN = int(input("Enter DDSN: "))
                                AUTH_LAST = input("Enter Author Last Name: ")
                                AUTH_FIRST = input("Enter Author First Name ")
                                TITLE = input("Enter Title")
                                CLASS = input("Enter Classification")
                        except ValueError:
                            print("Invalid input")
                            
                    case 'n':
                        pass
                    case _:
                        print("Invalid Input")    
                    
                        
            
        