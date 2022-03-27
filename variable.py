#변수
from re import A, I


a=[1,2,3]
print(id(a)) # a 객체의 주소 값

#리스트 복사
b=a
print(id(a))
print(id(b))
print(a is b)
#주소 값 같음 a와 b가 가르키는 대상은 동일

#b 변수 생성시 a 변수의 값을 가져오면서 a 와는 다른 주소값 가지는 방법
a=[1,2,3]
b=a[:]

from copy import copy
a=[1,2,3]
b=copy(a) #  or b=a.copy()

#변수 바꾸기
i=3
k=5
i,k=k,i
print(i,k)

a="a:b:c:d"
print(a.replace(":","#"))