#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/21 14:07
# @Author   : Mr.Gan
# @File     : send_email.py
# @Software : PyCharm


import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart

IMAP = "aplqkpmdwpdgbihf"

POP3 = "044ff0b1c0093668"

# 发件人邮箱账号
my_sender = 'th0701@sina.com'
# 发件人邮箱密码(当时申请smtp给的口令)
my_pass = POP3
# 收件人邮箱账号
my_user = '1050723018@qq.com'


def mail():
    ret = True
    try:
        # 实例化添加邮件附件对象
        msg = MIMEMultipart()
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From'] = formataddr(["谈欢", my_sender])
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To'] = formataddr(["大哥", my_user])
        # 邮件的主题，也可以说是标题
        msg['Subject'] = "自动化测试邮件"
        # MIMEText(邮件正文描述, 邮件类型, 编码)
        msg.attach(MIMEText('今天的自动化报告', 'plain', 'utf-8'))

        # 添加邮件附件
        with open(r'D:\api_zdh\report\2019-08-21\report_10-40-49_.html', 'rb') as f:
            # 设置附件的MIME和文件名，这里是html类型:
            mime = MIMEBase('image', 'html', filename='report_10-40-49_.html')
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename='report_10-40-49_.html')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            msg.attach(mime)
        # 发件人邮箱中的SMTP服务器，端口是465
        server = smtplib.SMTP_SSL("smtp.sina.com", 465)
        # 括号中对应的是发件人邮箱账号、邮箱密码
        server.login(my_sender, my_pass)
        # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(my_sender, [my_user], msg.as_string())
        # 关闭连接
        server.quit()
    # 如果 try 中的语句没有执行，则会执行下面的 ret=False
    except Exception as e:
        print(e)
        ret = False
    return ret


if __name__ == '__main__':

    ret = mail()
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
