class book:
    count=0
    def __init__(self,name,author):
        self.name=name
        self.author=author
        book.count+=1

    def display(self):
        print(f"Name :{self.name}\nAuthor :{self.author}")
        print("--"*25)
    
    @classmethod
    def getcount(cls):
        return cls.count


b1=book("hare krishna","anadaroopam")
b2=book("Radhe Radhe","premananda")
b3=book("hello city","john dennie")
b1.display()
b2.display()
b3.display()
print("total books :")
print(book.getcount())