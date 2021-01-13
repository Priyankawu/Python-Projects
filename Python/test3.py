



def getInfo():
    var1 = input("\nPlease provide the first numeric value: ") #input is string type
    var2 = input("\nPlease provide the second numeric value: ")
    return var1,var2



def compute():
    go = True
    while go:
        var1,var2 = getInfo()
        print(var1, var2)
        try:
            var3 = int(var1) + int(var2)
            go = False
        except ValueError as e: #built in name of the error
            print("{}: \n\nYou did not provide a numeric value".format(e))
        except:
            print("\nOops, you provided invalid input, program will close now")
    print("{} + {} = {}".format(var1, var2, var3))






if __name__ == "__main__":
    compute()
