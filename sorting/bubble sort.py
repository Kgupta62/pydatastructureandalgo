#called as sinking sort
#time complexity is 0(n^2),best omega(n)
list1=[3,4,5,3,0]
for j in range(len(list1)-1):#range(len(list1))-1,0,-1)
    for i in range(len(list1)-1-j):#range(j)
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
print("sorted list",list1)