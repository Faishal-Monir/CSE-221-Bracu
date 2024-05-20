#1-->b
inpt=open("input1b.txt","r")
otpt=open("output1b.txt","w")

rd=inpt.readline()
d=int(rd)
for i in range (d):
    temp=inpt.readline()
    calc=temp.split( )

    if calc[2]=="+":
        temp1=int(calc[1])+int(calc[3])
        otpt.write(f"The result of {calc[1]} {calc[2]} {calc[3]} is {temp1}\n")

    elif calc[2]=="-":
        temp1=int(calc[1])-int(calc[3])
        otpt.write(f"The result of {calc[1]} {calc[2]} {calc[3]} is {temp1}\n")

    elif calc[2]=="*":
        temp1=int(calc[1])*int(calc[3])
        otpt.write(f"The result of {calc[1]} {calc[2]} {calc[3]} is {temp1}\n")

    else:
        temp1=int(calc[1])/int(calc[3])
        otpt.write(f"The result of {calc[1]} {calc[2]} {calc[3]} is {temp1}\n")
        
otpt.close()
inpt.close()

#_______________________Code-Explanation_____________________________________
""" 
For this code we read the firt input file and took the range of loop from the first line ('15').Then type converted the value
to an integear and used that number (15) in the loop range. For each loop we used .split( ) to split the remaining lines by space and get 
a list and use indexing to check the operator signs and do the calculations by that given instruction. Lastly after each calculations we
wrote the output in the certain format in the output file and at the very last closed the file. 
"""