# while문
i=0
while i<5:
    i += 1
    print(i)
print("끝")

# continu문 홀수만 출력하기
num = 0
while num < 10:
    num += 1
    if num%2 == 0:
        continue
    print(num)

# 실습 1 1~사용자가 입력한 수까지 정수의 합
num = int(input("숫자를 입력하세요: "))
sum = 0
odd_sum = 0
for i in range(1,num+1):
    sum += i
    if i%2 == 1:
        odd_sum += i
    
print(f"입력한 수까지 합: {sum}")
print(f"입력한 수까지 홀수 합: {odd_sum}")

# 실습2 입력한 숫자만큼 카운트하고 "발사" 출력
num = int(input("몇 초?: "))
for i in range(num,0,-1):
    print(i,end=' ') 
print("발사!!")

# 실습3 구구단 만들기-사용자가 입력한 숫자의 구구단
num = int(input("몇 단을 출력 할까요? "))
for i in range(1,10):
    print(f"{num} * {i} = {num*i}")
    
# #sol1 합계
a = [10, 20, 30]
print(sum(a))

#sol2 합계
sum = 0
for i in a:
    sum+=i
print(sum)

# for문-list내포 <-복잡하지만 쓸 일이 많다!!
a=[1,2,3,4,5]
a2=[]
a3=[]
a4=[]

for i in a:
    a2.append(i*3)
print("a2 = ",a2)

a3 = [i*3 for i in a]
print("a3 = ",a3)

a4 = [i*3 for i in a if i % 2 == 0] # a에 있는것 중 짝수이면서 3의 배수인것 찾기!
print("a4 = ",a4)


# 이중 for문
for y in range(3):
    for x in range(2):
        print(f"y: {y}, x:{x}")
    print()
    
# 이중 for문 이용 구구단
for i in range(2,10):
    print(f"[{i} 단]")
    for j in range(1,10):
        print(f"{i} x {j} = {i*j}")
    print()
    
# 이중 for문 이용 자리배치도 행을 받아서 열을 나오도록

print('*** 자리배치도 ***')
customer = int(input('고객수 입력: '))
row = int(input('좌석행 수 입력: '))

if customer % row == 0:
    column = customer // row
else:
    column = (customer // row) + 1
# print(row)

for i in range(0, row):
  for j in range(1, column + 1):
    seat = i * column + j
    if seat > customer:
      break
    print(seat, end=" ")
  print()

# 실습4 이중for문 이용 별찍기
#1번
print("<1번문제>")
num = int(input("몇 줄? "))
for i in range(1,num+1):
    print(i*'*')
    
#2번
print("<2번문제>")
num = int(input("몇 줄? "))

for i in range(1,num+1):
  print(" "*(num-i)+"*"*(i))

#3번
print("<3번문제>")
num = int(input("몇 줄? "))
for i in range(1,num+1):
  print(" "*(num-i)+"*"*(2*i-1))

# 실습5
num = input("숫자 여러 개 입력 ").split()
num_list = list(map(int,num))
print(num_list)
sum = 0

max_n=max(num_list)
min_n=min(num_list)

print("가장 큰 값: ",max_n)
print("가장 작은 값: ",min_n)

num_list.remove(max_n)
num_list.remove(min_n)

count = len(num_list)

for i in num_list:
    sum += i

avg = sum/count
print("나머지 값의 평균: ",avg)
