##
##Python: 3.9
##
##Author: Priyanka Thakan
##
##Purpose:

def start():
    f_name = input("first name? ")
    l_name = input("last name ? ")
    age = 39
    gender = "Female"
    get_info(f_name, l_name, age, gender)
    

def get_info(f_name, l_name, age, gender):
    print("my name is {0} {1}. I am {2} year old {3}.".format(f_name, l_name, age, gender))
   





if __name__ == "__main__":
    start()
