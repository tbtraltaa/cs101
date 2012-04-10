def union(a,b):
    for i in b:
        if i not in a:
            a.append(i)
		
a=[1,2,3]
b=[2,4,6]
union(a,b)

print a
print b
