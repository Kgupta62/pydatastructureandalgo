n=input("enter a number")
lit=[]
for i in n:
    lit.append(i)
z=""
for i in range(len(lit)-1,-1,-1):
    z+=lit[i]
print(z)