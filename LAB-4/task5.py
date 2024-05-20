#=======================================Input Output=======================================
inpt=open("input/Task 05/input5_2.txt","r")
otpt=open("output5_1.txt","w")
v,e,d=[int(i) for i in inpt.readline().split()]
#=======================================Logic Part=======================================
a_list=[[] for i in range(v+1)] 

for i in range(e):
    v1,v2=inpt.readline().split( )
    a_list[int(v1)].append(int(v2))
    a_list[int(v2)].append(int(v1))    

queue=[[1]]             #initially staring from vertex 1
visit_history=[]

def bfs(lst,que,visited,des):     #Modified bfs code to find the shortest path 
    start=que[0]
    if start[0]==des:
        return start
    while que!=[]:
        way=que.pop(0)
        elem=way[-1]
        if elem not in visited:
            visited.append(elem)
            for sub_elem in lst[elem]:
                path_his=list(way)
                path_his.append(sub_elem)
                que.append(path_his)
                # print("PATH_his",path_his)#
                if sub_elem==des:
                    return path_his
step=bfs(a_list,queue,visit_history,d)



otpt.write(f"Time: {len(step)-1}\nShortest Path:")
for i in step:
    otpt.write(f" {i} ") 
    
otpt.close()
inpt.close()