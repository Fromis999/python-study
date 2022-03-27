#불(bool)자료형이란 참(True)과 거짓(False)를 나타냄
#True False 2가지 값만 가짐

a=True
b=False
print(type(a))
print(type(b))
#<class 'bool'>

#문자열,리스트,튜플,딕셔너리 등의 값이 비어있으면 거짓이된다
print(bool(a)) #true
print(bool([1,2,3])) #true
print(bool(0)) #false
print(bool(2)) #true
