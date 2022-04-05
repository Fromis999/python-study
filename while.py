#while

from ast import Add, Del
from typing import List


treeHit=0
while treeHit<10:
    treeHit=treeHit+1
    print("나무를 %d번 찍었습니다" %treeHit)
    if treeHit ==10:
        print("나무 넘어갑니다")
#나무 1~10번 이후 if문 실행 while문 탈출

#break
coffee=10
money=300
while money:
    print("돈을 받았으니 커피를 줌")
    coffee=coffee-1
    print("커피 잔여량 %d" %coffee)
    if coffee==0:
        print("커피 없음")
        break

#continue
a=0
while a<10:
    a=a+1
    if a % 2==0: continue
    print(a)

#무한루프
while True:
    print("Ctrl+c를 눌러야 while문을 나갑니다")

