#kahns-algo
#just change the number after input(EX: input2,input3) and it will show that output accordingly !
#=======================================Input Output=======================================
inpt=open("input/t1/input1.txt","r")
otpt=open("output1_B.txt","w")
v,e=[int(i) for i in inpt.readline().split()]
#=======================================Logic Part=======================================
a_list=[[] for i in range(v+1)] 

for i in range(e):
    v1,v2=inpt.readline().split( )
    a_list[int(v1)].append(int(v2))

final_list=[] 

def topo_sort(a_list,nodes):
    
    degree=[0]*(nodes+1)
    for i in range(0,len(a_list)):
        for j in a_list[i]:
            degree[j]+=1
            
    queue=[]
    n_count=0
    for i in range(1,len(degree)):
        if degree[i]==0:
            queue.append(i)
            
    while queue:
        temp_node=queue.pop(0) 
        final_list.append(temp_node)
        
        for sub_elem in a_list[temp_node]:
            degree[sub_elem]-=1
            if degree[sub_elem]==0:
                queue.append(sub_elem)
                
        n_count+=1
    return n_count
    
counter=topo_sort(a_list,v) 
if counter!=v:
    otpt.write("IMPOSSIBLE") 
else:
    for elem in final_list:
        otpt.write(str(elem)+" ")
        
otpt.close()
inpt.close()        