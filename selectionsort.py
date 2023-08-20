list1 = [2,3,0,0,32,4]
print(list1)
for i in range(len(list1)-1):
    #min_val = min(list1[i:])
    min_index = i
    for j in range(i+1,len(list1)):
        if list1[j] < list1[min_index]:
            min_index = j
    #min_index = list1.index(min_val,i) #this i  is inserted for handling duplicate values
    if list1[i] != list1[min_index]:
        list1[i] , list1[min_index] = list1[min_index] , list1[i]
print(list1)