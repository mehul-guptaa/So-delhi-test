#defining required function
def countingvalleys(a):
    downcount =0 #steps downward
    upcount=0 #steps upward
    val=0 #valleys traversed

    #iterate over the array
    for i in a:
        if i=='D':
            downcount +=1
            
            if downcount - upcount == 1: #only check on a down step to ensure a new valley is being entered and not an already entered valley being exited
                val +=1                
        else:
            upcount +=1
            
    return val

x=input("Enter the list:")

#creating interactable list and removing extra elements
y = list(x) 
y.remove('[')
y.remove(']')
a = y.count(',')
for i in range(a):
    y.remove(',')


print("The number of valleys traversed through =" , countingvalleys(y))
