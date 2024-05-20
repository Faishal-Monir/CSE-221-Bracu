#just change the number after input(EX: input2,input3) and it will show that output accordingly !
#=======================================Input Output=======================================
inpt=open("input/t1/input1.txt","r")
otpt=open("output1_A.txt","w")
v,e=[int(i) for i in inpt.readline().split()]
# print(v,e)
#=======================================Logic Part=======================================
a_list=[[] for i in range(v+1)] 

for i in range(e):
    v1,v2=inpt.readline().split( )
    a_list[int(v1)].append(int(v2))
    
def dfs(node,visit,stack,grph,c_n):
     visit[node]=True   
     c_n[node]=True
       
     for subelem in grph[node]:
         if visit[subelem]==False: 
             if dfs(subelem,visit,stack,grph,c_n)==True:
                 return True
         if c_n[subelem]==True:
             return True
     c_n[node]=False           
     stack.insert(0,node)  

stack=[]
def topo_sort(Main,lst):   
    currentnode=[False]*len(lst)
    visited=[False]*len(a_list)        
    for elem in range(1,len(lst)):
        if visited[elem]==False:
             if dfs(elem,visited,Main,lst,currentnode)==True:
                 return True
    return False

if topo_sort(stack,a_list)==True:
    otpt.write("IMPOSSIBLE")
else:
    for a in stack:
        otpt.write(str(a)+" ")  

otpt.close()
inpt.close()      