n=int(input())
arr=[int(i) for i in input().split()]
p1 = max(arr)
arr.remove(p1)
p2 = max(arr)
print(p1*p2)
