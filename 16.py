f = open("text.txt","w")
f.write("Hi\n")
# input("멈춰")
f.close()

f = open("text.txt","a")
f.write("addtion\n")
f.close()

f3 = open("text.txt")
print(f3.read())
f3.close()

f4 = open("text.txt")
print(f4.readline(), end="")
print(f4.readline(), end="")
print(f4.readline(), end="")
f4.close()

# readlines()
f4 = open("text.txt")
print(f4.readlines())
f4.close()

#중요!
f5 = open("text.txt","r+")
print(f5.read())
print(f5.tell())
f5.seek(4)
print(f5.write("8"))
f5.close()

#위치를 모를때 find쓰기
f6 = open("text.txt","r+")
str6 = f6.read()
print(f6.tell())
f6.seek(str6.find('5'))
print(f6.write("8"))
f6.close()

# with ~ as 구문 
with open("text.txt","r+") as f7:
    str7 = f7.read()
    print(f7.tell())
    f7.seek(str7.find('4'))
    print(f7.write("8"))

# 영어 타자연습 프로그램
import random

with open("word.txt", 'w') as f:
    word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple', 'grape',
            'garlic', 'onion', 'potato']
    for i in word:
        f.write(i + ' ')# \n , \t, \r, ' ' 가능

with open("word.txt", 'r') as f:
    data = f.read().split()
    # data = f.readlines() # \n인 경우에 이렇게도 가능
    word = random.choice(data)
    print(word)
    

# 
import sys

with open("./output/input.txt",'a') as f:
    while True:
        text = input("저장할 내용 입력(종료-z)")
        if text == 'z' or text == 'Z':
            break
        f.write(text + '\n')
        
        
# 실습 3) 회원 명부 작성하기
with open("member.txt",'w') as f:
    for i in range(3):
        name = input("이름을 입력하시오 : ")
        pw = input("비밀번호를 입력하시오 : ")
        f.write(f"{name} {pw}\n")
      
with open("member.txt",'r') as f:
    print(f.read())
    
# 실습 4) 로그인
with open("member.txt",'a') as f:
    while True:
        name = input("이름을 입력하시오 : ")
        pw = input("비밀번호를 입력하시오 : ")
        f.write(f"{name} {pw}\n")

# 로그인
new_name = input("이름을 입력하세요 : ")
new_ps = input("비밀번호를 입력하세요 : ")

with open("member.txt",'r') as f:
    find = False
    for i in f:
        id,ps = i.split()
        if id == new_name and ps == new_ps:
            print("로그인 성공")
            find = True
            break
    if not find:
        print("로그인 실패")


#로그인 dict ver)
dictUser = {}

with open("member.txt",'r') as f:
    for line in f:
        id,ps = line.split()
        dictUser[id] = ps
        
print(dictUser) 

new_name = input("이름을 입력하세요 : ")
new_ps = input("비밀번호를 입력하세요 : ")

if new_ps == dictUser.get(new_name):
    print("로그인 성공")

else:
    print("로그인 실패!")

#dict ver) 로그인 성공 시 전화번호
dictUser = {}

with open("member.txt",'r') as f:
    for line in f:
        id,ps = line.split()
        dictUser[id] = ps
        
print(dictUser) 

new_name = input("이름을 입력하세요 : ")
new_ps = input("비밀번호를 입력하세요 : ")

if new_ps == dictUser.get(new_name):
    print("로그인 성공")
    if id == new_name and ps == new_ps:
        print("로그인 성공")
        with open("member_tel.txt",'w') as f:
            tel = input("전화번호를 입력하세요 : ")
            f.write(f"{new_name} {tel}")
else:
    print("로그인 실패!")


# 로그인 성공 시 전화번호 입력
import os

new_name = input("이름을 입력하세요 : ")
new_ps = input("비밀번호를 입력하세요 : ")

with open("member.txt", 'r') as f:
    find = False
    for i in f:
        id, ps = i.split()
        if id == new_name and ps == new_ps:
            print("로그인 성공")
            find = True
            
            tel = input("전화번호를 입력하세요 : ")
            lines = []
            
            if os.path.exists("member_tel.txt"):
                with open("member_tel.txt", 'r') as f_tel:
                    lines = f_tel.readlines()
            
            with open("member_tel.txt", 'w') as tel_file:
                updated = False
                for line in lines:
                    if line.strip():
                        existing_name, existing_tel = line.split()
                        
                        if existing_name == new_name:
                            tel_file.write(f"{new_name} {tel}\n")
                            updated = True
                        else:
                            tel_file.write(line)
                
                if not updated:
                    tel_file.write(f"{new_name} {tel}\n")      
                    
            break
    
    if not find:
        print("로그인 실패")

#바이너리 파일 읽고 쓰기 <- 인코딩과 디코딩은 쌍으로 해야함
with open("./output/data.bin","wb") as f:
    txt = "안녕"
    f.write(txt.encode()) # 반드시 인코딩을 해서 써야한다!
        
with open("./output/data.bin","rb") as f:
    data = f.read()
    print(data)
    print(data.decode()) #인코딩을 했으므로 디코딩 해서 쓴다

# 바이너리 파일 읽고 쓰기
with open('img1.jpg','rb') as f1:
    img = f1.read()

with open('./output/img1.jpg','wb') as f2:
    f2.write(img)
        
        
# 에러와 예외 처리
try : 
    num = int(input("정수입력 : "))
    
except :
    print("정수가 아님!")

try : 
    num = int(input("정수입력 : "))
    
except ValueError as msg:
    print(msg)

try : 
    num = int(input("정수입력 : "))
    print(f"입력된 정수는 : {num}")
    
except Exception as msg: # 최상단에 있는 Exception만 외우면 된다!
    print(msg)

# 다중 예외 처리 #먼저 만나는 것 중 해당하는 애가 실행됨!
try :
    num = int(input("정수입력 : "))
    
except IndexError as msg :
    print("IndexError", msg) 

except ValueError as msg :
    print("ValueError", msg)

except Exception as msg :  # Exception을 가장 마지막에 배치해 주는것이 좋다!
    print("Exception", msg) 
else:
    print("예외없음")   

#실습) 정수 입력 받기
state = True
while state:
    try:
        num = int(input("숫자 입력 : "))
        print(f"정수 입력 성공 : {num}")
        state = False
    except Exception:
        print("정수가 아님! 정수를 다시 입력해 주세요!")
    finally:
        print("무조건 무조건이야")
        
# raise~exception구문 참고 <-raise하여 어디서 에러가 났는지 찾아볼 수 있다!
a = 1
try: 
    a += 1
    if a > 1:
        raise Exception # raise하면 무조건 except로 빠지는 것이다!
    a+=2
    print("a",a)
except:
    print("error",a)

# raise~exception구문
class Animal:
    def breathe(self):
        print("숨을 쉰다")
    def cry(self):
        raise NotImplementedError #<- 오버라이드 해서 쓰라는 말임! 안하면 에러 발생 시키겠다는 뜻 또는 까먹지 말라고 쓰는 것임!

class Dog(Animal):
    def cry(self):
        print("멍멍")

d = Dog()
d.breathe()
d.cry()        
    