# 복습
# 이스케이프 코드
'''
food = "Python\'s favorite food is perl"
print(food)
say = "\"Python is very easy.\"he says."
print(say)

# food 변수의 값을 대문자로 출력 p74

print(food.upper())
# say 변수의 값을 소문자로 출력 p74
print(say.lower())

print(say.title())

# 리스트 변수    c언어 배열
#1. 여러개의 값을 저장
#2. 값을 변경 가능

h = ['lee', 17, 172.5, True]
print(h)
print(h[1])
c = h[1]+h[2]
print(c)

h[1] = 25
print(h)


singer = ["카리나", "강해린", "김채원", "우기", "안유진", "얼룩말"]
print(singer)
#append remove 값으로 추가 제거
singer.append("기린") #값을 추가 append()
singer.append("코끼리")
singer.append("코뿔소")
singer.remove("카리나")    #값을 삭제 remove()
singer.remove("우기")
#번지수로 삽입 제거 insert pop
singer.insert(1,"박명수")  #insert 삽입 위치 지정 가능
singer.insert(3,"카더가든")
singer.pop(1)   #pop 번지수로 삭제
print(singer)



fruit = ["사과","망고","키위","귤","딸기","용과"]
print(type(fruit)) #자료형
fruit.append("두리안")
fruit.remove("망고")
fruit.pop(5)
fruit.insert(2,"포도")
print(fruit)
fruit.clear()
print(fruit)
'''
#리슽트변수 인덱싱

sport = ["야구","축구","농구","배구","탁구"]
print(sport)
print(sport[1]) #1번지 값 출구 출력
#축구 농구 배구 출력
print(sport[1:4])
print(sport[0:5:2])
