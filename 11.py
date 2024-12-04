# 실습1
n, m = map(int,(input()).split())
s = set()

for i in range(n):
    s.add(input())
    
ans = 0
for _ in range(m):
    t=input()
    if t in s:
        ans+=1
print(ans)

# 실습2 del해도 되고 pop해도 되나 pop은 값이 튀어나옴
student = {'Alice':85, 'Bob':90, 'Charli':95}
student['David'] = 80
student['Alice'] = 88
del(student['Bob'])

for i in student.keys():
    print(i,student[i])

#2차원 리스트 중요!!
d=[
    [10,20],
    [30,40],
    [50,60]
]
print(d)
print(d[0][0])
print(d[1][0])
d.append([70,80])
print(d)
d[0][0]=90
print(d)

# d[1].pop(1) #->오류를 낼 수 있다.
print(d)

print(len(d[0]))

#for문 연습 -> pop해도 쓸수 있다.(열이 비어도 가능)
for i in range(0,len(d)):
    for j in range(0,len(d[i])):
        print(d[i][j], end=" ")
    print()

#모든 열이 다 동일 해야한다!! 자주쓰니까 잘 알기
for x, y in d:
    print(x,y)