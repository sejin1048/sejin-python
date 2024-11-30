'''
print("hello world!")
print("hello", "Python", 1, 2, "ASDF", sep="\n")
print()
print("1")

print("안녕하세요",end="")
print("코딩온입니다.")
name ='홍길동'
age = 30
print(f"나의 이름은 {name}입니다. 나이는 {age}입니다.")

'''

ive = "I \'AM"
print(ive)

ive = "장원영"
print(ive)
print(f"나는 {ive}입니다.")
print("나는 ",ive,"입니다.",sep='')
print("나는 "+ive+"입니다.")
# my_home : snake_case
# MyHome : CalmelCase <-클래스이름적을때 사용
# myHome : PascalCase
print(type(77))
print(type(7.2))
print(type("ive"))

# print("111 \t222 \t333\n")
# print("111 \n222 \n333")
# print("'111'111")


num=10
b_num=0b1010
h_num=0xA

print(num)
print(b_num)
print(h_num)

print(bin(10))
print(hex(10))

print(ord('0'))
print(ord('A'))
print(chr(48))
print(chr(65))

# a=77
# print(type(a))
# a=7.2
# print(type(a))
# a="ive"
# print(type(a))