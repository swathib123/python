#insert an element at end of an array
insert_element=eval(input())
add_element=input()
insert_element.append(add_element)
print(insert_element)

#insert element at a given location in array
char_insert_element=eval(input())
index_element=int(input())
add_value=input()
char_insert_element.insert(index_element,add_value)
print(char_insert_element)

#python program to check the sizes of given two list are same
length_of_first_string=eval(input())
length_of_second_string=eval(input())
if len(length_of_first_string)==len(length_of_second_string):
    print("Both are same length")
else:
    print("not same length")

#python program to create a list
create_list=eval(input())
print(list(create_list))

using_split_list=input()
add_split=using_split_list.split()
print(add_split)

range_of_first_element=int(input())
range_of_second_element=int(input())
add_integer=range(range_of_first_element,range_of_second_element+1)
print(list(add_integer))

name=input()
print(list(name))
#python program to access a given element from the nested list
acess_element=eval(input())
access_number_of_start =int(input())
access_number_of_end=int(input())
print(acess_element[access_number_of_start])
print(acess_element[access_number_of_start:access_number_of_end:])
#write a python program to find largest and smallest number in list
largest_smallest_num=eval(input())
print(max(largest_smallest_num))
print(min(largest_smallest_num))

#write a python program to sum of lists elements
sum_of_list=eval(input())
sum=0
for number in sum_of_list:
    sum=sum+number
print(sum)

#python program to reverse an list in two ways

reverse_list=eval(input())
reverse_list.reverse()
print(reverse_list)
print(reverse_list[::-1])