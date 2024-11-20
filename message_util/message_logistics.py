from bs4 import BeautifulSoup

import datetime
import os

import certifi
import dotenv
import requests


dotenv.load_dotenv()

def message_logistics(message, room, sender):
    if "!택배" in message or "!ㅌㅂ" in message:
        return message_logistics_main(message)
    if "!통관" in message or "!ㅌㄱ" in message:
        return message_custom_tracker(message)
    return None

def message_custom_tracker(message):
    try:
        message = message.replace("!통관", "").replace("!ㅌㄱ", "").replace(" ", "")
        key = os.environ["CUSTOM_API_KEY"]
        year = datetime.date.today().year
        url = "https://unipass.customs.go.kr:38010/ext/rest/cargCsclPrgsInfoQry/retrieveCargCsclPrgsInfo?crkyCn=%s&blYy=%s&hblNo=%s" % (key, year, message)
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "xml")
        name = soup.find("prnm")
        customs_name = soup.find("etprCstm")
        status = soup.find("prgsStts")
        process_time = datetime.datetime.strptime(str(soup.find("prcsDttm").text), "%Y%m%d%H%M%S").strftime("%Y.%m.%d %H:%M:%S")
        return f"/// 관세청 UNIPASS 통관 조회 ///\n\n품명: {name.text}\n입항세관: {customs_name.text}\n통관진행상태: {status.text}\n처리일시: {process_time}"
    except (TypeError, AttributeError):
        return "존재하지 않는 운송장번호이거나 잘못된 형식 혹은 아직 입항하지 않은 화물입니다.\\m사용법: !통관 123456789"

def message_logistics_main(message):
    message = message.replace("!택배", "").replace("!ㅌㅂ", "").replace(" ", "")

    if message == "":
        return "///택배 운송장조회 사용 방법///\\m사용 예시: !택배[운송장번호]\nex)!택배1234567890\n지원중인 택배사: 우체국택배, 대한통운(CJ, 대통), 로젠택배, 롯데택배, 한진택배\n만약 통관 중인 택배라면 우선적으로 통관 상황을 조회합니다."

    str_message = message_custom_tracker(message)
    if "존재하지 않는 운송장" in str_message:
        str_message = message_logistics_parser(message)
    else:
        tmp_message = message_logistics_parser(message)
        if "존재하지 않는 운송장" in tmp_message:
            str_message = f"{str_message}\\m현재 택배사에 인계되지 않은 화물입니다."
        else:
            str_message = f"{str_message}\\m{tmp_message}"

    return str_message

def message_logistics_parser(message):
    logistics = [message_logistics_parser_cj,
                message_logistics_parser_hanjin,
                message_logistics_parser_koreapost,
                message_logistics_parser_logen,
                message_logistics_parser_lotte]

    for parser in logistics:
        str_message = parser(message)
        if str_message: return str_message

    str_message = "미집하된 택배이거나 존재하지 않는 운송장 번호입니다.\\m사용 예시: !택배[운송장번호]\nex)!택배1234567890\n지원중인 택배사: 우체국택배, 대한통운(CJ, 대통), 로젠택배, 롯데택배, 한진택배"

    return str_message

