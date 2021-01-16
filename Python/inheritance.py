
# Inheritance: Parent-Child Relationship

class Parent:
    def __init__ (self,fname,lname,gender): #notice the self as a first parameter, which is not in arguments when instantiated`
        self.fname = fname
        self.lname = lname
        self.gender = gender
    #notice the self passed in as parameter
    def print_info(self):
        print("Firstname: {} \nLastname {} \nGender: {}".format(self.fname,self.lname,self.gender))

#This is a child of the Parent class
class Child1(Parent): #inherits features from the Parent class
    def __init__(self,school,soccer_team,swim_team,fname,lname,gender):
        self.school = school
        self.soccer_team = soccer_team
        self.swim_team = swim_team
        self.fname = fname
        self.lname = lname
        self.gender = gender
     #notice the self passed in as parameter
    def song(self):
        print("My favorite songs are many.")

#This is the other child of Parent class
class Mother(Parent):
    def whoamI(self):
        print("Hi, I am the parent of your Parent class, ha ha!")
       
     
mom = Parent('Priyanka','Thak','Female')
mom.print_info()

child = Child1('SCDS','Seattle Celtic','Cascade Swim Team','Hirsh','Gar','Male')
child.song()

my_mother = Mother("Urmila", "Jha", "Female")
my_mother.whoamI()






    
