#python function 
#function basics, perameters,return,if else
def dhruv():
    print("hellow, welcome to python!")
dhruv()

def dhruv_user(name):
    print("Hello",name)
dhruv_user("Dhruv")

def add(a,b):
    return a + b
result = add(10,20)
print(result)

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return"odd"
print("Number is:",check_even_odd(10))

def square(number):
    return number * number

print("Square:",square(5))
