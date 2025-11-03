#def_test.py
#함수 일정한 동작을 수행하는 코드의 집합 호출 재사용
#1. 내장함수 print() input() max() range()....
#2. 사용자 정의 함수    내가 만든 함수
#3. 라이브러리 함수 import 해서 사용  turtle random  남이 만든 함수
'''
def hello():
    print("안녕하세요")
    print("인평자동차고등학교")
    print("서하랑입니다.")

hello()

#호출로(Call) 실행 재사용
def hi(name): #매개변수
    print(f"hi~~!!!  {name}!!!")

hi("서하랑")#인수
hi("서하랑")
hi("서하랑")
hi("서하랑")

#두 수를 더하는 함수
def add(x,y):
    print(f"{x} + {y} = {x+y}")

a = int(input("덧셈에 필요한 첫번째 수: "))
b = int(input("덧셈에 필요한 두번째 수: "))
add(a,b)



def 안녕(name1,name2,name3):
    print(f"안녕하세요",name3)
    print(f"안녕하세요",name1)
    print(f"안녕하세요",name2)


안녕("서하랑","하랑","모찌") #인수 3개



#두수를 더하는 계산기
def add(x,y):
    return x+y #반환값

a = int(input("덧셈에 필요한 첫번째 수: "))
b = int(input("덧셈에 필요한 두번째 수: "))
result = add(a,b)
print(f"{a}와 {b}를 더한 값은 {result}입니다.")
'''
#사칙연산 계산기

def add_num(x,y): #덧셈 계산기
    return x+y

def sub_num(x,y): #뺄셈 계산기
    return x-y

def mul_num(x,y): #곱셈 계산기
    return x*y

def div_num(x,y):  #나눗셈 계산기
    return x/y


a = int(input("연산에 필요한 첫번째 수: "))
b = int(input("연산에 필요한 두번째 수: "))

op_code = int(input("연산자를 선택하세요\n1.덧셈\n2.뺄셈\n3.곱셈\n4.나눗셈\n"))
if op_code == 1:
    result = add_num(a,b)
    print(f"정답 = {result}")
elif op_code == 2:
    result = sub_num(a,b)
    print(f"정답 = {result}")
elif op_code == 3:
    result = mul_num(a,b)
    print(f"정답 = {result}")
elif op_code == 4:
    result = div_num(a,b)
    print(f"정답 = {result}")






