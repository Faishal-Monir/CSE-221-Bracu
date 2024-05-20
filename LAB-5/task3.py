#Kosaraju SCC
#just change the number after input(EX: input2,input3) and it will show that output accordingly !
#=======================================Input Output=======================================
inpt=open("input/t3/input2.txt","r")
otpt=open("output3.txt","w")
v,e=[int(i) for i in inpt.readline().split()]
#=======================================Logic Part=======================================
a_list=[[] for i in range(v+1)] 
rev_graph=[[] for i in range(v+1)]
final_list=[]

for i in range(e):
    v1,v2=inpt.readline().split( )
    a_list[int(v1)].append(int(v2))
    
stack=[]
def dfs_f(grph,vst,node):
    vst[node]=True
    for a in grph[node]:
        if vst[a]==False:
            dfs_f(grph,vst,a)
    stack.insert(0,node)
 
def dfs_s(r_grph,vst,c_node):
    final_list[-1].append(c_node)
    vst[c_node]=True
    for b in r_grph[c_node]:
        if vst[b]==False:
            dfs_s(r_grph,vst,b)
    

def scc_calc(lst,nodes):
    visited=[False]*(nodes+1)
    for i in range(1,len(lst)):
        if visited[i]==False:
            dfs_f(lst,visited,i)
            
    #graph reversal
    for i in range(len(lst)):
        for j in lst[i]:
            rev_graph[j].append(i)
    
    visited=[False]*(nodes+1)
    stack.sort()
    while stack:
        curr_node=stack.pop(0)
        if visited[curr_node]==False:
            final_list.append([])
            dfs_s(rev_graph,visited,curr_node)
            final_list[-1].sort()
scc_calc(a_list,v)

for i in range(len(final_list)):
    for j in final_list[i]:
        otpt.write(f"{j} ")
    otpt.write("\n")

otpt.close()
inpt.close()    