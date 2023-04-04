lst=[5,2,4,3,1]
n=len(lst)
print("THE ORIGINAL LIST IS")
for i in range(n):
    print(lst[i],end=" ")
print(("----------------------------------------"))
#Method for circular rotation
x=lst[n-1]
for i in range(n-1,0,-1):
    lst[i]=lst[i-1]
lst[0]=x
print("AFTER CIRCULAR ROTATION LIST IS:")

for i in range(n):
    print(lst[i],end=" ")







