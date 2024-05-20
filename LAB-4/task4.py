#=======================================Input Output=======================================
inpt=open("input/Task 04/input4_2.txt","r")
otpt=open("output4_2.txt","w")
v,e=[int(i) for i in inpt.readline().split()]
#=======================================Logic Part=======================================
mtrix=[[] for i in range(v+1)]         #empty matrix


for i in range(e):                      #assigning values in the directed matrix
    v1,v2=inpt.readline().split( )
    mtrix[int(v1)].append(int(v2))  
    

    
def dfs(node,mtrix,visited,stack):     #recursive double list based cycle finding approach
    stack[node]=True
    visited[node]=True
    for sub_nodes in mtrix[node]:
        if visited[sub_nodes]==False:
            if dfs(sub_nodes,mtrix,visited,stack)==True:
                return True 
        if stack[sub_nodes]==True:
            return True 
    stack[node]=False
    return False    


def cycle(mtrix,node):                #matrix itterating function 
    visited=[False]*(node+1)    
    stack=[False]*(node+1)
    for i in range(1,len(mtrix)):
        if visited[i]==False:
            if dfs(i,mtrix,visited,stack)==True:
                return True
    return False 

rslt=cycle(mtrix,v) 

if rslt==True:
    otpt.write("Yes")
else:
    otpt.write("No")   

otpt.close()    
inpt.close()
