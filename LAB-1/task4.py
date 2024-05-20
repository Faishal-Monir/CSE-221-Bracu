#task-4
inpt=open("input4.txt","r")
otpt=open("output4.txt","w")

rng=inpt.readline()

data=[]                      #unsorted extracted data from the txt file  [['ABCD', 'Mymensingh', '00:30'], ['DhumketuExpress', 'Chittagong', '02:30']......
for i in range(int(rng)):
    temp=inpt.readline().split( )
    data.append([temp[0],temp[4],temp[6]])
# print(data)




for i in range(len(data)):                                #Lexicographical sorting the names only (Selection sort) Sort-1
    max_idx = i
    for j in range(i + 1, len(data)):
        if data[j][0] < data[max_idx][0]:
            max_idx = j
    data[i], data[max_idx] = data[max_idx], data[i]
#print(data)                                               #Names will be only sorted in the list 
            

dic={}

for j in data:              #Key:value for easier sorting --> {'ABC': [('Dhaka', '17:30'), ('Barisal', '03:00'), ('Khulna', '03:00')]}
    if j[0] not in dic: 
        dic.update({j[0]:[(j[1],j[2])]})
    elif j[0] in dic:
        dic[j[0]].append((j[1],j[2]))
#print(dic)
        

for a in dic.values():                  #selection sort to sort the time in dictionary  Sort-2
    for i in range (len(a)):
        min=a[i][1]
        min_idx=i
        for j in range(i+1,len(a)):
            if a[j][1]>min:
                min=a[j][1]
                min_idx=j
                
            if a[j][1]==a[i][1]:
                pass

        a[min_idx],a[i]=a[i],a[min_idx]
            

for i,j in dic.items():                                  
    for k in j: 
        otpt.write(f"{i} will departure for {k[0]} at {k[1]}\n")
        # print(f"{i} will departure for {k[0]} at {k[1]}\n")           #Tester line whether the output is right or wrong
inpt.close()
otpt.close()

#_______________________Code-Explanation_____________________________________
""" 
Finally for the last code we took the range and ran a loop and created a unsorted nested list of the trains [["Name","Destination",Time]]
['ABCD', 'Mymensingh', '00:30']. We could use a tuple but later we can not update it or reassign indexes in a tuple So used a list.

Then in (sort-1) using the basic selection sort we are sorting the names only in the nested list and python is doing it by default using the Unicode values and the 
conditions of the sorting algo. Now we create a dictionary for every names of the train where the name is the key and the destination and the time is stored in a list as values.
example:{'ABC': [('Dhaka', '17:30'), ('Barisal', '03:00'), ('Khulna', '03:00')]}

Now we sort the time in the dictionary values as we already assigned thenm in [(Destination,Time),(Destination,Time)]. Again using selction sort (Sort-2) we sorted the time in decending order.
And if the time is same for then we do nothing by using pass statement. 

Finally we have our sorted dictionary and then by using .items( ) we print the data in given format in the output file and close the opened files.
"""       
