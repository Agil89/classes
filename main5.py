class Author():
    def __init__(self,name,email,gender):
        self.name= name
        self.email=email
        self.gender=gender
    def getName(self):
        return self.name
    def getEmail(self):
        return self.email
    def setEmail(self,email):
        self.email=email
        return self.email
    def getGender(self):
        return self.gender
    def toString(self):
        return f"Author[name={self.name},email={self.email},gender={self.gender}]"

Shair = Author('Mikayil Musfiq','musfiq@gmail.com','m')

class Book():

    def __init__(self,name,author,price,qty):
        self.name= name
        self.price= price
        self.author= author
        self.qty = qty

    def getName(self):
        return self.name
    def getAuthor(self):
        return self.author
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
        return self.price
    def getQty(self):
        return self.qty
    def setQty(self,qty):
        self.qty=qty
        return self.qty

    def toString(self):
        return f"Book name={self.name},{self.author.toString()}),price={self.price},qty={self.qty}"

kitab = Book('Daglar',Shair,50,10)

print(kitab.toString())