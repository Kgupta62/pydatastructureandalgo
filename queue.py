# from collections import deque
# queue=[]
# queue.insert(0,132)
# queue.insert(0,135)
# queue.insert(0,131)
# print(queue)
# print(queue.pop())
# q=deque()
# q.appendleft(5)
# q.appendleft(6)
# q.appendleft(7)
# print(q)
# print(q.pop())

from collections import deque
class queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self,val):
        self.buffer.appendleft(val)
    def dequeue(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)
pq = queue()
pq.enqueue({
    'company':'wall mart',
    'timestamp':'15 apr,11.01 AM',
    'price':131.10
})

pq.enqueue({
    'company':'wall mart',
    'timestamp':'15 apr,11.02 AM',
    'price':132
})

pq.enqueue({
    'company':'wall mart',
    'timestamp':'15 apr,11.03 AM',
    'price':135
})

print(pq.buffer)
print(pq.dequeue())
print(pq.size())