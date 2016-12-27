# #list[] 대괄호를쓰고 있다 대괄호면 쓰면 리스트로 인식
# print("list")
# print([1,2,3])
# print(type([1,2,3]))
#
# #tuple (1, ) 소괄호를 쓰고 있다. 반드시 값을 적고 컴마를 하나 해야지 튜플로 인식
# print("tuple")
# print((1,2,3))
# #print(type((1,2,3)))
#
# #list
# print("list")
# list_a=[1,2,3]
# print(list_a)
# print(list_a[1])
# #파이선은 0부터 시작한다
# #slice 인덱스 2에 해당하는 부분의 바로 전까지 짤린다
# slice
# print(list_a[0:2])
# #append 뭔가를 추가하는것
# list_a.append(4)
# print(list_a)
#
# list_a.remove(2)
# print(list_a)
#
# #tuple (1,)
# print("tuple")
# tuple_a = (1,2,3)
# print(tuple_a)
# print(type(tuple_a))
#tuple_a.append(4)

#dict (map) 다른 언어에서는 map 이라고도 함

#key&value
# dict_a={
# "apple":"a type of fruits",
# "pen" :"something to write with"
# }
# print(dict_a["pen"])


#set set([]) 집합이라고 보면 쉽다
set_a = set([1,1,1,1,1,1,1,2,3])
set_b = set([2,4,6])
print(set_a)
print(set_b)
print(set_a&set_b)
print(set_a|set_b)
print(set_a-set_b)
#교집합 합집합 차집합 여집합 // 사실 셋을 쓰는 제일 큰 이유는 중복이 없다는 것 리스트와 제일 크게 다른점
