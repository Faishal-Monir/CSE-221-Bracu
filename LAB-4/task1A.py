#=======================================Input Output=====================================
inpt=open("input\Task 01\part a\input1a_2.txt","r")
otpt=open("output1a_2.txt","w")
v,e=[int(i) for i in inpt.readline().split()]

matrix=[[0]*(v+1) for i in range(v+1)] # building the empty matrix
#=======================================Logic Part=======================================


#====In-code-Matrix printer============            
def matrix_printer(data):    
    for i in data:
        for j in i:
            print(j,end=" ")
        print()
#=====================================

for i in range(e):     
    v1,v2,w=inpt.readline().split( )          #reading the line and inserting the values in the matrix 
    matrix[int(v1)][int(v2)]=int(w)
    
# matrix_printer(matrix)

for i in matrix:                      #output file printing
    for j in i:
        otpt.write(str(j)+" ")
    otpt.write("\n")
otpt.close()
inpt.close()