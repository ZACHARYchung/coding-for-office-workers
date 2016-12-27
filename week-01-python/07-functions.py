# # # 함수 functions
# # # 입력값 parameters, 반환값 return
# #
# # name1 = "marco"
# # name2 = "jane"
# # name3 = "john"
# # name4 = "tom"
# #
# # print("hello,{}".format(name1))
# # print("hello,{}".format(name2))
# # print("hello,{}".format(name3))
# # print("hello,{}".format(name4))
# # print("hello,{}".format(name1))
# # print("hello,{}".format(name1))
#
# def hello_friends(name):
#     print("hi,{}".format(name))
#
# name1="marco"
# name2="jane"
# name3="john"
# name4="snider"
# name5="zach"
#
# hello_friends(name1)
# hello_friends(name2)
# hello_friends(name3)
# hello_friends(name4)
# hello_friends(name5)

#반환값이 있다는건 return이 있다는 말
#입력값 o, 반환값 o
def sum(a,b):
    return a+b
#입력값 o, 반환값 x
def hello_friends(name):
    print("hello,{}".format(name))

#입력값 x, 반환값 o
def return_1():
    return 1
#입력값 x, 반환값 x
def hello_world():
    print("hello_world")

num_1 = return_1()
print(num_1)
