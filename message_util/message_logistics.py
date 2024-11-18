from bs4 import BeautifulSoup

import datetime
import os

import certifi
import requests


def message_logistics(message, room, sender):
    if "!택배" in message or "!ㅌㅂ" in message:
        return message_logistics_main(message)
    if "!통관" in message or "!ㅌㄱ" in message:
        return message_custom_tracker(message)
    return None

def message_custom_tracker(message):
    strMessage = ""
    try:
        message = message.replace('!통관', '').replace('!ㅌㄱ', '').replace(" ", "")
        key = os.environ['CUSTOM_API_KEY']
        year = datetime.date.today().year
        url = 'https://unipass.customs.go.kr:38010/ext/rest/cargCsclPrgsInfoQry/retrieveCargCsclPrgsInfo?crkyCn=%s&blYy=%s&hblNo=%s' % (key, year, message)
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "xml")
        name = soup.find('prnm')
        customs_name = soup.find('etprCstm')
        status = soup.find('prgsStts')
        process_time = datetime.datetime.strptime(str(soup.find('prcsDttm').text), "%Y%m%d%H%M%S").strftime("%Y.%m.%d %H:%M:%S")
        strMessage = "/// 관세청 UNIPASS 통관 조회 ///\n\n품명: %s\n입항세관: %s\n통관진행상태: %s\n처리일시: %s" % (name.text, customs_name.text, status.text, process_time)
    except:
        strMessage = "존재하지 않는 운송장번호이거나 잘못된 형식 혹은 아직 입항하지 않은 화물입니다.\\m사용법: !통관 123456789"

    return strMessage

def message_logistics_main(message):
    strMessage = ""
    message = message.replace("!택배", "").replace("!ㅌㅂ", "").replace(" ", "")

    if message == "":
        strMessage = "///택배 운송장조회 사용 방법///\\m사용 예시: !택배[운송장번호]\nex)!택배1234567890\n지원중인 택배사: 우체국택배, 대한통운(CJ, 대통), 로젠택배, 롯데택배, 한진택배\n만약 통관 중인 택배라면 우선적으로 통관 상황을 조회합니다."
        return strMessage

    strMessage = message_custom_tracker(message)
    if "존재하지 않는 운송장" in strMessage:
        strMessage = message_logistics_parser(message)
    else:
        tmpmsg = message_logistics_parser(message)
        if "존재하지 않는 운송장" in tmpmsg:
            strMessage =  strMessage + "\\m현재 택배사에 인계되지 않은 화물입니다."
        else:
            strMessage = strMessage + "\\m" + tmpmsg

    return strMessage

def message_logistics_parser(message):
    logistics = [
        message_logistics_parser_CJ,
        message_logistics_parser_HJ,
        message_logistics_parser_KP,
        message_logistics_parser_LG,
        message_logistics_parser_LT
    ]

    for parser in logistics:
        strMessage = parser(message)
        if strMessage: return strMessage

    strMessage = "미집하된 택배이거나 존재하지 않는 운송장 번호입니다.\\m사용 예시: !택배[운송장번호]\nex)!택배1234567890\n지원중인 택배사: 우체국택배, 대한통운(CJ, 대통), 로젠택배, 롯데택배, 한진택배"

    return strMessage

