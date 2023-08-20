class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.front=self.rear=None
    def isempty(self):
        return self.front==None
    def enqueue(self,item):
        temp=Node(item)
        if self.rear==None:
            return
        self.rear.next = temp
        self.rear =temp
    def dequeu(self):
        if self.isempty():
            return
        temp=self.front
        self.front=temp.next
        if (self.front == None):
            self.rear=None

if __name__=='__main':
    q=queue
    q.EnQueue(10)
    q.EnQueue(20)
    q.DeQueue()
    q.DeQueue()
    q.EnQueue(30)
    q.EnQueue(40)
    q.EnQueue(50)
    q.DeQueue()
    print(q)