def message_logistics_parser_cj(message):
    i = 1
    temp = ""
    try:
        if not message.isdigit(): raise TypeError
        request_headers = {
            "User-Agent" : ("Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
            Safari/537.36")
        }
        str_url = "https://trace.cjlogistics.com/tracking/jsp/cmn/Tracking_new.jsp?QueryType=3&pTdNo=" + message
        request_session = requests.Session()
        request_response = request_session.get(str_url, headers = request_headers, verify=certifi.where())
        soup = BeautifulSoup(request_response.text, "html.parser")

        while True:
            info = soup.select("#content > div > table.tepTb02.tepDep02 > tbody > tr:nth-child(%d)" % i)
            if not info:
                info = soup.select("#content > div > table.tepTb02.tepDep02 > tbody > tr:nth-child(%d)" % int(i-1))
                for tag in info:
                    temp += tag.get_text()
                break
            i = i+1
        goods_name = soup.select("#content > div > table.tepTb02.tepDep > tbody > tr:nth-child(6) > td:nth-child(2)")
        goods_name = goods_name[0].get_text().strip()
        goods_name = goods_name.replace("[<td>제품,", "").replace("</td>]", "")
        infom = temp.split("\n")
        for _ in range(len(infom)):
            if infom[_] == "\xa0":
                infom[_] = infom[_].replace(u"\xa0", u"(정보 없음)")
            elif "인수자 : " in infom[_]:
                infom[_] = infom[_].replace("인수자 : ", "")
        return f"/// CJ대한통운 배송조회 ///\n\n품목: {goods_name}\n처리장소: {infom[1]}\n전화번호: {infom[2]}\n구분: {infom[3]}\n처리일자: {infom[4]}\n상대장소(배송장소): {infom[5]}"
    except (TypeError, IndexError):
        return ""

def message_logistics_parser_hanjin(message):
    i = 1
    temp = ""
    try:
        if not message.isdigit(): raise TypeError
        request_headers = {
            "User-Agent" : ("Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
            Safari/537.36")
        }
        str_url = "https://www.hanjin.com/kor/CMS/DeliveryMgr/WaybillResult.do?mCode=MN038&wblnum=" + message + "&schLang=KR"
        request_session = requests.Session()
        request_response = request_session.get(str_url, headers = request_headers, verify=certifi.where())
        soup = BeautifulSoup(request_response.text, "html.parser")
        while True:
            info = soup.select("#delivery-wr > div > div.waybill-tbl > table > tbody > tr:nth-child(%d)" % i)
            if not info:
                info = soup.select("#delivery-wr > div > div.waybill-tbl > table > tbody > tr:nth-child(%d)" % int(i-1))
                for tag in info:
                    temp += tag.get_text()
                break
            i = i+1
        infom = temp.split("\n")
        for _ in range(len(infom)):
            if infom[7] == "":
                infom[7] = "(정보 없음)"
        goods_name = soup.select("#delivery-wr > div > table > tbody > tr > td:nth-child(1)")
        goods_name = goods_name[0].get_text().strip()
        return f"/// 한진택배 배송조회 ///\n\n상품명: {goods_name}\n날짜: {infom[1]}\n시간: {infom[2]}\n상품위치: {infom[3]}\n배송 진행상황: {infom[5]}\n전화번호: {infom[7]}"
    except (TypeError, IndexError):
        return ""

def message_logistics_parser_koreapost(message):
    i = 1
    temp = ""
    try:
        if not message.isdigit(): raise TypeError
        request_headers = {
        "User-Agent" : ("Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
        Safari/537.36"), }
        str_url = "https://service.epost.go.kr/trace.RetrieveDomRigiTraceList.comm?sid1=" + message
        request_session = requests.Session()
        request_response = request_session.get(str_url, headers = request_headers, verify=certifi.where())
        soup = BeautifulSoup(request_response.text, "html.parser")
        while True:
            info = soup.select("#processTable > tbody > tr:nth-child(%d)" % i)
            if not info:
                info = soup.select("#processTable > tbody > tr:nth-child(%d)" % int(i-1))
                for tag in info:
                    temp += tag.get_text()
                break
            i = i+1
        infom = temp.split("\n")
        for _ in range(len(infom)):
            if "\t" in infom[_]: infom[_] = infom[_].replace("\t", "")
        if infom[5] == "": infom[5] = "접수"
        if infom[5] == "            ": infom[5] = "배달준비"
        return f"/// 우체국택배 배송조회 ///\n\n날짜: {infom[1]}\n시간: {infom[2]}\n발생국: {infom[3]}\n처리현황: {infom[5]}"
    except (TypeError, IndexError):
        return ""

def message_logistics_parser_logen(message):
    i = 1
    temp = ""
    try:
        if not message.isdigit():
            raise TypeError
        request_headers = {
        "User-Agent" : ("Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
        Safari/537.36"), }
        str_url = "https://www.ilogen.com/web/personal/trace/" + message
        request_session = requests.Session()
        request_response = request_session.get(str_url, headers = request_headers, verify=certifi.where())
        soup = BeautifulSoup(request_response.text, "html.parser")
        while True:
            info = soup.select("body > div.contents.personal.tkSearch > section > div > div.tab_container > div > table.data.tkInfo > tbody > tr:nth-child(%d)" % i)
            if not info:
                info = soup.select("body > div.contents.personal.tkSearch > section > div > div.tab_container > div > table.data.tkInfo > tbody > tr:nth-child(%d)" % int(i-1))
                for tag in info:
                    temp += tag.get_text()
                break
            i = i+1
        infom = temp.split("\n")
        for _ in range(len(infom)):
            if "\t" in infom[_]: infom[_] = infom[_].replace("\t", "")
        infom = [v for v in infom if v]
        temp = ""
        if "전달" in infom[3]:
            temp = "\n인수자: " + infom[5]
        elif "배달 준비" in infom[3]:
            temp = "\n배달 예정 시간: " + infom[5]
        return f"/// 로젠택배 배송조회 ///\n\n날짜: {infom[0]}\n사업장: {infom[1]}\n배송상태: {infom[2]}\n배송내용: {infom[3]}" + temp
    except (TypeError, IndexError):
        return ""

def message_logistics_parser_lotte(message):
    temp = ""
    try:
        if not message.isdigit():
            raise TypeError
        request_headers = {
        "User-Agent" : ("Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
        Safari/537.36"), }
        str_url = "https://www.lotteglogis.com/mobile/reservation/tracking/linkView?InvNo=" + message
        request_session = requests.Session()
        request_response = request_session.get(str_url, headers = request_headers, verify=certifi.where())
        soup = BeautifulSoup(request_response.text, "html.parser")
        info = soup.find("div", "scroll_date_table")
        for tag in info:
            temp += tag.get_text()
        infom = temp.split("\n")
        for _ in range(len(infom)):
            infom[_] = infom[_].replace("\t", "").replace("\r", "").replace(" ", "").replace(u"\xa0", "")
        infom = [v for v in infom if v]
        infom[6] = infom[6][:10] + " " + infom[6][10:]
        return f"/// 롯데택배 배송조회 ///\n\n단계: {infom[5]}\n시간: {infom[6]}\n현위치: {infom[7]}\n처리현황: {infom[8]}"
    except (TypeError, IndexError):
        return ""