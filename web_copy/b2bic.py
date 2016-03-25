#!/usr/bin/python2
# -*-coding:utf-8-*-
import random
import requests
import datetime

__author__ = 'wendale'


# class PocketHeader:


def make_pocket_header(xml_length):
        version = 'A001'
        target = '02'
        encoding = '02'
        protocol = '02'
        customer_code = '00102079900001231000'
        length = '%010d' % xml_length
        tran_code = '  sc00'
        operator_code = '%5c' % ' '
        service_code = '01'

        now = datetime.datetime.now()
        tran_date = now.strftime('%Y%m%d')
        tran_time = now.strftime('%H%M%S')
        tran_serial_num = tran_date + tran_time + ('%06d' % random.randint(0, 999999))
        return_code = '000000'
        return_msg = '%100c' % ' '
        follow_pocket_flag = '0'
        request_turn = '000'
        sign_flag = '1'
        sign_format = '1'
        sign_method = '%12c' % ' '
        sign_length = '%010d' % 0
        attachment_num = '0'

        return ''.join([version, target, encoding, protocol, customer_code, length, tran_code, operator_code,
                      service_code, tran_date, tran_time, tran_serial_num, return_code, return_msg,
                      follow_pocket_flag, request_turn, sign_flag, sign_format, sign_method, sign_length,
                        attachment_num])


def test_file01():
    xml = '<?xml version="1.0" encoding="UTF-8" ?><Result><TradeSn>100</TradeSn><FileName>test.txt</FileName><FilePath></FilePath></Result>'

    post_entity = make_pocket_header(len(xml)) + xml
    headers = {'content-type': 'text/html; charset=utf8'}
    response = requests.post('http://127.0.0.1:7072/', data=post_entity)

    print post_entity
    print response.content.decode('gbk')


if __name__ == '__main__':
    test_file01()