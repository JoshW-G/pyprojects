
times = ["10:40:35" , "03:40:35", "03:40:36" ]

bestHr = 24
bestMin = 60
bestSec = 60
best = ""
for i in times:
    hr =int(i[:2]) 
    mn =int(i[3:5]) 
    sc =int( i[6:] )
    if(hr < bestHr):
        bestHr, bestMin , bestSec = hr, mn, sc
        best = i
    elif(hr == bestHr):
        if(mn<bestMin):
           bestHr, bestMin , bestSec = hr, mn, sc
           best = i 
        elif(sc < bestSec):
            bestHr, bestMin , bestSec = hr, mn, sc
            best = i 
print(best)