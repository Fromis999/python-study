#dictionary

a={1:'hi'}
print(a)
a[2]='bye'
print(a)
a[3]=[1,2,3]
print(a)

del a[3]
print(a)

print(a[1])
print(a.keys())
print(a.values())
print(a.items())
print(a.get(2))

print(1 in a)
