# 씨네 21 - 배우 정보 크롤링
# 페이지를 이동해도 url 주소가 변하지 않는 상황
# 개발자 도구 - network - Preserve log check - ALL
# 씨네 21 - request 방식 => POST

# section = 'actor'
# period_start = '2022-02'
# gender = 'all'
# page = 3

# 1. 라이브러리 import
from bs4 import BeautifulSoup
import requests
import pymongo
import re

# 2. mongodb connection
conn = pymongo.MongoClient()
actor_db = conn.cine21
actor_collection = actor_db.actor_collection

# 3. 크롤링 주소 requests
cine21_url = 'http://www.cine21.com/rank/person/content'
post_data = dict()
post_data['section'] = 'actor'
post_data['period_start'] = '2021-08'
post_data['gender'] = 'all'
post_data['page'] = 1

res = requests.post(cine21_url, data=post_data)

# 4. parsing과 데이터 추출
soup = BeautifulSoup(res.content, 'html.parser')

# for actor in actors:
#     print(re.sub('\(\w*\)', '', actor.text))

# 5. 배우 상세 정보 추출
# 6. 배우 흥행 지수와 흥행 영화
# 7. 수집한 데이터 기반 사전 만들기
# 특수한 정규 표현식
# Greedy(.*) 욕심 가득한 것 vs Non-Greedy(.*?) 욕심을 줄인 것

actors = soup.select('li.people_li div.name')
hits = soup.select('ul.num_info > li > strong')
movies = soup.select('ul.mov_list')
rankings = soup.select('li.people_li > span.grade')
actors_info_list = list()

for index, actor in enumerate(actors):
    actor_name = re.sub('\(\w*\)', '', actor.text)
    actor_hits = int(hits[index].text.replace(',', ''))
    movie_titles = movies[index].select('li a span')
    movie_title_list = list()
    for movie_title in movie_titles:
        movie_title_list.append(movie_title.text)

    actor_info_dict = dict()
    actor_info_dict['배우이름'] = actor_name
    actor_info_dict['흥행지수'] = actor_hits
    actor_info_dict['출연영화'] = movie_title_list
    actor_info_dict['랭킹'] = rankings[index].text

    actor_link = 'http://www.cine21.com' + actor.select_one('a').attrs['href']
    response_actor = requests.get(actor_link)
    soup_actor = BeautifulSoup(response_actor.content, 'html.parser')
    default_info = soup_actor.select_one('ul.default_info')
    actor_details = default_info.select('li')

    for actor_item in actor_details:
        actor_item_field = actor_item.select_one('span.tit').text
        actor_item_value = re.sub('<span.*?>.*?</span>', '', str(actor_item))
        actor_item_value = re.sub('<.*?>', '', actor_item_value)
        actor_info_dict[actor_item_field] = actor_item_value
    actors_info_list.append(actor_info_dict)
print(actors_info_list)