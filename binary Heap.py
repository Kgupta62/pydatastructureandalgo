import heapq
# heap=[]
# heapq.peapush(heap,10)
list1 = [(1,"riya") , (4,"sia") , (3,"gia")]
heapq.heapify(list1)
print(list1)
for i in range(len(list1)):
    print(heapq.heappop(list1))