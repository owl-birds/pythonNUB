class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return "books title {} by author {}".format(self.title,self.author)
    def __len__(self):
        return self.pages
    def __del__(self):
        print("A book object has been deleted")
book1 = Book("book1", "author 1", 90)
print(book1)
print(len(book1))
# deleteing var
del book1
print(book1)