def message_logistics_parser_CJ(message):
    strMessage = ""
    infom = []
    i = 1
    temp = ""
    try:
        if message.isdigit() == False: raise
        request_headers = {
        'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
        Safari/537.36'), }
        strUrl = "https://trace.cjlogistics.com/tracking/jsp/cmn/Tracking_new.jsp?QueryType=3&pTdNo=" + message
        requestSession = requests.Session()
        Response = requests.get(strUrl, headers = request_headers, verify=certifi.where())
        soup = BeautifulSoup(Response.text, 'html.parser')

        while True:
            info = soup.select('#content > div > table.tepTb02.tepDep02 > tbody > tr:nth-child(%d)' % i)
            if not info:
                info = soup.select('#content > div > table.tepTb02.tepDep02 > tbody > tr:nth-child(%d)' % int(i-1))
                for tag in info:
                    temp += tag.get_text()
                break
            i = i+1
        goods_name = soup.select('#content > div > table.tepTb02.tepDep > tbody > tr:nth-child(6) > td:nth-child(2)')
        goods_name = goods_name[0].get_text().strip()
        goods_name = goods_name.replace('[<td>제품,', '').replace('</td>]', '')
        infom = temp.split('\n')
        for _ in range(len(infom)):
            if infom[_] == "\xa0":
                infom[_] = infom[_].replace(u'\xa0', u'(정보 없음)')
            elif "인수자 : " in infom[_]:
                infom[_] = infom[_].replace('인수자 : ', '')
        strMessage = "/// CJ대한통운 배송조회 ///\n\n품목: %s\n처리장소: %s\n전화번호: %s\n구분: %s\n처리일자: %s\n상대장소(배송장소): %s" % (goods_name, infom[1], infom[2], infom[3], infom[4], infom[5])
    except:
        strMessage = ""
    return strMessage

def message_logistics_parser_HJ(message):
    strMessage = ""
    infom = []
    i = 1
    temp = ""
    try:
        if message.isdigit() == False: raise
        request_headers = {
        'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
        Safari/537.36'), }
        strUrl = "https://www.hanjin.com/kor/CMS/DeliveryMgr/WaybillResult.do?mCode=MN038&wblnum=" + message + "&schLang=KR"
        requestSession = requests.Session()
        Response = requests.get(strUrl, headers = request_headers, verify=certifi.where())
        soup = BeautifulSoup(Response.text, 'html.parser')
        while True:
            info = soup.select('#delivery-wr > div > div.waybill-tbl > table > tbody > tr:nth-child(%d)' % i)
            if not info:
                info = soup.select('#delivery-wr > div > div.waybill-tbl > table > tbody > tr:nth-child(%d)' % int(i-1))
                for tag in info:
                    temp += tag.get_text()
                break
            i = i+1
        infom = temp.split('\n')
        for _ in range(len(infom)):
            if infom[7] == '':
                infom[7] = "(정보 없음)"
        goods_name = soup.select('#delivery-wr > div > table > tbody > tr > td:nth-child(1)')
        goods_name = goods_name[0].get_text().strip()
        strMessage = "/// 한진택배 배송조회 ///\n\n상품명: %s\n날짜: %s\n시간: %s\n상품위치: %s\n배송 진행상황: %s\n전화번호: %s" % (goods_name, infom[1], infom[2], infom[3], infom[5], infom[7])
    except:
        strMessage = ""
    return strMessage

def message_logistics_parser_KP(message):
    strMessage = ""
    infom = []
    i = 1
    temp = ""
    try:
        if message.isdigit() == False: raise
        request_headers = {
        'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
        Safari/537.36'), }
        strUrl = "https://service.epost.go.kr/trace.RetrieveDomRigiTraceList.comm?sid1=" + message
        requestSession = requests.Session()
        Response = requests.get(strUrl, headers = request_headers, verify=certifi.where())
        soup = BeautifulSoup(Response.text, 'html.parser')
        while True:
            info = soup.select('#processTable > tbody > tr:nth-child(%d)' % i)
            if not info:
                info = soup.select('#processTable > tbody > tr:nth-child(%d)' % int(i-1))
                for tag in info:
                    temp += tag.get_text()
                break
            i = i+1
        infom = temp.split('\n')
        for _ in range(len(infom)):
            if '\t' in infom[_]: infom[_] = infom[_].replace('\t', '')
        if infom[5] == '': infom[5] = '접수'
        if infom[5] == '            ': infom[5] = '배달준비'
        strMessage = "/// 우체국택배 배송조회 ///\n\n날짜: %s\n시간: %s\n발생국: %s\n처리현황: %s" % (infom[1], infom[2], infom[3], infom[5])
    except:
        strMessage = ""
    return strMessage

def message_logistics_parser_LG(message):
    strMessage = ""
    infom = []
    i = 1
    temp = ""
    try:
        if message.isdigit() == False:
            raise
        request_headers = {
        'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
        Safari/537.36'), }
        strUrl = "https://www.ilogen.com/web/personal/trace/" + message
        requestSession = requests.Session()
        Response = requests.get(strUrl, headers = request_headers, verify=certifi.where())
        soup = BeautifulSoup(Response.text, 'html.parser')
        while True:
            info = soup.select('body > div.contents.personal.tkSearch > section > div > div.tab_container > div > table.data.tkInfo > tbody > tr:nth-child(%d)' % i)
            if not info:
                info = soup.select('body > div.contents.personal.tkSearch > section > div > div.tab_container > div > table.data.tkInfo > tbody > tr:nth-child(%d)' % int(i-1))
                for tag in info:
                    temp += tag.get_text()
                break
            i = i+1
        infom = temp.split('\n')
        for _ in range(len(infom)):
            if '\t' in infom[_]: infom[_] = infom[_].replace('\t', '')
        infom = [v for v in infom if v]
        temp = ''
        if "전달" in infom[3]:
            temp = '\n인수자: ' + infom[5]
        elif "배달 준비" in infom[3]:
            temp = '\n배달 예정 시간: ' + infom[5]
        strMessage = "/// 로젠택배 배송조회 ///\n\n날짜: %s\n사업장: %s\n배송상태: %s\n배송내용: %s" % (infom[0], infom[1], infom[2], infom[3]) + temp
    except:
        strMessage = ""
    return strMessage

def message_logistics_parser_LT(message):
    strMessage = ""
    infom = []
    i = 1
    temp = ""
    try:
        if message.isdigit() == False:
            raise
        request_headers = {
        'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
        Safari/537.36'), }
        strUrl = "https://www.lotteglogis.com/mobile/reservation/tracking/linkView?InvNo=" + message
        requestSession = requests.Session()
        Response = requests.get(strUrl, headers = request_headers, verify=certifi.where())
        soup = BeautifulSoup(Response.text, 'html.parser')
        info = soup.find("div", "scroll_date_table")
        for tag in info:
            temp += tag.get_text()
        infom = temp.split('\n')
        for _ in range(len(infom)):
            infom[_] = infom[_].replace('\t', '').replace('\r', '').replace(' ', '').replace(u'\xa0', '')
        infom = [v for v in infom if v]
        infom[6] = infom[6][:10] + ' ' + infom[6][10:]
        strMessage = "/// 롯데택배 배송조회 ///\n\n단계: %s\n시간: %s\n현위치: %s\n처리현황: %s" % (infom[5], infom[6], infom[7], infom[8])
    except:
        strMessage = ""
    return strMessage