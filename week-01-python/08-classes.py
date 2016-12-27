# 클래스

###Article varibles
title1="개발"
author1="마르코"
content1="개발은 쉬워요"
view_count1=0

# ##### Article Class
# class Article:
#     title = "개발"
#     author = "마르코"
#     content = "개발은 쉬워요"
#     view_count = 0
#
# article1 = Article() #인스턴스를 만들었다. 객체를 만들었다. 라는의미
# print(article1.title)
# article2 = Article()
# print(article2.title)
# article2.title="코칭"
# print(article1.title)
# print(article2.title)

#### Article class with _init
class Article:

    author = "marco"
    view_count=0

    def __init__(self,title,content): #self 는 클래스 내에서 함수를 쓰려면 꼭 넣어줘야 한다.
        self.title = title
        self.content = content
    def read(self):
        self.view_count = self.view_count + 1


article1 = Article("개발","개발은 쉬워요")
article2 = Article("코칭","코칭은 쉬워요")
article3 = Article("창업","창업은 쉬워요")

print(article1.view_count)
article1.read()
print(article1.view_count)
print(article1.author)


### Article class inheritance 상속

class BrunchArticle(Article): #여기는 아티클이라는 부모 클라스의 자식 클라스
    source="브런치"

    def read(self):
        self.view_count=self.view_count + 2 #Java의 오버라이드 개념

brunch_article=BrunchArticle("개발","개발은 쉬워요")
print(brunch_article.title)
print(brunch_article.source)
print(brunch_article.view_count)
brunch_article.read()
print(brunch_article.view_count)
