#=======================================Input Output=======================================
inpt=open("input/t3/input2.txt","r")
otpt=open("output3_2.txt","w")
v,e=[int(i) for i in inpt.readline().split()]
# print(v,e)
#=======================================Logic Part=======================================
links=[]
for i in range(e):
    temp=[int(i) for i in inpt.readline().split()]
    links.append( tuple(temp) )


parent=[i for i in range(v+1)]
final_lst=[]

def counter(val,parent):
    return parent.count(val)

def parent_changer(child,parent,parent_list):
    for i in range(len(parent_list)):
        if parent_list[i]==child:
            parent_list[i]=parent
    return parent_list
        

def union(relations,parent):
    for n1,n2 in relations:
        if parent[n1]==parent[n2]:
            final_lst.append(counter(parent[n1],parent))
            continue
        
        changed=None
        
        if parent[n1]==n1 and parent[n2]==n2:
            parent=parent_changer(parent[n2],parent[n1],parent)
            if parent[n1]==n1:
                changed=parent[n1]
            else:
                changed=parent[n2]
                
        else:
            c1=counter(parent[n1],parent)
            c2=counter(parent[n2],parent)
            if c1>c2:
                parent=parent_changer(parent[n2],parent[n1],parent)
                changed=parent[n1]
            else:
                parent=parent_changer(parent[n1],parent[n2],parent)
                changed=parent[n2]
        
        final_lst.append(counter(changed,parent))
    
union(links,parent)

# print(final_lst)
for i in final_lst:
    otpt.write(f"{i}\n")

otpt.close()
inpt.close()



