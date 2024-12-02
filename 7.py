#boolean자료형
print(1==2)

x=2
print(1<x<3) # c언어 : (1<x && x>3) ||
print('')

#논리연산자
print(True and False) # &&
print(True or False) # ||
print(not True) # !

#in연산자 중요!
cart=['계란', '마늘', '콩나물', '커피']
print("두부" in cart)
print("계란" in cart)

#if 문 중요!!
if True:
    print("True")
    print("True")
print("False")

#실습3
a = int(input("숫자를 입력하시오:"))
if a%2==0:
    print("짝수")
else:
    print("홀수")

#실습4
#sol1)
score = int(input("점수: "))
if score < 60:
    print("E")
elif score < 70:
    print("D")
elif score < 80:
    print("C")
elif score < 90:
    print("B")
else:
    print("A")

if score > 100:
    print("만점은 100점 입니다. 다시 점수를 입력해주세요!")

#sol2)
score = int(input("점수: "))
if score < 60:
    print("E")
elif score < 70:
    print("D")
elif score < 80:
    print("C")
elif score < 90:
    print("B")
elif score <101:
    print("A")
else:
    print("만점은 100점 입니다. 점수를 입력해주세요!")

#실습5
age = int(input("나이를 숫자로 입력해 주세요: "))
pay = input("결제 방법을 입력해 주세요. ('카드' 또는 '현금'만 입력) ")

if age < 8:
    if pay == '카드': 
        print(f"{age}세의 {pay} 요금은 무료 입니다.")

elif age < 14:
    if pay == '카드':
        print(f"{age}세의 {pay} 요금은 450원 입니다.")
    
elif age < 20:
    if pay == '카드':
        print(f"{age}세의 {pay} 요금은 720원 입니다.")
    elif pay == '현금':
        print(f"{age}세의 {pay} 요금은 1000원 입니다.")
        
elif age < 75:
    if pay == '카드':
        print(f"{age}세의 {pay} 요금은 1200원 입니다.")
    elif pay == '현금':
        print(f"{age}세의 {pay} 요금은 1300원 입니다.")

else:
    if pay == '카드':
        print(f"{age}세의 {pay} 요금은 무료 입니다.")    