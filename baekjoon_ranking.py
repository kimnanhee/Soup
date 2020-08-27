'''
Beautiful Soup를 사용해서 백준 문제 순위 가져오기
'''

import requests
from bs4 import BeautifulSoup

url = "https://www.acmicpc.net/problem/ranking" # 백준 문제 순위

req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser', from_encoding='utf-8')

ranking = soup.find('table', class_='table table-striped table-bordered clickable-table') # ranking에 문제 순위를 html저장
title_list = ranking.find_all('a') # ranking 안의 a태그를 모두 저장

for title in title_list:
	a = title.get_text()
	try:
		int(a) # 숫자일때 제외
	except:
		print(a)