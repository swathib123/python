name_of_the_stg=input()
length=len(name_of_the_stg)
count=0
result=""
while count<(length):
    result=result+str(name_of_the_stg[count])
    count=count+1
print(result)

name=input()
revers=""
for number in range(1,len(name)):
    revers=revers+(name[-number])
print(revers)