

def covariance(X,Y):
    n = len(X)
    Xmean= 0
    Ymean=0
    for i in range(n):
        Xmean = Xmean + X[i]
        Ymean = Ymean + Y[i]
        
    Xmean = Xmean/(n)
    Ymean = Ymean /(n)
    cov=0
    for i in range(n):
        cov = cov+ (X[i] - Xmean)*(Y[i]- Ymean)

    cov = cov/(n-1)
    return cov


x= [4,2,5,1]
y = [1,3,4,0]

print("cov(x,x):",covariance(x,x))
print("cov(x,y):",covariance(x,y))

print("cov(y,y):",covariance(y,y))
print("cov(y,x):",covariance(y,x))
