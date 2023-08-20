#time complexity is o(n^2)
#this is not for duplicate values
list1 = [56,2,3,54,6,7,0]
for i in range(len(list1)-1):
    min_val = min(list1[i:])
    min_index = list1.index(min_val)
    if list1[i] != list1[min_index]:
        list1[i],list1[min_index] = list1[min_index],list1[i]
print(list1)
#this is about duplicate list
list2=[2,3,5,3,56,0,76,2,5,7,0]
for i in range(len(list2)-1):
    min_val = min(list2[i:])
    min_index = list2.index(min_val,i)
    if list2[i] !=list2[min_index]:
        list2[i],list2[min_index] = list2[min_index],list2[i]
print(list2)
#without using min method
list2=[2,3,5,3,56,0,76,2,5,7,0]
for i in range(len(list2)-1):
    min_val = list2[i]
    for j in range(i+1,len(list2)):
        if list2[j] < min_val:
            min_val = list2[j]
    min_index = list2.index(min_val,i)
    if list2[i] !=list2[min_index]:
        list2[i],list2[min_index] = list2[min_index],list2[i]
print(list2)
#without using index method
list2=[2,3,5,3,56,0,76,2,5,7,0]
for i in range(len(list2)-1):
    m_ind=i
    for j in range(i+1,len(list2)):
        if list2[j] > list2[m_ind]:
            m_ind=j
    if list2[i] !=list2[m_ind]:
        list2[i],list2[m_ind] = list2[m_ind],list2[i]
print(list2)






















