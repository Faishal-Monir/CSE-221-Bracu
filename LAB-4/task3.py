#=======================================Input Output=======================================
inpt=open("input/Task 03/input3_1.txt","r") 
otpt=open("output3_2.txt","w")
v,e=[int(i) for i in inpt.readline().split()]
#=======================================Logic Part=======================================
mtrix=[[] for i in range(v+1)]   #Empty matrix 
final_lst=[]                     #Final path of the traversal 

for i in range(e):
    v1,v2=inpt.readline().split( )      #assigning values to the undirected and unweighted matrix or graph
    mtrix[int(v1)].append(int(v2))
    mtrix[int(v2)].append(int(v1))    
print(mtrix)                       

visited=[False]*len(mtrix)            # global visited list 

def dfs(lst,s,history,rslt):          # almost recursive search but the end case is list is empty
    history[s]=True
    rslt.append(s)
    
    for i in lst[s]:
        if history[i]==False:
            dfs(lst,i,history,rslt)
    
    
dfs(mtrix,1,visited,final_lst)

for i in final_lst:                 
    otpt.write(str(i)+" ")
otpt.close()    
inpt.close()
    