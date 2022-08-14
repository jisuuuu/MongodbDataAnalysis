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

actors = soup.select('li.people_li div.name')
for actor in actors:
    print(re.sub('\(\w*\)', '', actor.text))