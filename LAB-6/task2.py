#just change the number after input(EX: input2,input3) and it will show that output accordingly !
import math
from heapq import *
#=======================================Input Output=======================================
inpt=open("input/t2/input3.txt","r")
otpt=open("output2_3.txt","w")
vertex,e=[int(i) for i in inpt.readline().split()]
# print(vertex,e)
#=======================================Logic Part=======================================
lst=[]
for i in range(e+1):
    temp=inpt.readline().split()
    lst.append(temp)
    
source1,source2=lst.pop(-1)
source1,source2=int(source1),int(source2)

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
                
    return distance
    
    
source1list=diastra(graph,source1)
source2list=diastra(graph,source2)

time,place=math.inf,math.inf


for i in range(0,vertex+1):
    maximum_time=max(source1list[i],source2list[i])
    if maximum_time<time:
        time=maximum_time
        place=i

if time==math.inf and place==math.inf:
    otpt.write("Impossible")
else:
    otpt.write(f"Time {time}\nNode {place}")

otpt.close()
inpt.close()    
        