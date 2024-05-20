inpt=open("input1.txt","r"	)
otpt=open("output1(1).txt","w")

r_s=[int(i) for i in inpt.readline().split()]  #range and the sum [range,sum]
lst=[int(i) for i in inpt.readline().split()]  #list of the numbers [Numbers]

rng=r_s[0]
sm=r_s[1]

idx=[]
for i in range(rng):
    for j in range(rng):
        if i!=j:
            x=lst[i]+lst[j]
            if x==sm:
                idx.append((i+1,j+1))
#print(idx) #[(2, 4), (4, 2)]

if idx==[]:
    otpt.write(f"IMPOSSIBLE")
else:
    otpt.write(f"{idx[0][0]} {idx[0][1]}")
    
inpt.close()
otpt.close()


#============================Code-Explanation============================
"""
Took the numbers from input and took two separate lists for each category. Assigned the range at line-7 and the sum at line-8.
took a empty list named idx=[] that will store the final indexes. Implemented a nested loop and if the i and j index is 
same it will avoid those indexes. Then if the sum of (i) and (j) are equal to the sum it will append it to the list idx adding
1 to it as the output is (1) based indexed. Lastly if the idx list is empty then it is impossible otherwise we write the indexes 
to the output file.


"""
