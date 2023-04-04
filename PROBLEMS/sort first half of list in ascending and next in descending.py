lst=[9,0,5,6,7,3,2,1,99]
n=len(lst)
lst.sort()
for i in range(n//2):
    print(lst[i],end=" ")
print("_____________________________________")

for j in range(n-1,(n//2)-1,-1):
    print(lst[j],end=" ")