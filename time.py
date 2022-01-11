from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus


# 입력 매개변수
# stnIds : 지역 (108 # 서울)
# startDt : 날짜 범위 시작 (19870101)

def get_data(startDt_, stnIds_):
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode, quote_plus
    import bs4
    import pandas as pd
    import numpy as np
    from datetime import timedelta

    url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
    my_key = '서비스 키'

    # 날짜 범위의 최대값을 '20210501'로 설정
    queryParams = '?' + urlencode(
        {quote_plus('ServiceKey'): my_key, quote_plus('pageNo'): '1', quote_plus('numOfRows'): '999',
         quote_plus('dataType'): 'XML', quote_plus('dataCd'): 'ASOS', quote_plus('dateCd'): 'DAY',
         quote_plus('startDt'): startDt_, quote_plus('endDt'): '20210501', quote_plus('stnIds'): stnIds_})

    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()

    xmlobj = bs4.BeautifulSoup(response_body, 'lxml-xml')
    items = xmlobj.findAll('item')

    ## 원하는 형태로 가공
    asos = pd.DataFrame()
    for i in items:
        dic_ = {}
        for j in i.find_all():
            dic_[j.name] = [j.text]
        asos = pd.concat([asos, pd.DataFrame(dic_)], axis=0)

    # 한번에 1000건 이상 요청이 불가능한 상황에 대한 조치
    max_ = pd.to_datetime(asos['tm'], format='%Y-%m-%d').max()
    max_1 = max_ + timedelta(days=1)

    set_startDt_ = str(max_1.date()).replace('-', '')

    # 저장된 데이터 프레임과 다음 요청 시 시작될 날짜를 반환
    return asos, set_startDt_