lst=[0,8,5,3,7,9]
n=len(lst)
print(lst[::-1])
l=[]
for j in range(n-1,0,-1):
    l.append(j)
print(l[j],end=" ")
"""for j in range(n-1,(n//2)-1,-1):
    print(lst[j],end=" ")"""