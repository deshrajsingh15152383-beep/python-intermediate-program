l=[2,4,6,7]
l2=[2,3,5,7]

temp=l2.copy()
for i in range(len(l)):
    for j in range(len(temp)):
        if(l[i]== temp[j]):
            print(f"{l[i]}",end=" ")
            temp.pop(j)

print(" are same in the lists")
