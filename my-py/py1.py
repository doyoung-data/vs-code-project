# 함수 선언
def add_two_numbers(num1, num2):
  sum = num1 + num2
  print(sum)
  return sum



# 함수 호출
result = add_two_numbers(1, 2)
print(result)

if result == 100:
  print("100입니다")

elif  result == 200:
  print("200입니다")

else:
  ("100, 200이 아님")

#[2] 0보다 큰지 확인
if result>0:
  print('0보다 큽니다')




  

fruits = ['사과', '바나나','수박', '파인애플']

for i in range(len(fruits)):
  print(fruits[i])


for i in fruits:
  print(i)



def process():
  a=10
  try:
    b = 10 / 0 # 에러코드

  except:
    print("에러발생")

  finally:
    print("일단 출력")


process()



class Student:
  def __init__(self, name= '', age = 0):
    self.name=name
    self.age=age
    self.hello()
    
  def hello(self):
    print(self.name)




man = Student('정민', 35)




class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.introduce()  # 생성자에서 메서드 호출

    def introduce(self):
        print(f"Initializing... My name is {self.name} and I am {self.age} years old.")

# 클래스 인스턴스화
person = MyClass("Bob", 40)


class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"My name is {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # 부모 클래스의 초기화 메서드를 호출
        self.age = age

    def greet(self):
        super().greet()  # 부모 클래스의 greet 메서드를 호출
        print(f"I am {self.age} years old")