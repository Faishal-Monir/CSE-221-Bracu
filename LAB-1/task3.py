#task-3
inpt=open("input3.txt","r")
otpt=open("output3.txt","w")

rng=int(inpt.readline())
id=inpt.readline().split( )
mrk=inpt.readline().split( )
#print(id,mrk)

lst=[]

for i in range (rng):
    lst.append( (int(mrk[i]),int(id[i])) )  #[(40, 7), (50, 4), (50, 9), (20, 3), (10, 2), (10, 5), (10, 1)] -->for input 1


dic={}

for j in lst:
    if j[0] not in dic:
        dic.update({j[0]:[j[1]]})
    elif j[0] in dic:
        dic[j[0]].append(j[1])                         # {40: [7], 50: [4, 9], 20: [3], 10: [2, 5, 1]} -->for input 1

pair=list(dic.items())
# print(pair)              [(40, [7]), (50, [4, 9]), (20, [3]), (10, [2, 5, 1])]
for i in range(len(pair)): #Sorting Dictionary keys in descending order
    max_idx = i
    for j in range(i + 1, len(pair)):
        if pair[j][0] > pair[max_idx][0]:
            max_idx = j
    pair[i], pair[max_idx] = pair[max_idx], pair[i]

    

for i in range(len(pair)): #sorting values of dictionary in ascending order
    val = pair[i][1]
    for j in range(len(val)):
        min_idx = j
        for k in range(j + 1, len(val)):
            if val[k] < val[min_idx]:
                min_idx = k
        val[j], val[min_idx] = val[min_idx], val[j]
        
#print(pair) #sorted final list  [(50, [4, 9]), (40, [7]), (20, [3]), (10, [1, 2, 5])] -- >For input 1



for i,j in pair:  # k=id , i= marks, j=lists of Id [id,id,id]
    for k in j :
        otpt.write(f"ID: {k} Mark: {i}\n")
inpt.close()
otpt.close()

#_______________________Code-Explanation_____________________________________
""" 
For this code we firt took the range. then we took the ids and the marks in two separate lists.Then we formed a list of tuple for every 
id and the corresponding value for easier calculation. Then made a dictionary making the Numbers as Key and the id values as there are multiple id 
that got the same marks. Then we made a list of key value pairs using dic.items( ) and sorted that lists keys in descending order by using Selection sort.

Again sorted the values or the ids of that list in Ascending order by using selection sort. So finally for (input-1) the list became this 
[(50, [4, 9]), (40, [7]), (20, [3]), (10, [1, 2, 5])]. Latly we type formated the list and wrote the designated output in the output file.
 
"""        
    
    