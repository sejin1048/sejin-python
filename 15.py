import calc_module

print(calc_module.add(2,3))
print(calc_module.sub(2,3))
print(calc_module.mul(2,3))
print(calc_module.div(2,3))
print("")

from calc_module import add #특정 함수만 가져오는
print(add(2,3))
# calc_module.add(2,3)#안됨
print("")

import calc_module as cm #calc_module대신에 cm으로 쓰겠다. <-중복된 이름이 있을 때 바꾸기!
print(cm.add(2,3))
print(cm.sub(2,3))
print(cm.mul(2,3))
print(cm.div(2,3))

#import math하기
import math
print(math.floor(3.141592))
print(math.ceil(3.141592))
print(math.sqrt(9))
print("")

from math import floor, ceil #math에서 특정 함수만 import한것!
print(floor(3.141592))
print(ceil(3.141592))

# random 모듈
import random
print(random.randint(1,5)) #뒤에꺼 포함됨!
print(random.uniform(1,5)) #뒤에꺼 포함됨!
print(random.random())
print(random.randrange(1,5)) #뒤에꺼 포함안됨!
print(random.randrange(1,5,2)) #뒤에꺼 포함안됨!

#upDown게임
import random

com = random.randint(1, 100)
min_v = 1
max_v = 100
i = 0
count = 100
while i<10:
    i=i+1
    count-=10
    try:
        guess = int(input(f"숫자 입력([{i}회]{min_v} ~ {max_v}): "))
    
        if guess < 0 or guess >100: 
            print("입력 범위를 초과했어요!")
        elif com == guess:
            count = count+10
            print("정답이에요!")
            print(f"정답 : {guess}")
            print(f"점수 : {count}점")
            break
        elif com > guess:
            print("랜덤수보다 작아요!")
            min_v = guess
        else:
            print("랜덤수보다 커요!")
            max_v = guess

    except ValueError:
        print("숫자만 입력가능합니다!")
        

# 실습) 로또 번호 뽑기
import random
a=[]
for i in range(6):
    n = random.randint(1,45)
    while n in a:
        n = random.randint(1,45)
    a.append(n)
    
a.sort()    
print(a)

#datetime 모듈
import datetime
now = datetime.datetime.today()

print(now)
print(now.year, now.month)

print(f"{now.hour}시 {now.minute}분 {now.second}초")

#datetime 모듈 datetime.date했을때
import datetime
now = datetime.date.today()

print(now)
print(now.year, now.month)


# 지나온 날짜 계산하기
import datetime
print("지금까지 몇 일?")
first_day = datetime.date(2024, 11, 25)
print(first_day)

today = datetime.date.today()
print(today)

passed_time = today - first_day
print(passed_time)

print(f"개강 이후 {passed_time.days}일 지났습니다.")
