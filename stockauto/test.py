import win32com.client
 
 
# 연결 여부 체크
objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
bConnect = objCpCybos.IsConnect
if (bConnect == 0):
    print("PLUS가 정상적으로 연결되지 않음. ")
    exit()
 
# 종목코드 리스트 구하기
objCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
codeList = objCpCodeMgr.GetStockListByMarket(1) #거래소
codeList2 = objCpCodeMgr.GetStockListByMarket(2) #코스닥
 
 
print("거래소 종목코드", len(codeList))
for i, code in enumerate(codeList):
    secondCode = objCpCodeMgr.GetStockSectionKind(code)
    name = objCpCodeMgr.CodeToName(code)
    stdPrice = objCpCodeMgr.GetStockStdPrice(code)
    print(i, code, secondCode, stdPrice, name)
 
print("코스닥 종목코드", len(codeList2))
for i, code in enumerate(codeList2):
    secondCode = objCpCodeMgr.GetStockSectionKind(code)
    name = objCpCodeMgr.CodeToName(code)
    stdPrice = objCpCodeMgr.GetStockStdPrice(code)
    print(i, code, secondCode, stdPrice, name)
 
print("거래소 + 코스닥 종목코드 ",len(codeList) + len(codeList2))

# import sys
# import win32com.client
# import ctypes
# import time
# ################################################
# # PLUS 공통 OBJECT
# g_objCodeMgr = win32com.client.Dispatch('CpUtil.CpCodeMgr')
# g_objCpStatus = win32com.client.Dispatch('CpUtil.CpCybos')
# g_objCpTrade = win32com.client.Dispatch('CpTrade.CpTdUtil')
# ################################################
# # PLUS 실행 기본 체크 함수
# def InitPlusCheck():
#     # 프로세스가 관리자 권한으로 실행 여부
#     if ctypes.windll.shell32.IsUserAnAdmin():
#         print('정상: 관리자권한으로 실행된 프로세스입니다.')
#     else:
#         print('오류: 일반권한으로 실행됨. 관리자 권한으로 실행해 주세요')
#         return False
#     # 연결 여부 체크
#     if (g_objCpStatus.IsConnect == 0):
#         print("PLUS가 정상적으로 연결되지 않음. ")
#         return False
#     # 주문 관련 초기화
#     if (g_objCpTrade.TradeInit(0) != 0):
#         print("주문 초기화 실패")
#         return False
#     return True