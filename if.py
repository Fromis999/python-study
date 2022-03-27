#if
money=2000
card=True
if money>=3000 or card:
    print("택시 타고가기")
else:
    print("걸어가기")

# x in s, x not in s
print(1 in [1,2,3]) #True
print(1 not in [1,2,3]) #False


pocket=['paper','cellphone','money']
if 'money' in pocket:
    print("택시를 타고 가라") # pass 라하면 결과값 반환 X
else:
    print("걸어가라")
#else if 대신 elif 가능

