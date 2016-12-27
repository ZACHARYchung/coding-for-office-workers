#사람 클래스 만들기
class Man:
    def __init__(self,name,age,gender):
        self.name= name
        self.age= age
        self.gender= gender
    def printData(self):
        print("!!입력하신 정보!!")
        print ("이름"+ self.name)
        print ("나이"+ self.age)
        print ("성별"+ self.gender)

#사람 기본 정보 입력하기
print("사람정보를 입력하세요")
name1=input("이름")
age1=input("나이")
gender1=input("성별")

#클래스 활용
man2 = Man(name1,age1,gender1)
#클래스 활용 출력
man2.printData()

#상속클래스 생성
class Colleague(Man):
        position="대리"
print("새 직장동료정보를 입력하세요")
name2=input("name")
age2=input("age")
gender2=input("gender")
colleagu1=Colleague(name2,age2,gender2)
print("!! new colleague is!!")
colleagu1.printData()
print(colleagu1.position)
