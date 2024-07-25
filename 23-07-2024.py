#write a python program to merge two list
first_list=eval(input())
second_list=eval(input())
first_list.extend(second_list)
print(first_list)

#write a python program to delete element of given index in list
first_delete_index=eval(input())
first_delete_index.pop(1)
print(first_delete_index) 

#write a program to delete given element from the list
delete_element=eval(input())
delete_element.remove(1)
print(delete_element)

#write a python program to check if the two list are having atlest one common element
list_of_common=eval(input())
list_of_sec_comon=eval(input())
for number in list_of_common:
    if number in list_of_sec_comon:
        print(number)
    break

#write a program to remove specified column from the nestedlist
nested_list=eval(input())
add_nested_list=eval(input())
nested_list.insert(len(nested_list),add_nested_list)
nested_list.pop()
print(nested_list)

#write python program to covert a list of integer into single integer
list_of_integer=eval(input())
result=""
for single_integer in list_of_integer:
    result=result+str(single_integer)
print(result)
#write a python program to remove duplicates from the list
remove_dupli=[1,1,1,2,3,5,9,7,10,2,4,2,3]
lst=[]
sol=[]
for nums in range(len(remove_dupli)):
    list_add=[]
    for second_nums in remove_dupli:
        if remove_dupli[nums]==second_nums:
            list_add.append(second_nums)
    set_=(set(list_add))
    lst.extend(list(set_))
lst=(set(lst))
sol.extend(lst)
print(sol)