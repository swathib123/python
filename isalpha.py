""" n="swathi"
print(n.isalnum())
print(n.isalpha())


s={2*x for x in range(1,6)}
print(s) """

print(5)
"""sq=(map(lambda a:a*a))
print(sq(list(range(5))))"""

def iseven(number):
    if number%2==0:
        return number
        return square=number*number
range_of_list=list(range(1,10))
filter=list(filter(iseven,range_of_list))
res=list(map(square,filter))
print(res)