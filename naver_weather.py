'''
Beautiful Soup를 사용해서 지역별 현재 온도 가져오기
네이버 날씨의 지도에 표시되어있는 지역들의 날씨를 크롤링한다.
'''

import requests
from bs4 import BeautifulSoup

url = "https://n.weather.naver.com/" # 네이버 날씨

req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser', from_encoding='utf-8')

nation = soup.find('div', class_='nation_map') # nation에 날씨 지도 html 전체 저장
weather_list = nation.find_all('span', class_='text') # weather_list에 각 지역의 html을 리스트로 저장

for weather in weather_list: # 리스트이기 때문에 for문을 돌릴 수 있다
	print(weather.get_text()) # 지역별 html의 text만 뽑아서 출력한다