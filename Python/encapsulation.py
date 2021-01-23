#can have multiple classes in one file. They will be considered a package
import test_encapsulation

#Same class and subclasses can access/modify protected attributes
class Employee:
    def __init__(self, name, sal):
        self._name = name   #protected attribute so don't access from outside this class
        self._salary = sal

#Only the same class can access/modify private attributes
class Specialists:
    def __int__(self):
        self.__speciality = "cardiology"        #_classname__speciality
        self.__salary = "1000,000"
    def setSpeciality(self):
        self.__speciality = "electrophysiology"

    def setSalary(self):
        self.__salary = "8888"

    def getSalary(self):
        print(self.__salary)
    def getSpeciality(self):
        print(self.__speciality)
        


if __name__=="__main__":
    emp1 = Employee("Bob","10000")
    print(emp1._salary)
    emp1._salary = "9999"
    print(emp1._salary)
    
    doc1 = Specialists()
    
    # Python Name Mangling: Python changes the private names to _classname__attribute/method
    # example __salary becomes _Specialists__salary
    print(doc1.setSpeciality()) #calling from outside the class
    print(doc1.getSpeciality())
    print(dir(doc1))
   


    
    
