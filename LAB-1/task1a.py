#1-->a
inpt=open("input1a.txt","r")
otpt=open("output1a.txt","w")

c=int(inpt.readline())

for i in range (c):
    temp=inpt.readline()
    n=int(temp)
    if n%2==0:
        otpt.write(f"{n} is an Even number.\n")
    else:
        otpt.write(f"{n} is an Odd number.\n")
otpt.close()
inpt.close()

#_______________________Code-Explanation_____________________________________
"""
For this code we have opened the input file then took the range of the loop from line 1 by using readline( ). 
Then we ran the loop that amount of times and took the values every time also checked whether the number is even or odd.
lastly we wrote the output in the output file. and closed the file by using .close( ) at the very end.
"""

