def binarysearch(li,l,r,k):
    if r>=1:
        mid=0+(r-1)//2
        if li[mid]==k:
            return mid
        elif li[mid]>k:
            return binarysearch(li,l,mid-1,k)
        else:
            return binarysearch(li,mid+1,r,k)
    else:
        return -1
li=[1,2,3,4,5,6]
k=3
print(binarysearch(li,0,len(li)-1,k))