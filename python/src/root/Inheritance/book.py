'''
Created on 16 Apr 2018

@author: s258115
'''
class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages
        
class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        Book.__init__(self, title, publisher, pages) # call the init method of book
        # or super().__init__(title, publisher, pages)
        # super is a function that returns a proxy object that delegates method calls to a parent or sibling class. In this case, it will delegate that call to __init__ to the Book class,
        self.format_ = format_


ebook = Ebook('Learning Python', 'Packt Publishing', 360, 'PDF')
print(ebook.title) # Learning Python
print(ebook.publisher) # Packt Publishing
print(ebook.pages) # 360
print(ebook.format_) # PDF
   
   
# Note can have multiple inheritance     