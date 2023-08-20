#is a variation of insertion sort.
#sometimes called as "diminishing increment sort".
#time complexity is o(n^2) and best o(nlogn)
def shellsort(list1):
    gap = len(list1)//2
    while gap>0:
        for index in range(gap,len(list1)):
            current_element = list1[index]
            pos = index
            while pos>=gap and current_element < list1[pos-gap]:
                list1[pos] = list1[pos-gap]
                pos=pos-gap
            list1[pos] = current_element
        gap = gap//2

list1=[54,26,93,20]
shellsort(list1)
print(list1)
