#튜플 -> 
t1=(10, 20, 30)
print(type(t1))
print(t1[0])
#삭제안됨 del t1[0], # 수정 안됨 
# t1[0]=3, 할당안됨
t2=(10)
t3=(10,)
t4=10,40
print(type(t4))

# set
set1 = {1,2,3,3}
print(set1)
set2 = set([1,2,3,3])
print(set2)
set2.add(4)
print(set2)

while len(set2) > 0:
    a = set2.pop()
    print(a)
    
l1=[1,2,3,4]

while len(l1) > 0:
    a = l1.pop()
    print(a)
 
set3=set("apple")
print(set3)

while len(set3) > 0:
    a = set3.pop()
    print(a)

# set응용 -> 반복문 안에서 remove하면 안된다! 
# for루프 안에 하려면 다른곳에 저장했다가 해야한다!
name = ["1","2","3","2"]
a = []
for i in range(len(name)):
    if a.count(name[i]) < 1:
        a.append(name[i])
        print(a)
name = a
print(name)
                             
                
name_set = set(name)
print(name_set)
name_list = list(name_set)
name_list.sort()
print(name_list)

# 딕셔너리 중요!!
a = {} #딕셔너리
print(type(a))
b = {1} #셋
print(type(b))
c = dict() #딕셔너리
print(type(c))

c={1:'a', 'b':'b'} #값은 중복될 수 있느나 키는 중복 불가
print(c)
c[2]='c' #인덱스가 아니라 키다
c['c']=2 #인덱스가 아니라 키다
print(c)

del c[2]
del c['b']
print(c)
#print(c[2])<- 요소가 없을 때 에러
print(c.get(2)) # <-에러처리 된거
print(c.keys())
print(c.values())

#많이 씀 <-get으로도 가능하고 리스트형태로도 가능
for i in c.keys():
    print(i, c.get(i))
    
    
print('c' in c) #print('c' in c.keys())처럼 안해도됨
print(2 in c.values())

#딕셔너리 응용
dic = {
    "비트": "0이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위",
    "변수": "어떤 1개의 자료를 저장하기 위한 메모리 할당 공간",
    "리스트": "여러 개의 연속적인 자료를 저장하는 자료구조"
}

print("★ 컴퓨터 사전 ★")
word = input("검색할 단어를 입력하세요: ")
if word in dic:
    print(f'{word}: {dic[word]}')
else:
    print("정의된 단어가 없습니다.")