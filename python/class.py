# i = 40

# while i <= 65:
#     print(i)
#     i=i+2
# a = 40
# b = 65 
# if a  > b: 
#     print("Yes")
# else:    print("No")
# while (a <= b):
#     print(a)
#     a = a + 1
#     print(a)
#first answer 
# for a in range(1, 100):
#     if a % 2 == 0 and a % 3 == 0:
#         print(a)
#second answer
# a = input("Enter any word ")
# reversed_word = a[::-1]
# print("Reversed word is ", reversed_word)
# OR
# a = list(input("Enter any word "))
# b = ""
# for i in a :
#     b = i + b
#     print("reversed word is", b)
    
# for a in range(1, 20) : 
#     a == 1 
#     print(a)
#     continue
# a = [1,2,3]
# b = [4,5,6]
# def username():
#   a = input("enter your name : ")
#   print("Hello" , a)
# username()    
# def temp(c): # Iske ander ke variables ko arguments kahte hai 
#     F = ((9*c))/5+32
#     return F
# c = int(input("Enter temp in celcius : "))
# b = temp(c) # Iske ander ke variables ko parameters kahte hai 
# print( "Temperature in Fahrenheit is :" , b)
# def fruit(a):
#     return a
# def fruit(a,b):
#     return a,b
# def fruit(a,b,c):
#     return a,b,c
# a = [1,3,4,5]
# b = [5,6,7]
# c = a+b
# a.extend(b)
# print(c,a)       
# a = [1,2,3,4]
# a.pop[0:2]
# print(a)
# list.insert(1,5)
# listb = [ 6 , 7 , 8]
# list.extend(listb)
# print(list)

#Answer 1 
# a = int(input("Enter first value : "))
# b = int(input("Enter  second value : "))
# c = int(input("Enter  third value : "))
# list =[ a , b , c ] 
# print(list) 

# Answer 2 
# list = []
# for list in range(1,5):
#      print(list)

# Answer 4 
# a = "This is a string"
# b = a.count('a')
# c = a.count('e')
# d = a.count('i')
# f = a.count('o')
# g = a.count('u')
# print(b,c,d,f,g)
#  # OR 
# a = " This is a sting "
# for vowels in str(a) :
    
# Answer 5 
# a = [
#     int(input("Enter first value : ")) ,
#     int(input("Enter second value : ")) ,
#     int(input("Enter third value : ")) ,   
#     int(input("Enter fourth value : ")) ,
#     int(input("Enter fifth value : ")) ,   
    
#     int(input("Enter sixth value : ")) ,
# ]
# b = sum(a) 
# print("Sum of this list is " ,b)
# c =  b/5
# print("Average of this given list is",c)
# a.sort()
# e = a[5]
# print(a)
# print(e)


# d = { 
#      "student name" : "Dipanshu Raj " ,
#      " studentt age":  18 ,
#      "course" : "Btech" }   
# print(d["student name"])                         
# d["student age" ] = 19
# d["Grade" ]     = "A"                                                                                                                                                                                                                                                                                                                                                          
# print(d)


book = {
    "title" : " Mr star physics " ,
    "Author" : " Manish Raj" ,
     "price" : 499
}
 
book["year"] = 2025 
book["price"] = 399
del book["Author"] 
#print(book)
 