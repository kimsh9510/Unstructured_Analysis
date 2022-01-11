# 라이브러리 import
import requests
import pprint
import json
import pandas as pd
from pandas.io.json import json_normalize
from xml.etree import ElementTree
import xml.etree.ElementTree as ET
import csv

# url 입력 - ServiceKey=인증키, pageNo=페이지 시작, numOfRows=출력 행 갯수, type=json or xml
url = 'http://apis.data.go.kr/1741000/DisasterMsg3/getDisasterMsg1List?serviceKey=vBWCvCxW515%2BgkLcMNXIXHBLHaNh9Xa8F8V9TrjFpKFeB0lP7D9%2BwXEIuAttbGQPrND%2BREAx2GIJf5eXoHF%2FdA%3D%3D&pageNo=1&numOfRows=10&type=json'

# url 불러오기
response = requests.get(url)

#데이터 값 출력해보기
contents = response.text
#print(contents)

#json 변경
json_ob = json.loads(contents)
pp = pprint.PrettyPrinter(indent=4)
print(pp.pprint(contents))

json_ob = json.loads(contents)
print(json_ob)
print(type(json_ob)) #json타입 확인

body = json_ob['DisasterMsg']
print(body)

info = json.loads(body)['row']

print(info[0].keys())

df=pd.json_normalize(contents['CardSubwayStatsNew']['row'])