# The variable y is the LAMBDA FUNCTION here
y = lambda x: x*x*x

ans = y(4)
print(ans)

#PLACEHOLDER/ WILDCARD -- .format( , )

first = "Priyanka"
last = "Thakan"
print("Hello {} {}, welcome to Python!".format(first, last))

#format 16 to binary
x = format(16,'b')
print(x)

print("binary:{0:b} , hexadecimal:{0:b} , percentage:{0:%} ".format(4))

def getSum(num1, num2):
    answer = num1+num2
    print("The answer is: {}".format(answer))

getSum(2,14)

myAdd = getSum #myAdd variable represents the getSum function now

myAdd(48,38)

num1 = 3
num2 = 4
answer = "The answer is {}.".format(num1+num2)
print(answer)
