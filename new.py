nums=[1,0,1,1,0,1]
li=[]
z=0
for x in range(0,len(nums)):
    if(nums[x]==0):
        li.append(z)
        z=0
    else:
        z+=1