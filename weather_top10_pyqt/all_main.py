from all_ui import *
from image_rc import *

import requests
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
from time import sleep

def read_thread(ui):
	while True:
		url = "https://n.weather.naver.com/" # 네이버 날씨
		req = requests.get(url)
		soup = BeautifulSoup(req.content, 'html.parser', from_encoding='utf-8')
		nation = soup.find('div', class_='nation_map') 
		weather_list = nation.find_all('span', class_='text') 
		arr=""
		for weather in weather_list:
			arr+=(weather.get_text()+'\n')
		ui.text_weather.setText(arr)

		url = "http://www.kyobobook.co.kr/bestseller/bestSellerMain.laf" # 교보문고 베스트셀러
		req = requests.get(url)
		soup = BeautifulSoup(req.content, 'html.parser', from_encoding='utf-8')
		title_list = soup.find_all('div', class_='title') # return value : list
		num=0
		arr=""
		for title in title_list:
			a = title .find('strong')
			if a and num<10:
				num+=1
				arr+=(str(num)+' - '+a.get_text()+'\n')
		ui.text_best.setText(arr)

		url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn" # 네이버 영화 순위
		req = requests.get(url)
		soup = BeautifulSoup(req.content, 'html.parser', from_encoding='utf-8')
		rank = soup.find('table', class_='list_ranking')
		movie_list = rank.find_all('div', class_='tit3')
		num=0
		arr=""
		for movie in movie_list:
			name = movie .find('a')
			if name and num<10: # top 10까지 출력
				num+=1
				arr+=(str(num)+' - '+name.get_text()+'\n')
		ui.text_movie.setText(arr)

		url = "https://www.acmicpc.net/problem/ranking" # 백준 문제 순위
		req = requests.get(url)
		soup = BeautifulSoup(req.content, 'html.parser', from_encoding='utf-8')
		ranking = soup.find('table', class_='table table-striped table-bordered clickable-table')
		title_list = ranking.find_all('a')
		num=0
		arr=""
		arr_2=""
		for title in title_list:
			a = title.get_text()
			try:
				int(a) # 숫자일때 제외
			except:
				if num<10:
					num+=1
					if num<6:
						arr+=(str(num)+' - '+a+'\n')
					else:
						arr_2+=(str(num)+' - '+a+'\n')
		ui.text_baekjoon.setText(arr)
		ui.text_baekjoon_2.setText(arr_2)
		sleep(5)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    th = threading.Thread(target=read_thread, args=(ui,)) # 스레드 설정, read_thread함수에 인자로 ui를 넘겨준다
    th.daemon = True;
    th.start()

    MainWindow.show()
    sys.exit(app.exec_())