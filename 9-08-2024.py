"""Write a program which can filter even numbers in a list by using filter function. The list is: 
[1,2,3,4,5,6,7,8,9,10]"""
def iseven(number):
    if number%2==0:
        return True
    else:
        return False
range_of_list=list(range(1,10))
filter=list(filter(iseven,range_of_list))
print(filter)

"""2. Write a program which can map() to make a list whose elements are square of elements in 
[1,2,3,4,5,6,7,8,9,10]."""
def issquare(number):
    number=number*number
    return number
range_of_num=list(range(1,10))
map_of=list(map(issquare,range_of_list))
print(map_of)

"""Write a program which can map() and filter() to make a list whose elements are square of even 
number in [1,2,3,4,5,6,7,8,9,10]."""
def is_even(number):
    return number%2==0
def square(number):
    return number*number
range_of_list=list(range(1,11))
square_of_even_number=list(map(square,filter(is_even,range_of_list)))
print(square_of_even_number)
"""4. Write a program which can filter() to make a list whose elements are even number between 1 and 
20 (both included)."""
def iseven(number):
    if number%2==0:
        return True
    else:
        return False
range_of_list=list(range(1,21))
filter=list(filter(iseven,range_of_list))
print(filter)
"""5. Define a class named American and its subclass NewYorker."""
class American:
    def __init__(self,name):
        self.name=name
    def get_name(self):
        print(self.name)
class newyorker(American):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def get_age(self):
        super().get_name()
        print(self.age)
add=newyorker("swathi",24)
add.get_age()
"""7. Define a class named Rectangle which can be constructed by a length and width. The Rectangle 
class has a method which can compute the area."""
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def get_res(self):
        print(self.length*self.width)
result=Rectangle(4,5)
result.get_res()
"""8. Write a function that returns the lesser of two given numbers if both numbers are even, but 
returns the greater if one or both numbers are odd"""
def func(a,b):
    if a%2==0 and b%2==0:
        print(min(a,b))
    else:
        print(max(a,b))
func(2,4)
func(6,3)
"""10. Write a function that capitalizes the first and fourth letters of a name"""
def  capitalize_first_fourth(name):
    name=list(name)
    if len(name)>0:
        name[0]=name[0].upper()
    if len(name)>3:
        name[3]=name[3].upper()
    print("".join(name))
letter=input()
capitalize_first_fourth(letter)