class Author():
    name=None
    email=None
    gender=None

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


TestAuthor = Author('Nizami Gencevi',"krutoyGence@gmail.com",'m')

print(TestAuthor.email)
print(TestAuthor.name)
print(TestAuthor.toString())
# A class called Author (as shown in the class diagram) is designed to model a book's author. It contains:
# Three variables: name (String), email (String), and gender (char of either 'm' or 'f');
# One constructor to initialize the name, email and gender with the given values;
# public Author (String name, String email, char gender) {......}
# (There is no default constructor for Author, as there are no defaults for name, email and gender.)
# public getters/setters: getName(), getEmail(), setEmail(), and getGender();
# (There are no setters for name and gender, as these attributes cannot be changed.)
# A toString() method that returns "Author[name=?,email=?,gender=?]", e.g., "Author[name=Tan Ah Teck,email=ahTeck@somewhere.com,gender=m]".
# Write the Author class. Also write a test driver called TestAuthor to test all the public methods, e.g.,