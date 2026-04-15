# arithematic operators 
a=20 
b=2
print("addition operator ",a+b)   #addition 
print("subtraction operator",a-b)
print("multiplication operator",a*b)
print("divison operation",a/b)
print("modulus operation",a%b)
print("exponentiaton operation",a**b)
print("floor value",a//b)

# assigned operators 
a=5
a+=3 
print("additon operator",a )
a=5
a-=3
print("subtraction operator",a)
a=10 
a*=2
print("multiplication operator",a)
a=4 
a/=2
print("division operator",a)
a=4
a**=3
print("exponentiation operator",a)

# logical operator
a=45
b=65 
print(a>b and b>a)
print(a>b or b>a)
print(not a>b and b>a)
a,b=5,10
if ( a<b and b>a ):
    print("yes")