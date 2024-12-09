# class

a = dict()
a = set()

class b: #클래스:붕아빵틀
    pass
o1 = b() #객체:붕어빵
o2 = b()
o3 = b()


class Movie:
    title = "범죄도시4"
    
movie1 = Movie()
movie2 = Movie()

print(movie1.title)
print(movie2.title)

movie1.title = "파묘" #붕어빵끼리는 서로 영향을 미치지 않는다

print(movie1.title)
print(movie2.title) # .이 클래스에 접근하는 것임!

movie1.score = '1' # .score(score말고 다른것도 가능) 는 새로 만듦과 동시에 출력
print(movie1.score)
# print(movie2.score)

#클래스 함수
class Movie:
    name = ''
    def print_msg(msg):
        print(msg)
    def modify(self,movie):
        self.name = movie
    def print_name(self):
        print(self.name) #self.name해야함!
    
movie1 = Movie()
movie2 = Movie()

Movie.print_msg("print하기")
# Movie.modify(movie1,"print하기2") #이렇게 잘 안씀
movie1.modify("프린트하기3") #원래는 self,movie를 둘다 넣어줘야하는데 self값이 자동 할당 되기 때문에 안써도됨!
movie1.print_name()

movie2.modify("프린트하기4")
print("movie2.name: ",movie2.name)

# Movie.print_name("ttt")

# 생성자
class Movie:
    def __init__(self): # 초기화 해주는것 : 생성자
        print("hello")

movie = Movie()

# 매개변수가 있는 생성자
class Movie:
    count = 0
    
    # def __init__(self,title = "오징어게임", audience = 300):
    def __init__(self,title,audience):
        self.title = title
        self.audience = audience

movie1 = Movie("파묘", 100)
movie2 = Movie("파묘2", 200)
print(movie1.title,movie1.audience)
print(movie2.title,movie1.audience)

# movie3 = Movie() #<-파라미터 없어서 안되는것! 
# print(movie3.title,movie3.audience)


# 중요! class와 공유하는 변수를 만들고 싶을때
class Movie:
    count = 0

    def __init__(self,title,audience):
        self.title = title
        self.audience = audience
        Movie.count += 1 #<-붕어빵 틀을 바꾸는것이므로 영햐을 미침

movie1 = Movie("파묘", 100)
print(Movie.count)
movie2 = Movie("파묘2", 200)
print("")

print(movie1.count) #
print(movie2.count) # 3개 다 공유하는 값
print(Movie.count)  #
print("")

Movie.count += 1
print(movie1.count) #
print(movie2.count) # 3개 다 공유하는 값
print(Movie.count)  #
print("")

movie1.count += 1 # <- 웬만하면 안쓰는게 좋다! -> 클래스 변수는 클래스변수 용도로만 사용하자! 
print(movie1.count) #
print(movie2.count) # 3개 다 공유하는 값
print(Movie.count)  #
print("")

Movie.count += 1 # 값을 공유하게 만드므로! : 붕어빵 틀을 바꾼것
print(movie1.count) #
print(movie2.count) # 3개 다 공유하는 값
print(Movie.count)  #

# 접근제어
class Movie:
    count = 0
    def __init__(self,title,audience):
        self.__title = title
        self.__audience = audience
        Movie.count += 1
        
    def get_title(self):
        return self.__title
    
    def set_title(self,title):
        self.__title = title

movie1 = Movie("파묘",100)
# print(movie1.__title) #안됨! 직접 접근을 못한다!
print(movie1.get_title())
# print(movie1.set_title())

# movie1.__title = "오겜" #<- class안에 __init__에 들어있는 __title이 아니라 새롭게
# print(movie1.get_title())
# print(movie1.__title)

# 접근제어 언더바 하나만 있을 때
class Movie:
    count = 0
    def __init__(self,title,audience):
        self.__title = title
        self._audience = audience
        Movie.count += 1
        
    def get_title(self):  # 접근제한 했기때문에 get이랑 set을 만들어서 접근 창구를 만들어준다!!
        return self.__title
    
    def set_title(self,title):
        self.__title = title
        
    
    def get_audience(self):
        return self._audience    
    
    def set_audience(self, audience):
        self._audience = audience   

movie1 = Movie("파묘",100)
# print(movie1.__title) #안됨! 직접 접근을 못한다!
print(movie1.get_title())
print(movie1._audience)
print(movie1.get_audience())

movie1.set_title("타이타닉")

print(movie1.get_title())

#접근제한 문제

class MyAdd:
    __a = 1
    __b = 2
    
    def set_a(self,a):
        self.__a = a
            
    def sum(self): 
        return self.__a + self.__b
    
    
a = MyAdd()
print(a.sum()) # 3

a.set_a(3)
print(a.sum())

#정보 은닉 건강상태 클래스 만들기
class Health:
    def __init__(self,name):
        self.__name = name
        self.__hp = 100
    
    def get_name(self):
        return self.__name
    
    def set_hp(self,hp):
        hp = max(hp,0) #둘중에 큰게 0 -> 0보다 작을때 0으로 만들어 주는것
        hp = min(hp, 100) #둘중에 작은게 100 -> 100보다 작을 땐 100
        self.__hp = hp
    
    def get_hp_str(self):
        return "hp: " + str(self.__hp)
    
    def exercise(self,hours):
        self.set_hp(self.__hp + hours)
        print(f"{hours}시간 운동하다")

    def drink(self,cups):
        self.set_hp(self.__hp + cups)
        print(f"술을 {cups}잔 마시다")
        
p1 = Health("나몸짱")
p1.set_hp(100)
p1.exercise(5)
p1.drink(2)
print(f"{p1.get_name()} - {p1.get_hp_str()}")
print("")

p2 = Health("나약해")
p2.set_hp(10)
p2.exercise(1)
p2.drink(12)
print(f"{p2.get_name()} - {p2.get_hp_str()}")

# 실습1) 사칙연산 클래스 만들기
class calc:
    def __init__(self,a,b):
        self.__a = a
        self.__b = b
        
    def add(self):
        return self.__a + self.__b
    
    def sub(self):
        return self.__a - self.__b
    
    def mul(self):
        return self.__a * self.__b
    
    def div(self):
        if self.__b == 0:
            return "0으로 나눌 수 없습니다! 다시 입력하세요!"
        else:
            return self.__a / self.__b

result1 = calc(5,3)
print(f"add: {result1.add()}, sub: {result1.sub()}, mul: {result1.mul()}, div: {result1.div()}")

result2 = calc(4,0)
print(f"add: {result2.add()}, sub: {result2.sub()}, mul: {result2.mul()}, div: {result2.div()}")

#사번 자동부여
class Employee:
    serial_num = 1000
    
    def __init__(self,name):
        Employee.serial_num += 1
        self.id = Employee.serial_num
        self.name = name
    
    def __str__(self): #string이 뭔지 알아야 한다! 적고자 하는거 적는것 
        return f"사번 : {self.id}, 이름 : {self.name}"
    
    def __int__(self):
        return 10
    
e1 = Employee("최사원")
print(e1)

e2 = Employee("안사원")
print(e2)

e3 = Employee("한사원")
print(e3)

a = str(e3)
print("<스트링 형변환> a",a) #string형 변환
b = int(e3)
print("<int> b",b)

employee = [
    Employee('구름'),
    Employee('별'),
    Employee('행성'),
    Employee('달') 
]
for i in employee:
    print(i)
        
