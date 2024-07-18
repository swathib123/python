#given string are anagram

first_name=input()
second_name=input()
first_letter_sorting=(sorted(first_name))
first_letter_sorting="".join(first_letter_sorting)
second_letter_sorting=(sorted(second_name))
second_letter_sorting="".join(second_letter_sorting)
if first_letter_sorting==second_letter_sorting:
    print("anagram")
else:
    print("not anagram")

print("..................................................")

#palindrome or not

first_letter=input()
first_letter=(first_letter.upper())
length=len(first_letter)
second_letter=first_letter[-1::-1]
second_letter=(second_letter.upper())
if first_letter==second_letter:
    print("palindrome")
else:
    print("not palindrome")

print(".............................................")

#replace the string space with given charcter
first_replace=input()
second_repalce= input()
result=""
for replacing in first_replace:
    if replacing==" ":
        result=result+second_repalce
    else:
        result=result+replacing
print(result)

print(".......................................")
#replace the string space with a given character using replace()method
first_replacing=input()
second_replacing=input()
print(first_replacing.replace(" ",second_replacing))

print(".............................................")
#lowecase to  uppercase
lower_case_upper=input()
print(lower_case_upper.upper())

#uppercase to lowercase
upper_case_lower=input()
sol=""
for vowels in upper_case_lower:
    if (vowels in "A,E,I,O,U,a,e,i,o,u"):
        sol=sol+(vowels.lower())
    else:
        sol=sol+vowels
print(sol)

#separte charcters in a given string
separte=input()
print(" ".join(separte))

#remove blank space
remove_blank_space=input()
e=(remove_blank_space.split())
print("".join(e))
#concatenate two strings using join method

join_string_1=input()
join_string_2=input()
print("".join([join_string_1,join_string_2]))
#concatenate two strings using without join method
withoutjoin_string_1=input()
withoutjoin_string_2=input()
print(withoutjoin_string_1+withoutjoin_string_2)