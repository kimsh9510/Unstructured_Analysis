import urllib.request
import xml.dom.minidom

encodingKey = "vBWCvCxW515%2BgkLcMNXIXHBLHaNh9Xa8F8V9TrjFpKFeB0lP7D9%2BwXEIuAttbGQPrND%2BREAx2GIJf5eXoHF%2FdA%3D%3D"
decodingKey = "vBWCvCxW515+gkLcMNXIXHBLHaNh9Xa8F8V9TrjFpKFeB0lP7D9+wXEIuAttbGQPrND+REAx2GIJf5eXoHF/dA=="

print("[START]")

# request url정의
url = "http://apis.data.go.kr/1741000/DisasterMsg3/getDisasterMsg1List?ServiceKey=" + encodingKey + "&numOfRows=10&pageNo=1&asmItmCd=26&type=xml"
request = urllib.request.Request(url)

# request보내기
response = urllib.request.urlopen(request)

# 결과 코드 정의
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    dom = xml.dom.minidom.parseString(response_body.decode('utf-8'))
    pretty_xml_as_string = dom.toprettyxml()
    print(pretty_xml_as_string)
else:
    print("Error Code:" + rescode)

print("[END]")