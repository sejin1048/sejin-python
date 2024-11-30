a = []
b = [1,2,3,4]
c = ["장원영", "안유진"]
d = [1, "아이브"]

print(len(c))
print(c[0])
print(c[1])
c[0]="카리나"
print(c)

del c[0]
print(c)

c.append("asdfs")
print(c)

print(b[-1])
print(type(b))

seasons = ["봄", "여름", "가을", "겨울"]
print(seasons[0:1])
print(seasons[0:2])
print(seasons[:2])
print(seasons[1:])
print(seasons[2:])
print(seasons[1:3])
print(seasons[:])
print(seasons)
print(seasons[::3])
print(seasons[::-1])

#리스트
seasons2=["봄", "여름", "가을", "겨울", [1,2,3,4]]
print(seasons2[-1][0::2])

abcd ="abcd"
abc = ['a','b','c','d']
print(len(abcd))
print(len(abc))

#리스트 실습문제 _ a를 이용하여 짝수만을 뽑은 리스트 만들기
a = [1,2,3,4,5,6,7,8,9,10]
even=a[1::2]
odd=a[0::2]
print("짝수:",even)
print("홀수:",odd)
