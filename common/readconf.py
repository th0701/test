#读取配置文件
import os
import configparser
from common import getpath

path = getpath.getpath("config","config.ini")
conf = configparser.ConfigParser()

conf.read(path, encoding="utf8")

url = conf.get("API", "api_weath")





