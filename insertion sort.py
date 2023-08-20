def insertionsort(li):
    for i in range(1,len(li)):
        key = li[i]
        j=i-1
        while j>=0 and key < li[j]:
            li[j+1]=li[j]
            j-=1
        li[j+1] = key
    return li

li=[12,11,13,5,6]
print(insertionsort(li))