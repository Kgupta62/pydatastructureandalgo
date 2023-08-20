class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data: #we are ignoring duplicate values if we want to add that value in left then condition will become self.key>=data(same as right side we do if want that value in right side)
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self,data):
        if self.key == data:
            print("Node is found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in tree!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in tree!")

    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def postorder(self):
        if self.lchild:
            self.lchild.inorder()
        if self.rchild:
            self.rchild.inorder()
        print(self.key, end=" ")

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()

    def delete(self,data,curr):#curr=root.key
        if self.key is None:
            print("Tree is empty")
            return
        if data < self.key:
            if self.lchild:
               self.lchild = self.lchild.delete(data,curr)
            else:
                print("node is not present")
        elif data >self.key:
            if self.rchild:
               self.rchild = self.rchild.delete(data,curr)
            else:
                print("node is not present")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data ==curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data ==curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self = None
                return temp
            node=self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self

    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("smallest key",current.key)

    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("maxmimum key",current.key)

def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)

if __name__=='__main__':
    root = BST(None)
    # root.insert(20)
    list1 = [20,4,30,4]
    for i in list1:
        root.insert(i)
    root.search(10)
    print("preorder")
    root.preorder()
    print("inorder")
    root.inorder()
    print("postorder")
    root.postorder()
    if count(root)>1:
        root.delete(1,root.key)
    else:
        print("can't perform deletion operation")
    print("after deleting")
    root.preorder()
    print("count")
    print(count(root))
    root.min_node()
    root.max.node()
    # print(root.key)
    # print(root.lchild)
    # print(root.rchild)
    #
    # root.lchild = BST(5)
    # print(root.key)
    # print(root.lchild)
    # print(root.rchild)
    # print(root.lchild.key)
    # print(root.lchild.lchild)
    # print(root.lchild.rchild)