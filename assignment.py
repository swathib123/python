space_name=input()
result=""
for words in space_name:
    if words == " ":
        continue
    result=result+words
print(result)

print(".....................................")

length_of_string=input()
print(len(length_of_string))

print("......................................")
#sum of first 10 ....natural number
nature_num=int(input())
sum=0
for nature_number in range(1,nature_num+1):
    sum=sum+nature_number
print(sum)

print(".........................................")

#To read integer and convert it into  float
int_num = int(input())
print(float(int_num))

print(".............................................")
#To find greater among two numbers
A=int(input())
B=int(input())
if A>B:
    print(A)
else:
    print(B)

print("...............................................")

#two inputs strings from the user print greatest among
first_string=input()
second_string=input()
if first_string>second_string:
    print(first_string)
else:
    print(second_string)

print(".................................................")
#given number is even or odd

n=int(input())
if n%2==0:
    print("Even")
else:
    print("Odd")
print("........................................")
#positive or negative

pos_or_neg=int(input())
if pos_or_neg>0:
    print("postive")
else:
    print("negative")

print("...............................................")
