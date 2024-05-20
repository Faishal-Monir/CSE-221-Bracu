inpt=open("input2.txt","r"	)
otpt=open("output2(1).txt","w")

rng1=int(inpt.readline())  #range 1 
lst1=[int(i) for i in inpt.readline().split()] #list1 
rng2=int(inpt.readline())
lst2=[int(i) for i in inpt.readline().split()] #list2
#print(rng1,lst1,rng2,lst2)
rng_final=rng1+rng2
lst=lst1+lst2
lst.sort()



for i in range(rng_final):
    otpt.write(f"{lst[i]} ")


inpt.close()
otpt.close()

#============================Code-Explanation============================
"""
First took the values from the input file as range1, list1, range2, list2. Then added range(1+2) and got the final range of the list.
then merged the two list as one and named it lst-->(the final list). Then we sorted it using .Sort() method.Finally wrote the output
in the output file.

// Here the sort works as a merge sort and we have done the task in O(nlogn) time complexity. //


"""