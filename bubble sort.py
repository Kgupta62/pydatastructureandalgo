def bubblesort(li):
    for i in range(len(li)-1):
        # print(li)
        for j in range(len(li)-i-1):
            if(li[j]>li[j+1]):
                li[j],li[j+1] = li[j+1],li[j]
    return li
li=[2,5,8,4,2,8,1]
print(bubblesort(li))

