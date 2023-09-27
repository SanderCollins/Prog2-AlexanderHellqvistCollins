str = input('Enter 3 numbers').split(' ')
str = [eval(i) for i in str]
lst = []
x = 1
while x <= str[2]:
    if x % str[0] == False and x % str[1] == False:
        lst.append("FizzBuzz")
    elif x % str[0] == False:
        lst.append("Fizz")
    elif x % str[1] == False:
        lst.append("Buzz")
    else:
        lst.append(x)
    x += 1

print(lst)