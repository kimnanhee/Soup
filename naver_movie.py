'''
Beautiful Soup를 사용해서 네이버 영화 순위 가져오기
'''

import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"

req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser', from_encoding='utf-8')

rank = soup.find('table', class_='list_ranking') # rank에 영화 순위 html 전체 저장
movie_list = rank.find_all('div', class_='tit3') # movie_list에 영화 제목 html을 list형태로 저장

num=0
for movie in movie_list:
	name = movie .find('a')
	if name and num<10: # top 10까지 출력
		num+=1
		print(num,' ',name.get_text())