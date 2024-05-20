#=======================================Input Output=======================================
inpt=open("input/Task 06/input6_1.txt","r")
otpt=open("output6_3.txt","w")
r,c=[int(i) for i in inpt.readline().split()]
#=======================================Logic Part=======================================
map=[]

for i in range(r):           #reading from the input file and making the map 
    map.append([])
for j in range(r):
    line=inpt.readline()
    for k in line:
        map[j].append(k)
    
    
    
#=====================================            
#Function to print the map !        
def map_print(data):    
    for i in data:
        for j in i:
            print(j,end="")
    print()
# map_print(map)
# print(map) 
#=====================================

def search(ro,col,mp):
    if ro<0 or col<0 or r<=ro or c<=col or mp[ro][col]=="#":            #corner case check 
        return 0 
    if mp[ro][col]=="D":  #If diamond found 1 if not then 0
        temp_count=1
    else:
        temp_count=0
    
    map[ro][col]="#"      #visited flagging 
    # map_print(mp)
    temp_count+=search(ro-1,col,mp) #Upward shift
    temp_count+=search(ro+1,col,mp) #Downwad shift
    temp_count+=search(ro,col+1,mp) #Left shift
    temp_count+=search(ro,col-1,mp) #Right shift
    return temp_count


counter=0

for i in range(r):                        #map or matrix itteration
    for j in range(c):
        if map[i][j]==".":
            diamond=search(i,j,map)
            counter=max(counter,diamond)


otpt.write(str(counter))     #outputting the counter value or the total value of Diamond 

otpt.close()
inpt.close()