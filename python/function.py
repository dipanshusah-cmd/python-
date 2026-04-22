
def calc_sum(a,b):
    sum = a + b 
    #print(sum)
    return(sum) 

def calc_sqr(a):
    sqr = a*a 
    print(sqr)
    return(sqr)

def greeting():
    greeting_msg = "Hi" 
    user_name = input("Enter your name :")
    print(greeting_msg,user_name)
    return()


def calc_avg(a,b,c):
    avg = (a+b+c)/3
    print(avg)
    return(avg)

def evnorodd(a):
    if a%2==0 and a != 0 :
        print("Number is even")
    elif a%2!=0 :
        print("Number is odd")
    elif a == 0 :
        print("Number is zero")
    return(a)
  
def grt2():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if a > b :
        print("First number is greater than second number: ")
    else :
        print("Second number is greater than first number: ")
    return(a,b)

def max():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    if a > b and a > c :
        print("First number is greater")
    elif b > a and b > c :
        print("Second number is greater")
    else :
        print("Third number is greater ")
    return()
  
    
def pnz():
    a = int(input("Enter number:"))
    if a > 0 :
        print("Number is positive")
    elif a < 0 :
        print("Number is negative")
    else :
        print("Number is zero")
    return()

def sum_of_n_numbers():
    n = int(input("Enter last number: "))
    sum = 0 
    for i in range(1,n) :
        sum = i+sum 
        #print(sum)
    return(sum)

def table():
    n = int(input("Enter number: "))
    table = []
    for i in range(1,11):
        product = n*i
        table.append(product)
        
    return(table)

def evn_in_range():
    n = int(input("Enter last number of range: "))
    even = 0
    for i in range(1,n):
        if i % 2 == 0 :
            even = i
        #print( even)   
    return(even)

