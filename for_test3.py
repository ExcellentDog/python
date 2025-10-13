
#제어문 반복문 for - 문자열 리스트변수 range
# 구구단 찍기
'''
print("구구단 2단 출력")
for i in range(1,10):
    print(f"2 x {i} = {2*i}")

#구구단 8단 출력
print("구구단 2단 출력")
for i in range(1,10):
    print(f"8 x {i} = {8*i}")

#구구단 4단 홀수만 찍기
print("구구단 4단 홀수만 출력")
for i in range(1,10,2):
    print(f"4 x {i} = {4*i}")


print("구구단 2단 출력")
for i in range(1,10):
    print(f"2 x {i} = {2*i}")

#중복 for
count = 0
for i in range(1,6):#i 1,2,3,4,5
    #print("i값은",i)
    for j in range(1,6):#j 1,2,3,4,5
        count += 1
        print(count,"hello")

# 구구단 2~9단 찍기
for i in range(2,10):
    print(f"구구단 {i}단 출력")
    for j in range(1,10):
        print(f"{i} x {j} = {i*j}")

for i in range(2,10):
    print()
    for j in range(1,10):
        print(f"{i:>2} x {j:>2} = {i*j:>2}",end = '  ')



#print 포매팅 정렬
name = '서하랑'
print(f"{name:<10}")#왼쪽 정렬
print(f"{name:^10}")#가운데 정렬
print(f"{name:>10}")#오른쪽 정렬

for i in range(1,10):
    print()
    for j in range(2,10):
        print(f"{j:>2} x {i:>2} = {i*j:>2}",end='  ')

for o in range(0,9,3):
    print()
    for j in range(2,10):
        print()
        for i in range(2,5):
            print(f"{i+o:>2} x {j:>2} = {(i+o)*j:>2}",end='    ')

#반복 별찍기
for i in range(1,6):
    print("*"*i)
print()
for i in range(5,0,-1):
    print("*"*i)

for i in range(6,1,-1):
    for j in range(0,i-1):
        print("*",end='')
    print()
'''
for i in range(10):
    print(f"{"*"*i:^10}")












