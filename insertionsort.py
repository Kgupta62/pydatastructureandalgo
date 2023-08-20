def insertionsort(list1):
    for index in range(1,len(list1)):
        current_element=list1[index]
        pos=index
        while current_element<list1[pos-1] and pos>0:
            list1[pos] = list1[pos-1]
            pos-=1
        list1[pos] = current_element

list1=[2,3,4,3,1]
insertionsort(list1)
print(list1)
