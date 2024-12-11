import sys

# print(sys.argv)
# args = sys.argv[1:]
# print(args)

sum = 0

for i in range(1,len(sys.argv)):
    sum += int(sys.argv[i])

print(sum)
# print(int(sys.argv[1])+int(sys.argv[2]))

#2번 문제 sys.exit(0)할때
import sys

if len(sys.argv) <= 2 or len(sys.argv) > 4:
    print("3개만 입력해 주세요")
    sys.exit(0)    

if sys.argv[1] == 'mul':
    mul = int(sys.argv[2]) * int(sys.argv[3])
    print(mul)
elif sys.argv[1] == 'add':
    add = int(sys.argv[2]) + int(sys.argv[3])
    print(add)

# sys.exit(0)으로 고쳐보기
import sys

args = sys.argv
if (len(args)!=4):
    print("입력오류")
    sys.exit(0)

cmd = args[1]
num1 = int(args[2])
num2 = int(args[3])
if cmd == "mul":
    print(num1*num2)
elif cmd == "add":
    print(num1+num2)

# os모듈
import os
os.chdir("C:/Users/hsjin/git-test/python")
dir = os.popen('dir')
print(dir.read())
print(os.listdir())

