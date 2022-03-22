#set (집합)
s1=set([1,2,3])
print(s1)

s2=set("Hello")
print(s2)
#집합 자료형의 특징
#중복을 허용하지 않는다
#순서가 없다 (인덱싱 값을 얻을 수 없다.)

l1=list(s1)
print(l1[0])

l2=tuple(s2)
print(l2[0])

#set 자료형 교집합,합집합,차집합 구할 때 많이 사용
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

#교집합
print(s1 & s2)
#합집합
print(s1 | s2)
print(s1.union(s2))
#차집합
print(s1-s2)
print(s2-s1)
print(s1.difference(s2))
print(s2.difference(s1))

#값 1개 추가하기(add)
s1=set([1,2,3])
s1.add(4)
print(s1)
#값 여러게 추가하기(update)
s1.update([4,5,6])
print(s1)
#특정 값 제거하기(reomve)
s1.remove(2)
print(s1)