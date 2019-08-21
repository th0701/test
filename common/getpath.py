#编辑方法获取路径
import os
import time


def getpath(path,filename):
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),path,filename)
    return path

def jiutu(driver):
    # 报错 截图
    time_name = time.strftime("%Y-%m-%d")
    img_time_name = getpath("api_err_img", time_name)
    if not os.path.isdir(img_time_name):
        os.mkdir(img_time_name)
    # 时分秒
    time_name1 = "api_err_" + time.strftime("%H-%M-%S") + "_img.png"
    driver.get_screenshot_as_file(os.path.join(img_time_name, time_name1))
