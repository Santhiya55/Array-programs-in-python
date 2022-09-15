# Find duplicate numbers in given array

l=[1,2,1,3,4,3,5,6,4,5]
l1=[ ]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')
    
