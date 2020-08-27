import requests
from bs4 import BeautifulSoup

url = "http://www.kyobobook.co.kr/bestseller/bestSellerMain.laf"

req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser', from_encoding='utf-8')
title_list = soup.find_all('div', class_='title') # return value : list

for title in title_list:
	a = title .find('strong')
	if a:
		print(a.get_text()) # none을 제외하고 출력