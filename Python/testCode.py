mySentence = 'I love the color '

color_list = ['red','blue','green','pink','teal','black']

print(len(color_list))

#print("{}.format(color_list[0])")
#print("{} {}".format(mySentence,color_list[0]))


def color_function(name):
    lst = []
    for i in color_list:
        msg = "{} {} {}".format(name,mySentence, i) #{} is wildcard
        lst.append(msg)
    return lst


def get_name():
    go = True
    while go:
        name = input('What is your name? ') #how to get an input answer
        if name == '':
            print('You need to provide your name!')
        elif name == 'Sally':
            print("Sally, you may not use this software.")
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)

get_name()

arr = [91,2,13,4,2,2,7,18,9,10]
x = arr.count(2)
print(x)
arr.sort()
print(arr)
