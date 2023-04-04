lst=[5,9,8,7,99,1,5699]
lst.sort()
n=len(lst)
mp=dict()
for i in range(n):
    if lst[i] in mp:
        mp[lst[i]]+=1
    else:
        mp[lst[i]]=1
for x in mp:
    print(x,"->",mp[x])
