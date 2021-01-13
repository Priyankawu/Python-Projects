#single lined comment
## this is for multiple lined commment
##    see you can keep going

##single line

def documentation():
    """This is the documentation for this method."""
    
    
    print("Hello")

print(documentation.__doc__)


def printMe():
    """this is my docstring
    """
    print("hello")
    print(2+5)

printMe()
print(printMe.__doc__)
print(2+5)


