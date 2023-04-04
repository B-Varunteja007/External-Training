f,p1,p2=map(int,input().split())
def prime(n):
    lower=p1
    upper=p2
    for  i in range(lower,upper+1):
        if i>0:
            for j in range(2,i):
                if(i%j==0):
                    break
            else:
                print(i)
