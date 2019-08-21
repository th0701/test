#配置日志

from common import getpath
import os
import time
import logging


class MyLog():

    def __init__(self):
        err_log = getpath.getpath("logs","err_log")
        info_log = getpath.getpath("logs","info_log")
        if not os.path.isdir(err_log):
            os.mkdir(err_log)
        if not os.path.isdir(info_log):
            os.mkdir(info_log)

        time_name = time.strftime("%Y-%m-%d")
        self.err_log_time = os.path.join(err_log, time_name)
        self.info_log_time = os.path.join(info_log, time_name)
        if not os.path.isdir(self.err_log_time):
            os.mkdir(self.err_log_time)
        if not os.path.isdir(self.info_log_time):
            os.mkdir(self.info_log_time)
        self.th = logging.Formatter("%(levelname)s %(filename)s %(asctime)s %(lineno)s %(message)s")
        self.c = logging.StreamHandler()
        self.c.setFormatter(self.th)

    def error(self, msg):
        logger = logging.getLogger()
        logger.setLevel("ERROR")
        #配置文件路径
        filename = os.path.join(self.err_log_time, "err.txt")
        eh = logging.FileHandler(filename, "a", encoding="utf8")
        eh.setFormatter(self.th)
        # 判断logger属性字典 handlers是否为空，为空则添加 句柄对象
        if logger.__dict__["handlers"] != []:
            # 判断handlers的value 下标0的句柄对象，是否与这一次调用时创建的eh对象相同
            # 如果不相同，则重新设置 handlers的value为[],然后添加eh
            # 如果 与这一次 eh对象相同，则不做任何操作
            if logger.__dict__["handlers"][0] != eh:
                logger.__dict__["handlers"] = []
                logger.addHandler(eh)
                logger.addHandler(self.c)
        else:
            logger.addHandler(eh)
            logger.addHandler(self.c)
        logger.error(msg)

    def info(self, msg):
        logger = logging.getLogger()
        logger.setLevel("INFO")
        # 配置文件路径
        filename = os.path.join(self.info_log_time, "info.txt")
        ih = logging.FileHandler(filename, "a", encoding="utf8")
        ih.setFormatter(self.th)
        # 判断logger属性字典 handlers是否为空，为空则添加 句柄对象
        if logger.__dict__["handlers"] != []:
            # 判断handlers的value 下标0的句柄对象，是否与这一次调用时创建的eh对象相同
            # 如果不相同，则重新设置 handlers的value为[],然后添加eh
            # 如果 与这一次 eh对象相同，则不做任何操作
            if logger.__dict__["handlers"][0] != ih:
                logger.__dict__["handlers"] = []
                logger.addHandler(ih)
                logger.addHandler(self.c)
        else:
            logger.addHandler(ih)
            logger.addHandler(self.c)
        logger.info(msg)

if __name__ == "__main__":
    logs = MyLog()
    logs.error("你好")
    logs.info("大家好")
