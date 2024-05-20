import math
from heapq import *
#just change the number after input(EX: input2,input3) and it will show that output accordingly !
#=======================================Input Output=======================================
inpt=open("input/t1/input1.txt","r")
otpt=open("output1_1.txt","w")
vertex,e=[int(i) for i in inpt.readline().split()]
# print(v,e)
#=======================================Logic Part=======================================
lst=[]
for i in range(e+1):
    temp=inpt.readline().split()
    lst.append(temp)
    
start=int(lst.pop(-1)[0])
graph={}

for i in lst:
    u,v,w= i
    u=int(u)
    v=int(v)
    w=int(w)
    if u not in graph:
        graph[u]=[(v,w)]
    else:
        graph[u].append((v,w))
        
def diastra(grph,s):
    distance=[math.inf]*(vertex+1)
    min_heap=[(s,0)]
    visited=set()

    while min_heap:
        v,w=heappop(min_heap)   
        
        if w <distance[v]:
            distance[v]=w 
        if v in visited:
            continue
        visited.add(v)
        if v in graph:
            for n_v , n_w in graph[v]:
                heappush(min_heap,(n_v,n_w+w))
                
    for i in range(1,len(distance)):
        if distance[i]==math.inf:
            distance[i]=-1
    return distance[1:]
    
    
final_list=diastra(graph,start)

for i in final_list:
    otpt.write(str(i)+" ")
otpt.close()    
inpt.close()

     
