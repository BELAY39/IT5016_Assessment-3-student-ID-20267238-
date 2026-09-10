

#Book class stores information about each book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available=True
#Display the book details and availablity
    def display(self):
        status="Available"if self.available else "Borrowed"
        print(self.title,"-", self.author,"-",status)

#member class stores member information and borrowed books      
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
#borrow a book if it is available
    def borrow_book(self,book):
        if book.available:
         book.available=False
        self.borrowed_books.append(book)
        print(self.name,"borrowed",book.title)
#return a borrowed book
    def return_book(self,book):
        if book in self.borrowed_books:
            book.available=True
        self.borrowed_books.remove(book)
        print(self.name,"returned",book.title) 

                    
#library class manages books and members

class Library:
    def __init__(self):
        self.books = []
        self.members = []

#add a book to the library
    def add_book(self, book):
        self.books.append(book)
#add a member to the library
    def add_member(self,member):
        self.members.append(member)
#display all books in the library      
    def display_books(self):
        print("Library Books:")
        for book in self.books:
            book.display()
       
#create two book objects
book1 = Book("Python basics","Mary Jones")

book2 = Book("Oop programming","John Smith")
#create a member object
member1 = Member("Alex")
#create a liabrary object
library = Library()
#add books and member to the liabrary
library.add_book(book1)
library.add_book(book2)
library.add_member(member1)
#display the books before borrowing
library.display_books()

#Alex borrows oop programing
member1.borrow_book(book2)
#display the books after returning
library.display_books()
#Alex returns oop programming
member1.return_book(book2)
#display the books after returning
library.display_books()
