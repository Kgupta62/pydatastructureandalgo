def delete(self,key):
    index=self.find(key)
    if self.table[index]==key:
        self.table[index] = None
        self.size-=1
def find(self, key):
    index = self.hash(key)
    while self.table[index] != None and self.table[index] != key:
        index = (index + 1) % self.M
    return index
def display(hashtable):
    for i in range(len(hashtable)):
        print(i,end=" ")
        for j in hashtable[i]:
            print("-->",end=" ")
            print(j,end=" ")
        print()
def hashing(keyvalue):
    return keyvalue%len(hashtable)
def insert(hashtable,keyvalue,value):
    hash_key=hashing(keyvalue)
    hashtable[hash_key].append(value)

hashtable = [[]for _ in range(10)]

insert(hashtable,10,"Bhopal")
insert(hashtable,25,"Bhopa")
insert(hashtable,20,"Bhop")
insert(hashtable,9,"Bho")
insert(hashtable,21,"Bh")
insert(hashtable,21,"B")

display(hashtable)

delete(9)

display(hashtable)