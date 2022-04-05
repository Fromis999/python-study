test_list=['one', 'two', 'three']
for i in test_list:
    print(i)
# one two three 
# for문은 자동으로 처음부터 증가한 값까지 보여줌

a=[(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)
#3 7 11

marks=[90, 25, 67, 45, 80]
number=0
for mark in marks: #marks에서 차례로 하나씩 점수를 꺼내 mark에 대입
    number=number+1
    if mark>=60:
        print("%d번 학생은 합격입니다" % number)
    else:
        print("%d번 학생은 불합격입니다." %number)
# 합격 불합격 합격 불합격 합격

# continue
marks=[90,25,67,45,80]
number=0
for mark in marks:
    number=number+1
    if mark<60:
        continue
    print("%d번 학생 합격입니다." %number)
# 1, 3, 5번 합격

# range 합수 같이 쓰기
add=0
for i in range(1,11): # range(10)이랑 같음 0~9까지
    add=add+1
    print(add)

marks=[90,25,67,45,80]
for number in range(len(marks)):
    if marks[number]<60:
        continue
    print("%d번 합격" %(number+1)) # number가 0부터 시작

#리스트 내포 사용
a=[1,2,3,4]
result=[num*3 for num in a]
print(result)
# [3, 6, 9, 12]

#리스트 내포안에 조건문
a=[1,2,3,4]
result=[num*3 for num in a if num % 2 ==0] #짝수만 곱하기
print(result)
# [6, 12]

