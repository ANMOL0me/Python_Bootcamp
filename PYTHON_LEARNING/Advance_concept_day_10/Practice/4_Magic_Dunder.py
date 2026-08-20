'''4. Magic/Dunder Methods
Create a class Book with attributes title and author.

Implement __str__() so that printing the object displays "Title by Author".
Implement __len__() so that len(book) returns the length of the title.
Create two Book objects and test these methods.'''

class Book:
 def __str__(self,title,author):
  print(f"{title} by {author}")
 def __len__(self,book):
  print(len(book))
obj1 = Book()
obj1.__str__("Take me to the moon","Austin")
obj1.__len__("MIGHTYs")
 
  

