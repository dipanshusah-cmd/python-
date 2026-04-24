
# def calc_sum(a,b):
#     sum = a + b 
#     #print(sum)
#     return(sum) 

# def calc_sqr(a):
#     sqr = a*a 
#     #print(sqr)
#     return(sqr)

# def greeting():
#     greeting_msg = "Hi" 
#     user_name = input("Enter your name :")
#     #print(greeting_msg,user_name)
#     return(greeting_msg , user_name)


# def calc_avg(a,b,c):
#     avg = (a+b+c)/3
#     #print(avg)
#     return(avg)

# def evnorodd(a):
#     if a%2==0 and a != 0 :
#         return("Number is even")
#     elif a%2!=0 :
#         return("Number is odd")
#     elif a == 0 :
#         return("Number is zero")
#     # return(a)
  
# def grt2():
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     if a > b :
#         return("First number is greater than second number: ")
#     else :
#         return("Second number is greater than first number: ")
#     #return(a,b)

# def maximum():
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     c = int(input("Enter third number: "))
#     if a > b and a > c :   
#         return("First number is greater")
#     elif b > a and b > c :
#         return("Second number is greater")
#     else :
#         return("Third number is greater ")
#     #return()
  
    
# def pnz():
#     a = int(input("Enter number:"))
#     if a > 0 :
#         return("Number is positive")
#     elif a < 0 :
#         return("Number is negative")
#     else :
#         return("Number is zero")
#     #return()

# def sum_of_n_numbers():
#     n = int(input("Enter last number: "))
#     sum = 0 
#     for i in range(1,n) :
#         sum = i+sum 
#         #print(sum)
#     return(sum)

# def table():
#     n = int(input("Enter number: "))
#     table = []
#     for i in range(1,11):
#         product = n*i
#         table.append(product)
        
#     return(table)

# def evn_in_range():
#     n = int(input("Enter last number of range: "))
#     even = 0
#     for i in range(1,n):
#         if i % 2 == 0 :
#             even += 1
#         #print( even)   
#     return(even)



# # def even_in_list(a) :
# #     a = [input("Enter list :")]
# #     even = 0
# #     for i in list :
# #         if i % 2 == 0 :
# #             even += 1         
# #     return(even)

# # def odd_in_list(list) :
# #     odd = 0
# #     for i in list :    
# #         if i % 2 != 0 :
# #             odd += 1 
# #     return(odd)

    
# def function_l(*a) :
#     l = list(a)
#     even = 0
#     odd = 0
#     small = min(l)
#     large = max(l)
#     div3 = []
#     for i in l :
#         if i % 2 == 0 :
#             even += 1 
#         elif i % 2 != 0 :
#             odd += 1
        
    
#     return even, odd, small, large

# print(function_l(1, 2, 3))
 
 
#Password validator(Password must be at least 8 character, one upper case  , special character, isalum)

# def password_validator(a) :
#     a = input("Create password : ")
#     has_8_letter = False 
#     has_upper = False
#     has_lower = False
#     has_special_char = False
#     for i in a :
#         if len(a)<8 :
#             has_8_letter = True
         
class student:
    def __init__(self,name,age,roll_no,classs) :
        self.name = name
        self.age = age 
        self.roll_no = roll_no 
        self.classs = classs 
    def showdetails(self):
            print("Name is",self.name)
            print("Age is " , self.age)
            print("roll no is",self.roll_no)
            print("class is",self.classs)
            print()
        
     
s1 = student("dipanshu",18,254088,"btech")
s2 = student("Rahul",20,254025,"B.Tech")
s1.showdetails()
s2.showdetails()
