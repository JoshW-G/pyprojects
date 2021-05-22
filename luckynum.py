#nums with 6 or 8 are lucky, 6 and 8 are not

L, H = 1, 100
cnt = 0
for i in range(L,H+1):
    val = str(i)
    is6 = val.find("6")
    is8 = val.find("8")
    
    if(is6 == 0 and is8 == 0):
        continue
    if(is6 == 0 and is8 == -1):
        cnt +=1
    if(is8 == 0 and is6== -1):
        cnt +=1
print(cnt)