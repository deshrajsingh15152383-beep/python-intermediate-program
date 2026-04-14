l=[2,4,6,7,7,3,5,3,4]
temp=l.copy()

for i in range(len(l)):
    if l[i] not in temp:
        continue

    count=1

    for j in range(len(temp-1,i,-1)):
        if(l[i]==temp[j]):
            count+=1
            temp.pop(j)
    print(f"frequency of {l[i]} is {count}")
