#===========================================
inpt=open("input.txt","r")
otpt=open("output.txt","w")
v,e=[int(i) for i in inpt.readline().split()]

data={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20}

a_list=[[]for i in range(v+1)]

for i in range(e):
    temp=inpt.readline().split("^")
    idx=data[temp[0]]
    a_list[idx].append(temp[1][0])
# print(a_list)

otpt.write(f"Ad.list:\n[")
for i in a_list:
    otpt.write(f"{i}")
otpt.write(f"]\n=======================================")

start=inpt.readline()[0]
start_idx=data[start]

visited=[False]*(v+1)

def bfs(node,counter):
    queue=[node]
    while queue:
        temp=queue.pop(0)
        visited[temp]=counter
        for i in a_list[temp]:
            sub=data[i]
            if visited[sub]==False:
                queue.append(sub)
        counter+=1
        
bfs(start_idx,0)
# print(visited)
visited=visited[1:]

lift1=[]
lift2=[]

for i in visited:
    if i%2==0:
        lift1.append(i)
    else:
        lift2.append(i)
        
otpt.write(f"\nlift1:{lift1}")
otpt.write(f"\nlift1:{lift2}")

otpt.close()
inpt.close()

#This code does not works 100% accurate use at your own risk ! But hey its a good point to start isnt it ?

