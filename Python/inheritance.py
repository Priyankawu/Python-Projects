
# Inheritance: Parent-Child Relationship

class Parent:
    def __init__(self,fname,lname,gender):
        self.fname = fname
        self.lname = lname
        self.gender = gender
    def print_info(self):
       print("Firstname: "+self.fname+" \nLastname "+self.lname+" \nGender: "+self.gender)


class Child1(Parent): #inherits features from the Parent class
    def __init__(self, school, soccer_team, swim_team):
        self.school = school
        self.soccer_team = soccer_team
        self.swim_team = swim_team
    def song():
        print("My favorite songs are many.")


class Mother(Parent):
      def whoamI():
          print("Hi, I am the parent of your Parent class, ha ha!")
       
     
mom = Parent('Priyanka','Thak','Female')
mom.print_info()

child = Child1('SCDS','Seattle Celtic','Cascade Swim Team')
child.fname = "Hirsh"
child.song()

my_mother = Mother("Urmila", "Jha", "Female")
my_mother.whoamI()






    
