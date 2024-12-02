#1
n = int(input("정수를 입력하시오: "))
num = list(range(n+1))
num.pop(0)
print(num)

## 2
vending_machine = ['게토레이', '레쓰비', '생수', '이프로']
print("================= RESTART")
drink = input("마시고 싶은 음료? ")

if drink in vending_machine:
    print(f"{drink} 드릴게요")
else:
    print(f"{drink}는 지금 없네요")


#3 자판기 프로그램 응용
vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']
print("남은 음료수: ",vending_machine)

user = input("사용자 종류를 입력하세요:\n1.소비자\n2.주인\n")
if user == '1' or user == '사용자':
    drink=input("마시고 싶은 음료? ")
    if drink in vending_machine:   
        print(f"{drink} 드릴게요")
        vending_machine.remove(drink)
        print("남은 음료수: ",vending_machine)
    else:
        print(f"{drink}는 지금 없네요")
    
elif user == '2' or user == '주인':
    select = input("할 일 선택:\n1.추가\n2.삭제\n")
    if select == '1' or select == '추가':
        print("남은 음료수: ",vending_machine)
        print('')
        add=input("추가할 음료수? ")
        vending_machine.append(add)
        vending_machine.sort()
        print("추가 완료")
        print("남은 음료수: ",vending_machine)
    elif select == '2' or select == '삭제':
        print("남은 음료수: ",vending_machine)
        delete=input("삭제할 음료수? ")
        if delete in vending_machine:
            vending_machine.remove(delete)
            print("삭제 완료")
            print("남은 음료수: ",vending_machine)
        else:
            print(f"{delete}는 지금 없네요")
    else:
        print("추가 또는 삭제를 선택해주세요.")
else:
    print("소비자 또는 주인 두가지 종류로만 입력해 주세요!(번호 또는 값 입력)")