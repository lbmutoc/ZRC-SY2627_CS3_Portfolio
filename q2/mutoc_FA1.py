class libmaterial:
    def __init__(self, title, author):
        self.title = title
        self.author = author  
        
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")
        
class magazine(libmaterial):
    def __init__(self, title, author, issue_no):
        super().__init__(title, author)
        self._issue_no = issue_no
        
class book(libmaterial):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self._pages = pages
        
libmat1 = libmaterial("Python Programming", "John Doe")
mag1 = magazine("Tech Monthly", "Jane Smith", 42)
book1 = book("Data Science Handbook", "Alice Johnson", 350)

print("Library material information:")
libmat1.display_info()
mag1.display_info()
book1.display_info()
