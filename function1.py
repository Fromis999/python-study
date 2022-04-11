#함수 구조
''' def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장2>
    ...
'''
def add(a,b):  # a, b는 매개변수(함수에 입력으로 전달된 값을 받는 변수)
    return a+b
a=3
b=4
print(add(a,b)) # a, b는 인수(함수를 호출할 때 전달하는 입력값)

#일반적인 함수 - 입력값이 이고 결괏값이 있는 것
def add(a,b):
    result=a+b
    return result
a=add(3,4) # 결괏값을 받을 변수 = 함수이름(입력인수1, 입력인수2...)-사용법
print(a)

#입력값이 없는 함수
def say():
    return 'Hi'
a=say() # 결괏값을 받을 변수 = 함수이름() -사용법
print(a) # Hi

#결괏값이 없는 함수 (return 값이 없음)
def add(a, b):
    print("%d, %d의 합은 %d입니다." %(a,b,a+b))

add(3,4) # 함수이름(입력인수1, 입력인수2,...) - 사용법
a=add(3, 4) # 3, 4의 합은 7입니다.
print(a) # None 결과값이 없기때문에

# 입력값도 결괏값도 없는 함수
def say():
    print('Hi')
say() # 함수이름() - 사용법

#매개변수 지정하여 호출하기
def add(a,b):
    return a+b
result=add(a=3, b=7)
print(result)

result=add(b=5,a=3) # 매개변수 순서에 상관없이 가능 (장점)
print(result)

#입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까
'''
def 함수이름(*매개변수):
    <수행할 문장>
    ...
'''
def add_many(*args): # 입력값이 몇 개이든 * 붙이면 전부 모아 튜플로 만들어줌
    result=0
    for i in args:
        result = result + i
    return result
result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice, *args):
    if choice == "add": # choice 매개변수가 add면 뒤에 값 전부 덧셈
        result =0
        for i in args:
            result=result + i
    elif choice == "mul": # choice 매개변수가 mul면 뒤에 값 전부 곱셈
        result=1
        for i in args:
            result = result * i
    return result

result=add_mul('add',1,2,3,4,5)
print(result) #15
result=add_mul('mul',1,2,3,4,5)
print(result) #120

# 키워드 피라미터 kwargs
def print_kwargs(**kwargs): # 매개변수 이름 앞에 **를 붙이면
    print(kwargs)           # 매개변수 kwargs는 딕셔너리가 되고
print_kwargs(a=1)           # 모든 key=value 형태의 결괏값이 딕셔너리에 저장
# {'a':1}
print_kwargs(name='foo',age=3)
#{'age':3,'name':'foo'}