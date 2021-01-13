import app1

def print_app2():
    name = (__name__) #dunder name dunder is the name (main) of this file/module
    return name

if __name__ == "__main__":  
    # The following is calling code from within the script
    print("I am running code from {}".format(print_app2()))

    # The following is calling code from the imported app1.py
    print("I am running code from {}".format(app1.print_app()))

    
