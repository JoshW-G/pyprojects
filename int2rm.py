rn = {
    1 : 'I',
    4: 'IV',
    5:'V',
    9:'IX',
    10:'X',
    40:	'XL',
    50:	'L',
    90:	'XC',
    100:'C',
    200:'CC',
    300:'CCC',
    400:'CD',
    500:'D',
    600:'DC',
    700:'DCC',
    800:'DCCC',
    900:'CM',
    1000:'M'
    
}

dec = list(rn.keys())

def closestDec(x):
    t = 0 #temp     
    for i in dec:
        if i<x:
            t = i
        elif i==x:
            t = i
            return t
        elif i > x:
             return t  
    

def getRN(x):
    v=closestDec(x) #value
    rnum = rn[v]
    while(x >0):
        x= x - v
        v=closestDec(x)
        if(x<=0):
            break
        else:
            rnum +=  rn[v]
    return rnum  
print(getRN(298))

 
    

