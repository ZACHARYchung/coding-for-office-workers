#1) 한식, 중식, 일식 세가지 뜨고 사용자가 한가지 고르게 하도록
#2) 한가지를 고르면 식당 이름을 randomly 추천해준다

import random
foodtype_1=input(" 한식, 중식, 일식 중 한 가지를 고르세요!!!")
#한식당 중식당 일식당 리스트를 작성
중식=["복성각","홍콩반점","산둥성"]
한식=["삼원가든","순대국집","남도음식"]
일식=["이도","쿠시","이태원천상"]
# print(foodtype_1)
if foodtype_1=="한식":
    print(random.choice(한식))
elif foodtype_1=="중식":
    print(random.choice(중식))
elif foodtype_1=="일식":
    print(random.choice(일식))
