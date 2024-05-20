#=======================================Input Output=======================================
inpt=open("input/Task 01/part b/input1b_3.txt","r")
otpt=open("output1b_3.txt","w")
v,e=[int(i) for i in inpt.readline().split()]
#=======================================Logic Part=======================================
dic={}

for i in range(v+1):
    dic.update({i:[]})          #making the empty ad.list

for j in range(e):
    v1,v2,w=inpt.readline().split()
    dic[int(v1)].append((int(v2),int(w)))                     #updating the values in forms of tuple in the ad.list 
    
for a,b in dic.items():                                      #printing the list as output format 
    otpt.write(f"{a} :")
    for c in b:
        otpt.write(f" {c} ")
    otpt.write("\n")
otpt.close()
inpt.close()
    
