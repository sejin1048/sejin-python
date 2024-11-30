song = input("너의 최애 노래는?")
print(song)
print(type(song))

a=input("1+1=?")
print(int(a)*2) #문자랑 숫자랑 더하거나 빼지 못함!
a=int(intput())

ff = float(input())
print(ff)

a=2
print(str(a)*10)
print(str(a)+" 입니다.")

#실습2 개 출력하기
print('|\_/|')
print('|q p|\t/}')
print('( 0 )"""\\')
print("|\"^\'\t |")
print("||_/=\\\__|")

#실습3 입출력 실습
#1번
print("<1번 문제>")
name=input("이름을 입력하세요.")
age=int(input("나이를 입력하세요."))
print(f"안녕하세요! {name}님 ({age}세)\n")

#2번
print("<2번 문제>")
name=input("이름을 입력하세요.")
birth=int(input("태어난 년도를 입력하세요."))
year=int(input("올해 년도를 입력하세요."))
print(f"올해는{year}년,{name}님의 나이는 {year-birth+1}세 입니다.")
