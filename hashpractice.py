class Hashtable:
    def __init__(self):
        self.max=10
        self.arr=[[] for i in range(self.max)]
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.max
    def __setitem__(self, key, val):
        h=self.get_hash(key)
        found=False
        for idx,elem in enumerate(self.arr[h]):
            if len(elem)==2 and elem[0]==key:
                self.arr[h][idx] =(key,val)
                found=True
                break
        if not found:
            self.arr[h].append((key,val))

    def __getitem__(self, item):
        h = self.get_hash(item)
        for elem in self.arr[h]:
            if elem[0]==item:
                return elem[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx ,kv in enumerate(self.arr[h]):
            if kv[0]==key:
                del self.arr[h][idx]




