# a=[]
# a.append('kuber')
# a.append('jk')
# a.append('divya')
# print(a)
# print(a.pop())
# print(a)
# from collections import deque
# stack = deque()
# # print(dir(stack))
# stack.append("kuber")
# stack.append("kg")
# stack.append("divya")
# print(stack)
# print(stack.pop())
# print(stack)
from collections import deque
class stack:
    def __init__(self):
        self.container = deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.conatiner)
if __name__=='__main__':
    s=stack()

