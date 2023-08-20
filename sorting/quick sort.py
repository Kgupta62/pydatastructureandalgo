#also called as partition exchange sort.
#when implemented well it can be about 2 or 3 times faster than the its main competitors merge sort and heap sort.
#it is comparison sort,in_place,unstable,recusrsive algorithm.
#time complexity is o(n^2),best omega(n(log(n)))
#it is divide and conquer and combine method.
#three conditions are====1-left<=right,2-a[left]<=pivot,3-a[right]>=pivot(if 2 is false then check 3)(if 1 become false then swap pivot with right)
def pivot_place(list1,first,last):
    pivot= list1[first]
    left =first+1
    right = last
    while True:
        while left<=right and list1[left] <= pivot:
            left = left+1
        while left<=right and list1[right] >=pivot:
            right = right-1
        if right<left:
            break
        else:
            list1[left],list1[right] = list1[right],list1[left]
    list1[first], list1[right] = list1[right], list1[first]
    return right

def quicksort(list1,first,last):
    if first<last:
        p=pivot_place(list1,first,last)
        quicksort(list1,first,p-1)
        quicksort(list1,p+1,last)

#main
list1=[56,34,13,13,0]
quicksort(list1,0,len(list1)-1)
print(list1)

















