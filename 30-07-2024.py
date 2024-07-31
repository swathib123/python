#write a python program to add a key to a dictonary
add_dic=dict()
number=int(input())
for nums in range(number):
    name_key=input()
    name_value=input()
    add_dic[name_key]=name_value
print(add_dic)
#write a python program to check where the given value is present in the dictionary or not
dic_or_not=eval(input())
values=input()
only_value=dic_or_not.values()
print(values in only_value)
#write a python script to print a dictionary where the keys are numbers between 1 and 15 (both included and the values are the square of the keys)
num_1_to_15={}
for num in range(1,15+1):
    num_1_to_15[num]=num*num
print(num_1_to_15)

#write a python to create a dictionary from the string
stn="name=swathi,age=23,qualification=mca"
stn=stn.split(",")
dict_1={}
for number in stn:
    strin1,strin2=number.split("=")
    dict_1[strin1]=strin2
print(dict_1)
#write a python program to combine two dictionary by adding values of commom keys
first_str=eval(input())
second_str=eval(input())
dic_commonvalues={}
for number in first_str:
    if (number) in second_str:
        adding=(first_str[number]+second_str[number])
        dic_commonvalues[number]=adding
print(dic_commonvalues)
#write a python program to merge two python dictionary
first_merge=eval(input())
second_merge=eval(input())
first_merge.update(second_merge)
print(first_merge)