list

a=[1,2,3,4,5,['a','b','c']]
b=[9,8,7]

print(a+b)
print(str(b[1])+"people")
a[0]=0
print(a)

del a[0]
print(a)

a.insert(0,1)
print(a)

print(a[-1][1])

print(a[2:6])
print(a[2:6][3][0])
.
.
.
.
.