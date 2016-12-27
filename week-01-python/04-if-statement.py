# #참과 거짓 blooean 참인진 거짓인지지 판단해서 참을 기본값으로 return
# #if
#
# a = True
# b = False
# # a가 참이고 그리고 b가 참이라면 (a 와 b가 둘다 참이어야 된다. )
# print (a and b)
# #a 가 참이거나 혹은 b가 참이라면 (a 나 b둘중에 하나라도 참이면 된다 )
# print (a or b)
#
#
# # == 이게 진짜 equal 의 meaning
# # = this refers to where a variant has certain appointed value
# a = True
# a == True
# print (a == True)
# print (a is True)
#


d = 6
if d >10 :
    print("숫자는 10보다 큽니다")
elif d>5 and d <= 10 :
    print("숫자는 10보다 작거나 같고 오보다 큽니다 ")
else :
    print("숫자는 5보다 작습니다")
