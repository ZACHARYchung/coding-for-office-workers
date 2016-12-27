def divided_by(first,second):
    try:
        return first/second

    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."

print(int(divided_by(4,2)))
print(divided_by(4,0)) #zerodividing error expected to happen

#예외 만들기
#Exception
class EvenNumberDevisionError(Exception):
    pass#클래스나 데피니션 정의를 할 때 내부에 뭐라도 코드가 한줄은 있어야 오류로 안뜸.
    #그걸 당장 안적더라도 일단 비워놓겠다는 의미의 명령어

def divide_by_odd_number(first, second):
    if second % 2 == 0:
        raise EvenNumberDevisionError #에러를 직접 일으켜야하는 상황에서는 raise 함수를 쓴다.
    else:
        return first/second

print(divide_by_odd_number(4, 2))
print(divide_by_odd_number(4, 3))
