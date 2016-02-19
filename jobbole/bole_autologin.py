#-*-coding:utf-8-*-
from email.header import Header
from email.mime.text import MIMEText
import json
import requests
import smtplib

__author__ = 'wendale'

user_name = ''
password = ''
login_url = 'http://www.jobbole.com/wp-admin/admin-ajax.php'
login_form_data = 'action=user_login&user_login=%s&user_pass=%s' % (user_name, password)
login_headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8',
'Cache-Control': 'no-cache',
'Connection': 'keep-alive',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Origin': 'http://www.jobbole.com',
'Pragma': 'no-cache',
'Referer': 'http://www.jobbole.com/login/?redirect=http%3A%2F%2Fwww.jobbole.com%2F',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}

sign_in_data = 'action=get_login_point'


def send_email(err_msg):
    sender = ''
    receiver = ''
    subject = '博乐在线自动签到失败'
    smtpserver = ''
    username = ''
    password = ''

    err_msg = eval("u'%s'" % err_msg)
    msg = MIMEText(err_msg, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


def check_result(response, error_message):
    json_result = json.loads(response.content)
    if json_result['jb_result'] != 0:
        raise Exception(error_message + u'，返回结果：' + response.content)

try:
    #登陆获得cookies
    login_response = requests.post(login_url, data=login_form_data, headers=login_headers)
    check_result(login_response, u'登陆失败')
    cookies = login_response.cookies
    #签到
    login_headers['Referer'] = 'http://www.jobbole.com/'
    sign_in_response = requests.post(login_url, data=sign_in_data, cookies=cookies, headers=login_headers)
    check_result(sign_in_response, u'签到失败')
except Exception, e:
    send_email(e.message)

