inpt=open("input1.txt","r"	)
otpt=open("output1(2).txt","w")

r_s=[int(i) for i in inpt.readline().split()]  #range and the sum [range,sum]
lst=[int(i) for i in inpt.readline().split()]  #list of the numbers [Numbers]

rng=r_s[0]
sm=r_s[1]

idx=[]

i1=0
i2=rng-1

while i2>i1:
    temp=lst[i1]+lst[i2]
    if temp<sm:
        i1+=1
    elif temp>sm:
        i2-=1
    elif temp==sm:
        idx.append((i1+1,i2+1))
        break
    
# print(idx)
        
if idx==[]:
    otpt.write(f"IMPOSSIBLE")
else:
    otpt.write(f"{idx[0][0]} {idx[0][1]}")
    
inpt.close()
otpt.close()

#============================Code-Explanation============================
"""
Took the numbers from input and took two separate lists for each category. Assigned the range at line-7 and the sum at line-8.
took a empty list named idx=[] that will store the final indexes. then took two pointers i1, i2. i1 starts itterating from the
front index and i2 from the back index. There is a simple logic in the while loop if the sum of the pointer i1+i2 is less than
the given sum then i1 will increase. And if the sum is bigger then i2 will decrease. and if i2>i1 it will break returning the idx
list empty. Same as perviously if the idx list is empty it means impossible otherwise we write the indexes to the output file as 
(1) based indexes.     \\ here there is only while loop menas we did the task in O(n) time complexity.  \\ 


"""