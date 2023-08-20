#time complexity is 0(logn)
def Binarysearch(list1,key):
    low=0
    high=len(list1)-1
    found=False
    while low<=high and not found:
        mid = (low+high)//2
        if key == list1[mid]:
            found=True
        elif key> list1[mid]:
            low=mid+1
        else:
            high=mid-1
    if found==True:
        print("key is found")
    else:
        print("key is not found")

list1=[2,3,4,5,6,7,8,2,4,6]
list1.sort()
key=int(input("eneter the key element:"))
Binarysearch(list1,key)