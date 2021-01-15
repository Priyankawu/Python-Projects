
# Inheritance: Parent-Child Relationship

class Parent:
    def __init__(self,fname,lname,gender):
        self.fname = fname
        self.lname = lname
        self.gender = gender
    def print_info(self):
       print("Firstname: "+self.fname+" \nLastname "+self.lname+" \nGender: "+self.gender)

#This is a child of the Parent class
class Child1(Parent): #inherits features from the Parent class
    def __init__(self, school, soccer_team, swim_team):
        self.school = school
        self.soccer_team = soccer_team
        self.swim_team = swim_team
    def song():
        print("My favorite songs are many.")

#This is the other child of Parent class
class Mother(Parent):
      def whoamI():
          print("Hi, I am the parent of your Parent class, ha ha!")
       
     
mom = Parent('Priyanka','Thak','Female')
mom.print_info()

child = Child1('SCDS','Seattle Celtic','Cascade Swim Team')
# ?? Is this how I have to put in the values of parent features-fname,lname,gender??
child.fname = "Hirsh"
#?? Why does this method not work?? 
child.song()

#?? To create this child instance, I had to pass in the parent attributes while
# to create Child1 instance, I had to pass in the __init__ described values-school,
#soccer_team, swim_team. Why?? 
my_mother = Mother("Urmila", "Jha", "Female")
my_mother.whoamI()






    
