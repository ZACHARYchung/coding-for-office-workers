#구구단-my version

num = input("몇 단을 출력하시겠습니까")
a=1
while a<10:
    print (num,"*",a,"=",int(num) * int(a))
    a=a+1

#구구단-marco version
#1)사용자로부터 몇단을 출력할지 받을 것
#2)해당 단을 곱하기 1에서 곱하기 9까지 실행할 것
dan = int(input("몇 단을 출력하시겠습니까?"))
for num in range(1,10):
    print("{}*{}={}".format(dan, num, dan * num))
