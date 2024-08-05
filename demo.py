"""for num in range(1,10):
    pass
for number in range(1,16):
    if number == 15:
        break
    else:
        if number==5:
            continue
    print(number)"""
l=[1,2,3,4,1,5,0]
target=5
for num in range(len(l)):
    for num_1 in range(num+1,len(l)):
            if (l[num]+l[num_1])==4:
                print(l[num],l[num_1],l[num]+l[num_1])





  