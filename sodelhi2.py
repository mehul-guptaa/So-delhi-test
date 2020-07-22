#Can be made into any square matrix as per convenience
a = [
    [1,2,3,4] ,
    [4,5,6,7] ,
    [10,8,9,12],
    [25,2,3,7]
    ]

#defining required function
def diagonalDifference (a):
    lrdiagonal=0 #left to right diagonal
    rldiagonal=0 #right to left diagonal
    
    for i in range(len(a)):
        lrdiagonal=lrdiagonal + a[i][i] #a[i][i] represents left to right diagonal elements
        rldiagonal = rldiagonal + a[i][len(a)-1-i] #a[i][len(a)-1-i] represents right to left diagonal elements
    result = abs(lrdiagonal-rldiagonal) #Absolute value of the difference
    return result

print ("The final result is" ,diagonalDifference(a))
