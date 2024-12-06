def pr_str(txt="str", count = 1, count2 = 1): #디폴트 되는게 앞에 있어야한다!(뭐가 생략된지 알아야 하기 때문에!) 중요!!
    for i in range(count):
        print(txt)
        print(count2)


pr_str("hello", 3 ,2)
pr_str("hello", 3)
print()
pr_str("hello")
print()
pr_str()

print(1,2,3,4)
pr_str("234",count2=3)
 
# 평균내기 , *없을때는 튜플로 넣자! 중요!!! <- print()에서 사용하는 방식
def calc_avg(*numbers):
    # print(type(numbers))
    print(numbers)
    return sum(numbers)/len(numbers)

print(calc_avg(1,2))
print(calc_avg(1,2,3,4,5))

# 튜플로 동작한다
def a():
    return 1,2

print(a())

#가변 매개변수 <- 잘 쓰지는 않음
def intro(**kw):
    print(type(kw))
    for k, v in kw.items(): #딕셔너리 쓰는것이므로 items()는 중요!
        print(f"{k}: {v}")
    for i in kw: # key를 뽑아낸다!
        print(f"{i}")
        
intro(name = 'Alice', age=25, city="NY")

# sorted <-파이썬 내장함수! .sort()와 구분하기!
list = [2,4,1,4,6]
list.sort() # <- 원본 리스트 자체를 바꾸는 것임!
print("list",list)

list2 = [2,4,1,4,6]
print("sorted_list",sorted(list2))
print("list2",list2) # <- sorted쓰면 원본 리스트 자체를 변경하는 것이 아니라 sort된 결과를 return하는 것임! 

# sorted 써야함
# 3번째로 작은 값의 인덱스를 구하라
#정렬하고 그 값을 원본에서 찾으면 된다.
list2 = [2,4,1,4,6]
print("sorted_list",sorted(list2)[2])

# eval <-많이 쓰는 함수임
print(eval("1+2*2"))
#round
print(round(4.4)) #파이썬에서 round는 짝수가 되도록 반올림한다. ex) 4.5->5 , 5.5->6
print(int(4.7+0.5)) # round안쓰고 반올림하기 

print(round(2.547))
print(round(2.547,1))
print(round(2.547,2))
print(round(127,-1))
print(round(127,-2))
print(round(127))

# pow
print(2**3)
print(pow(2,3))

# 재귀 함수 (중요!!) <- 종료조건 필수
def hello():
    global count  
    
    if count == 3:
        return

    print("hello")
    count += 1
    hello()

count = 0
hello()

# 재귀 함수 
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5)) 

#실습2 재귀함수로 피보나치 수 구하기
def fibo(n):
    if n <= 2:
        return 1
    return fibo(n-1)+fibo(n-2)

print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))
print(fibo(6))
# print(fibo(100))

# 최적화 하기
def fibo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
    return memo[n]

print(fibo(1))
print(fibo(2))  
print(fibo(3))  
print(fibo(4))  
print(fibo(5))  
print(fibo(6))  
print(fibo(100)) 

# 최적화 하기(메모이제이션)
memory = {1: 1, 2: 1}
def fibo_memoization(n):
    if n in memory:
        number = memory[n]
    else:
        number = fibo_memoization(n-1) + fibo_memoization(n-2)
        memory[n] = number
    return number
print(fibo_memoization(1))
print(fibo_memoization(2))
print(fibo_memoization(3))
print(fibo_memoization(4))
print(fibo_memoization(5))
print(fibo_memoization(6))
print(fibo_memoization(100))

#하노이탑문제(재귀 함수!) 2*f(n-1)+1
def hanoi(number_of_disks_to_move, from_, to_, via_):
    global cnt
    if number_of_disks_to_move == 1:
        print(f"{cnt+1}: ",end=' ')
        print(from_, "->", to_)
        cnt+=1
    else:
        hanoi(number_of_disks_to_move-1, from_, via_, to_)
        print(f"{cnt+1}: ",end=' ')
        print(from_, "->", to_)
        hanoi(number_of_disks_to_move-1, via_, to_, from_)
        cnt+=1
        
cnt = 0
print(hanoi(4,"T1", "T2", "T3"))

# 람다식 return을 생략해도 된다!
add = lambda x,y:x+y #<-함수를 변수에 넣을 수 있다!
print(type(add))
print(add(1,2))

def add2(x,y):
    return x+y

add3 = add2
print(add2(1,2))
print(add3(1,2))

#람다 함수를 매개변수로 전달하기 <- 콜백함수!!
def call_3(func): #func는 매개변수
    for i in range(3):
        func()

call_3(lambda:print("hi"))
call_3(lambda:print("hello"))

#콜백예시
def download(startedCallback, endedCallback):
    startedCallback()
    #download
    print("download 중")
    ###
    ###
    endedCallback()

#한번만 하고 말때(일시적으로 필요할 때)
download(lambda:print("다운로드 시작"),lambda:print("완료되었습니다.")) 

# # map
# list(map(int,["1","2","3"]))

# result = map(lambda x:3*x, [1,2,3,4]) #1,2,3,4를 3배하는 것 1회성
# #어디에 할당하지 않으면 재사용 불가능. 따라서 계속 필요하면 함수를 직접 만들자!
# print(list(result))

# #filter()
# li = [-5,1,2,-11,76]
# value = list(filter(lambda x:x>=3 ,map(lambda x:2*x, li))) #결과가 true인것들만 나오도록
# print(value)
# # value = list(filter(lambda x:x>10, li)) #결과가 true인것들만 나오도록
# # print(value)

# 문제1
def solution(arr):
    answer = []
    for i in arr:
        if i>=50 and i%2 == 0:
            answer.append(i//2)
        elif i<50 and i%2 == 1:
            answer.append(i*2)
        else:
            answer.append(i)
    return answer
print(solution([1, 2, 3, 100, 99, 98]))

# 문제2
def solution(myString):
    answer = []
    new = myString.split('x')
    for i in new:
        answer.append(len(i))        
    return answer

print(solution("oxooxoxxox"))
print(solution("xabcxdefxghi"))

# 문제3
def solution(str1, str2):
    answer = 0
    if str1 in str2:
        answer = 1
    else:
        answer = 0
    return answer

print(solution("abc","aabcc"))
print(solution("tbt","tbbttb"))	