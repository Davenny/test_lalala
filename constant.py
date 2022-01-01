import os

USERS = eval(os.environ['USERS'])
SERVER_KEY = os.environ['SERVER_KEY']


LOGIN_API = 'https://app.bupt.edu.cn/uc/wap/login/check'
GET_API = 'https://app.bupt.edu.cn/ncov/wap/default/index'
REPORT_API = 'https://app.bupt.edu.cn/ncov/wap/default/save'

# 当今日没有填报时，在https://app.bupt.edu.cn/ncov/wap/default/index下进行填报，
# 全部填完，不要提交，f12打开控制台，在Console页面下输入代码 console.log(vm.info) 就会得到以下信息，之后每天就默认填以下信息
INFO = r"""{
    "ismoved": 0,
    "jhfjrq": "",
    "jhfjjtgj": "",
    "jhfjhbcc": "",
    "sfxk": 0,
    "xkqq": "",
    "szgj": "",
    "szcs": "",
    "zgfxdq": "0",
    "mjry": "0",
    "csmjry": "0",
    "ymjzxgqk": "已接种",
    "xwxgymjzqk": 3,
    "uid": "32446",
    "tw": "2",
    "sfcxtz": "0",
    "sfyyjc": "0",
    "jcjgqr": "0",
    "jcjg": "",
    "sfjcbh": "0",
    "sfcxzysx": "0",
    "qksm": "",
    "remark": "",
    "address": "湖北省黄石市黄石港区三江共和城",
    "area": "黄石市  黄石港区",
    "province": "湖北省",
    "city": "黄石市",
    "geo_api_info": "{\"type\":\"complete\",\"info\":\"SUCCESS\",\"status\":1,\"fEa\":\"jsonp_641907_\",\"position\":{\"Q\":40.00713,\"R\":116.34569999999997,\"lng\":116.3457,\"lat\":40.00713},\"message\":\"Get ipLocation success.Get address success.\",\"location_type\":\"ip\",\"accuracy\":null,\"isConverted\":true,\"addressComponent\":{\"citycode\":\"010\",\"adcode\":\"110108\",\"businessAreas\":[{\"name\":\"三江共和城\",\"id\":\"110108\",\"location\":{\"Q\":39.99118,\"R\":116.34157800000003,\"lng\":116.341578,\"lat\":39.99118}}],\"neighborhoodType\":\"住宅小区;\",\"neighborhood\":\"三江共和城\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"黄石港花港路\",\"streetNumber\":\"20号\",\"country\":\"中国\",\"province\":\"湖北省\",\"city\":\"黄石市\",\"district\":\"黄石港区\",\"towncode\":\"110108010000\",\"township\":\"花湖街道\"},\"formattedAddress\":\"湖北省黄石市黄石港区三江共和城\",\"roads\":[],\"crosses\":[],\"pois\":[]}",
    "created": 1641012973,
    "sfzx": 0,
    "sfjcwhry": "0",
    "sfcyglq": "0",
    "gllx": "",
    "glksrq": "",
    "jcbhlx": "",
    "jcbhrq": "",
    "sftjwh": "0",
    "sftjhb": "0",
    "fxyy": "开学",
    "bztcyy": "",
    "fjsj": "0",
    "sfjchbry": "0",
    "sfjcqz": "",
    "jcqzrq": "",
    "jcwhryfs": "",
    "jchbryfs": "",
    "xjzd": "",
    "sfsfbh": 0,
    "jhfjsftjwh": "0",
    "jhfjsftjhb": "0",
    "szsqsfybl": 0,
    "sfygtjzzfj": 0,
    "gtjzzfjsj": "",
    "sfsqhzjkk": 0,
    "sqhzjkkys": "",
    "sfjzxgym": 1,
    "sfjzdezxgym": 1,
    "created_uid": 0,
    "id": 16460712,
    "gwszdd": "",
    "sfyqjzgc": "",
    "jrsfqzys": "",
    "jrsfqzfy": ""
        }"""

REASONABLE_LENGTH = 24
TIMEOUT_SECOND = 25

class HEADERS:
    REFERER_LOGIN_API = 'https://app.bupt.edu.cn/uc/wap/login'
    REFERER_POST_API = 'https://app.bupt.edu.cn/ncov/wap/default/index'
    ORIGIN_BUPTAPP = 'https://app.bupt.edu.cn'

    UA = ('Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
          'Mobile/15E148 MicroMessenger/7.0.11(0x17000b21) NetType/4G Language/zh_CN')
    ACCEPT_JSON = 'application/json'
    ACCEPT_HTML = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    REQUEST_WITH_XHR = 'XMLHttpRequest'
    ACCEPT_LANG = 'zh-cn'
    CONTENT_TYPE_UTF8 = 'application/x-www-form-urlencoded; charset=UTF-8'

    def __init__(self) -> None:
        raise NotImplementedError

COMMON_HEADERS = {
    'User-Agent': HEADERS.UA,
    'Accept-Language': HEADERS.ACCEPT_LANG,
}
COMMON_POST_HEADERS = {
    'Accept': HEADERS.ACCEPT_JSON,
    'Origin': HEADERS.ORIGIN_BUPTAPP,
    'X-Requested-With': HEADERS.REQUEST_WITH_XHR,
    'Content-Type': HEADERS.CONTENT_TYPE_UTF8,
}

from typing import Optional
from abc import ABCMeta, abstractmethod

class INotifier(metaclass=ABCMeta):
    @property
    @abstractmethod
    def PLATFORM_NAME(self) -> str:
        """
        将 PLATFORM_NAME 设为类的 Class Variable，内容是通知平台的名字（用于打日志）。
        如：PLATFORM_NAME = 'Telegram 机器人'
        :return: 通知平台名
        """
    @abstractmethod
    def notify(self, *, success, msg, data,username, name) -> None:
        """
        通过该平台通知用户操作成功的消息。失败时将抛出各种异常。
        :param success: 表示是否成功
        :param msg: 成功时表示服务器的返回值，失败时表示失败原因；None 表示没有上述内容
        :return: None
        """

