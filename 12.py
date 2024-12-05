# 함수
def f(x):
    result = x**2 + 2*x + 1
    return result

print(f(3))

# 매개변수도 없고 return도 없는 내가 만든 함수
def sayHi():
    print("Hi")
    print("Hi")
    print("Hi")

sayHi()

# 전역변수 지역변수
x = 10 #전역변수 -> 밑에 부분 전부다 동작한다!
def func():
    x = 20 #지역변수
    print("func",x)

func()
print("main",x)

def func2():
    print("func2",x)
    
func2()

def func3(x):
    print("func3",x)
func3(3)

# 실습 1
def func(x,y):
    if x == y:
        total = print(f"결과(곱): {x*y}")
    else: 
        total = print(f"결과(합): {x+y}")

func(2,2)
func(2,3)

# 실습 2
# sol1)
def total(price,num):
    total_price = price * num
    if total_price < 20000:
        total_price += 2500
        print(f"상품2 가격: {total_price}원")
    else:
        print(f"상품1 가격: {total_price}원")

total(100,300)
total(100,150)

# sol2)
def price(x,y):
    if x*y<20000:
        val = x * y+2500
    else:
        val = x * y
    return val

# a = int(input("상품 금액 입력: "))
# b = int(input("상품 수량 입력: "))
# print(f"총 가격 : ",price(a,b))

a = list(map(int,input().split()))
if len(a)<3:
    print(f"총 가격 : ",price(a[0],a[1]))
else:
    print("2개만 입력하세요!")

# 리스트 전달
def times(l):
    l2 =  [i*2 for i in l]
    return set(l2)

v2 = times([1,2,3,4,5])
print(v2)
     
# return 2개 할 수 있다! c언어에서는 안됨!
def sum_mul(a,b):
    sum = a+b
    mul = a*b
    return sum,mul

s, m = sum_mul(2,3)
print(s,m)

# 실습3 자판기 프로그램 함수화

#남은 음료수 확인 함수
def check_machine():
    print("남은 음료수: ",vending_machine)

# 음료수가 있는지 확인 함수
def is_drink():
    if drink in vending_machine:   
        print(f"{drink} 드릴게요")
        vending_machine.remove(drink)
        print("남은 음료수: ",vending_machine)
    else:
        print(f"{drink}는 지금 없네요")

# 음료수를 추가하는 함수
def add_drink():
        print("남은 음료수: ",vending_machine)
        print('')
        add=input("추가할 음료수? ")
        vending_machine.append(add)
        vending_machine.sort()
        print("추가 완료")
        print("남은 음료수: ",vending_machine)

# 음료수 제거하는 함수
def remove_drink():
        print("남은 음료수: ",vending_machine)
        delete=input("삭제할 음료수? ")
        if delete in vending_machine:
            vending_machine.remove(delete)
            print("삭제 완료")
            print("남은 음료수: ",vending_machine)
        else:
            print(f"{delete}는 지금 없네요")
    
#3 자판기 프로그램 응용
vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']
check_machine()

user = input("사용자 종류를 입력하세요:\n1.소비자\n2.주인\n")
if user == '1' or user == '소비자':
    drink=input("마시고 싶은 음료? ")
    is_drink()
    
elif user == '2' or user == '주인':
    select = input("할 일 선택:\n1.추가\n2.삭제\n")
    if select == '1' or select == '추가':
        add_drink()
        
    elif select == '2' or select == '삭제':
        remove_drink()
    else:
        print("추가 또는 삭제를 선택해주세요.")
else:
    print("소비자 또는 주인 두가지 종류로만 입력해 주세요!(번호 또는 값 입력)")
    
# 실습4
import sys 
line = int(sys.stdin.readline())
stack = []

def push(p):
    stack.append(p)
    
def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)
        
def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
# # sol1
# for i in range(line+1):
#     func = sys.stdin.readline().split()
    
#     if func[0] == 'push':
#         push(int(func[1]))
#     elif func[0] == 'pop':
#         pop()
#     elif func[0] == 'size':
#         size()
#     elif func[0] == 'empty':
#         empty()
#     elif func[0] == 'top':
#         top()
    
#sol2
for i in range(line):
    func = sys.stdin.readline().split()
    fnc = func[0]
    match fnc:
        case 'push':
            push(int(func[1]))
        case 'pop':
            pop()
        case 'size':
            size()
        case 'empty':
            empty()
        case 'top':
            top()            
        
# 전역변수(global) 파이썬은 선언과 할당이 동시에 일어나기때문에...
def oneUp():
    global x #전역변수임
    x += 1
    return x
x = 0
print(oneUp())
print(oneUp())
print(oneUp())

#실습5
def get_times(n):
    global count
    for i in range(1,31):
        if i%n == 0:
            count += 1
            print(f"{i}",end=" ")
    return count
count = 0
n = 3

print(f"\n3의 배수의 개수: {get_times(n)}")
