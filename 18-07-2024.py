#python program to check given character is vowel or consonant
char_vowel_consonant=input()
for vowel_consonant in char_vowel_consonant:
    if vowel_consonant in "a,A,I,i,e,E,o,O,U,u":
        print(vowel_consonant +" is a vowel")
    elif vowel_consonant==" ":
        continue
    else:
        print(vowel_consonant+" is a consonant")

# python program to check given character is digit or not
char_digit_not=input()
for digit_not in char_digit_not:
    if digit_not.isdigit():
        print(digit_not+ " is a digit")
    elif digit_not==" ":
            continue
    else:
        print(digit_not+ " not a digit")

#python program to delete vowels in given string
char_del_str=input()
result=""
for del_str in char_del_str:
    if del_str in "a,A,i,e,o,u,I,E,O,U":
        continue
    else:
        result=result+del_str
print(result)

#python program to count the occurrence of vowels and consonants in a string
char_count_vowels=input()
count=0
count_of_consonant=0
for count_of_vowels in char_count_vowels:
    if count_of_vowels in "a,i,e,o,u,A,I,E,O,U":
        count=count+1
    elif char_count_vowels==" ":
        continue
    else:
        count_of_consonant=count_of_consonant+1
print(str(count)+" is a vowel")
print(str(count_of_consonant)+" is a constant")
#python program to print the highest frequency character in string
char_highest_fre=input()
second_char_highest_fre=set(char_highest_fre)
dict={}
second_char_highest_fre=("".join(second_char_highest_fre))
for count_str in second_char_highest_fre:
    dict[count_str]=(char_highest_fre.count(count_str))
print(dict)
#python program to replace first occurrence of vowel with "-" in string
char_first_occurence=input()
count=0
req=""
for frst_occurrance in char_first_occurence:
        if frst_occurrance in "a,i,e,o,u,A,I,E,O,U":
            req=req+"-"
            count=count+1
            break
        else:
            req=req+frst_occurrance
            count=count+1
print(count)
print(req+char_first_occurence[count::])

#python program to count alphabets,digits and special charcters
count_alp_digi=input()
count=0
count_digit=0
count_special=0
for alp_digit_spec in count_alp_digi:
    if alp_digit_spec.isalpha():
        count=count+1
    elif alp_digit_spec.isdigit():
        count_digit=count_digit+1
    else:
        count_special=count_special+1
print("alphabets is :"+str(count))
print("digit is : "+str(count_digit))
print("special charcters : "+str(count_special))

#python program to check given charcter is digit or not using digit()method
char_without_digit=input()
print(",".join(char_without_digit))
for without_digit in char_without_digit:
    if without_digit.isalpha():
        print(without_digit+" is a not digit")
    else:
        print(without_digit +" is  a digit")
#python program to calculate sum of integers in string
calculate_sum=input()
sum=0
for sum_of_digit in calculate_sum:
    if sum_of_digit.isdigit():
        sum=sum+int(sum_of_digit)
print(sum)
#python program to print all non repeating character in string
char_reap_char=input()
non_repeating=""
for repeating_char in char_reap_char:
    if char_reap_char.count(repeating_char)==1:
        non_repeating=non_repeating+(repeating_char)
print(non_repeating)

#python program to copy one string to another string
one_string=input().split()
two_string=""
for number in one_string:
    two_string=two_string+number
print(two_string)