import unittest


from common import log_conf
import unittest
import requests
from common import readconf
from common import request


param1 = {
    "key": "b4a415d875b91358b4f46ca3c1c08bea",
    "cityname": "武汉"
}

class Mytestcase(unittest.TestCase):

    logs = log_conf.MyLog()
    def setUp(self):
        print("开始测试")

    def tearDown(self):
        print("结束测试")

    def test_01(self):
        self.assertEqual(request.doRequest(param1),("200","successed!"))


    def test_02(self):
        param2 = {
            "key": "b4a415d875b91358b4f46ca3c1c08bea",
            "cityname": ""
        }
        self.assertEqual(request.doRequest(param2), ("201", "Error Cityname!"))
