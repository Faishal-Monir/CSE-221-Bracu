#Kruskal
#=======================================Input Output=======================================
inpt=open("input/t4/input1.txt","r")
otpt=open("output4_1.txt","w")
v,e=[int(i) for i in inpt.readline().split()]
# print(v,e)
#=======================================Logic Part=======================================
path=[]
parentlst=[i for i in range(v+1)]

for i in range(e):
    u,v,w=[int(i) for i in inpt.readline().split()]
    path.append((u,v,w))

def parent_finder(val):
    if parentlst[val]==val:
        return parentlst[val]
    parentlst[val]=parent_finder(parentlst[val])
    return parentlst[val]

def beluga_roads(grph,n):
    grph.sort(key=lambda x:x[2])
    cost=0
    for i in grph:
        p_u=parent_finder(i[0])
        p_v=parent_finder(i[1])
        
        if p_u!=p_v:
            parentlst[p_v]=p_u
            cost+=i[2]
    return cost
    
    
    
    
temp=beluga_roads(path,e)
otpt.write(f"{temp}")

otpt.close()
inpt.close()


