#write a program to create a set
create_set=eval(input())
create_set=set(create_set)
print(create_set) 
#write program to iterate over sets
iterate_set=eval(input())
for iterate in iterate_set:
    print(iterate) 
#write a python program to add member to a set
first_set=eval(input())
add_number=eval(input())
first_set.add(add_number)
print(first_set) 

#write a program to create a intersection of set
set_1=eval(input())
set_2=eval(input())
print(set_1 & set_2)

#write a python program to create a union of set
set_union_1=eval(input())
set_union_2=eval(input())
print(set_union_1|set_union_2)

#write a python program to create a symmetric defferance
set_symmetric_1=eval(input())
set_symmetric_2=eval(input())
print(set_symmetric_1.symmetric_difference(set_symmetric_2))

#write a python program to fixd max and min value in a set
max_min_set=eval(input())
print(max(max_min_set))
print(min(max_min_set))

#Given two python set,write a python program to update the first set with items that exist only in he first set and not in the second set
set_1=eval(input())
set_2=eval(input())
print(set_1 & set_2)

#write a python program  to remove items 10,20,30 from the following set at once.
remove_set=eval(input())
second_remove_set={10,20,30}
print(remove_set-second_remove_set)

#check if two sets have any elements in common.if yes,display the common elements
dsplycommelemt_1=eval(input())
dsplycommelemt_2=eval(input())
print(dsplycommelemt_1 & dsplycommelemt_2)

#update set1 by adding items from set2,expect common items
set_symmetric_1=eval(input())
set_symmetric_2=eval(input())
print(set_symmetric_1.symmetric_difference(set_symmetric_2))
