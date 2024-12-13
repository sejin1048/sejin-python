# # sort()할때 사전순서로 진행된다!
# a = [3,4,2,1]
# # a.sort(reverse=True)
# a.sort()
# a.reverse()
# print(a)

# b = ["a", "c", "b", "d"]
# b.sort()
# print(b)

# c = ["1", "10", "11", "2"]
# c.sort()
# print(c)



# # 두번째 강서를 찾아라
# d = ["강남", "강북", "서", "asdfd", "서", "서"]
# # d.sort()
# first = d.index("서")+1
# print(first + d[first:].index("서"))
# print(d.count("서"))

#실습 1 리스트 있을때 결과 출력하라
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
#1 2번 인덱스 값 출력
print("<1번>")
print(rainbow[2])

#2 알파벳 순서로 정렬한 값 출력
print("<2번>")
rainbow.sort()
print(rainbow)

#3 좋아하는 색 맨 마지막에 추가하기
print("<3번>")
rainbow.append("black")
print(rainbow)

#4 3~6번째 값 삭제하기
print("<4번>")
del rainbow[3:7]
print(rainbow)
# print(rainbow.pop(1))
# print(rainbow.count("a"))



