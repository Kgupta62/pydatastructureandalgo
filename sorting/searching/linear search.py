#time complexity is o(n)
def search(list1,key):
    for i in range(len(list1)):
        if key == list1[i]:
            print("key element is found",i)
            break
    print("element is not found")

list1=[2,3,4,63,2,1,2]
key=int(input("enter the element:"))
search(list1,key)
