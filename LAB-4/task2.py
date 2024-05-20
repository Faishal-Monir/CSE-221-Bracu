#=======================================Input Output=======================================
inpt=open("input/Task 02/input2_1.txt","r")
otpt=open("output2_4.txt","w")
v,e=[int(i) for i in inpt.readline().split()]

#====In-code-Matrix printer============            
def matrix_printer(data):    
    for i in data:
        if i==[]:
            print(0)
            continue
        for j in i:
            print(j,end=" ")
        print()
#=====================================


#=======================================Logic Part======================================
mtrix=[[] for i in range(v+1)]         #Making a empty matrix
final_lst=[]                           #final list of paths

for i in range(e):
    v1,v2=inpt.readline().split( )        #initializing undirected values in the matrix
    mtrix[int(v1)].append(int(v2))
    mtrix[int(v2)].append(int(v1))    

# matrix_printer(mtrix)  
# print(mtrix)

def bfs(g,s):                        #bfs code
    visited=[False]*len(g)           
    queue=[]                         # Queue based bfs code and list falgging based approach.
    queue.append(s)
    visited[s]=True 
    
    while queue:
        s=queue.pop(0)
        final_lst.append(s)
        
        for i in mtrix[s]:
            if visited[i]==False:
                queue.append(i)
                visited[i]=True
bfs(mtrix,1) 

for i in final_lst:                  #output printing
    otpt.write(str(i)+" ")
otpt.close()    
inpt.close()
