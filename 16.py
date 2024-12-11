f = open("text.txt","w")
f.write("Hello World!!@@\n")
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