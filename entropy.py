import math 
from collections import Counter

def entropy():
#open the file
    f = open('yourfilepath', 'r')          
    #digits = np.loadtxt('yourfilepath', dtype = np.str)
    
    digits = f.readline()
    #Tdigits = digits.T
    #count0 = 0
    #prob0 = 0

#loop to count digits in the file
    for numCount in digits:                     
        numCount = Counter(digits)
            
#count total number of digits 
    total = (numCount['0'] + numCount['1'] + numCount['2'] + numCount['3'] + numCount['4']
     + numCount['5'] + numCount['6'] + numCount['7'] + numCount['8'] + numCount['9'])
    
#calculate individual probablity
    prob0 = numCount['0']/ float(total)
    prob1 = numCount['1']/ float(total)
    prob2 = numCount['2']/ float(total)
    prob3 = numCount['3']/ float(total)
    prob4 = numCount['4']/ float(total)
    prob5 = numCount['5']/ float(total)
    prob6 = numCount['6']/ float(total)
    prob7 = numCount['7']/ float(total)
    prob8 = numCount['8']/ float(total)
    prob9 = numCount['9']/ float(total)
    
    #totProb = float(prob0 + prob1+ prob2 + prob3 + prob4 + prob5 + prob6 + prob7 + prob8 + prob9)    
   
#    print prob0    
#    print prob1
#    print prob2
#    print prob3
#    print prob4
#    print prob5
#    print prob6
#    print prob7
#    print prob8
#    print prob9
    
# find the entropy
# H = -Σ p(i) log2 p(i)
    H = -((prob0 * math.log(prob0,2)) + (prob1 * math.log(prob1,2)) + (prob2 * math.log(prob2,2))
     + (prob3 * math.log(prob3,2)) + (prob4 * math.log(prob4,2)) + (prob5 * math.log(prob5,2))
     + (prob6 * math.log(prob6,2)) + (prob7 * math.log(prob7,2)) + (prob8 * math.log(prob8,2))
     + (prob9 * math.log(prob9,2)))

    print H
#    print round(H)

entropy()
