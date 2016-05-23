#!/usr/bin/python2
# -*-coding:utf-8-*-

import logging

log = None

def init_log(log_name):
    # 日志输出格式
    fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(levelname)s - %(name)s - %(message)s'
    formatter = logging.Formatter(fmt)

    # 创建一个handler，用于输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    log = logging.getLogger(log_name)
    log.addHandler(console_handler)
    log.setLevel(logging.DEBUG)

    return log



def test():
    # 关键任务开始前打日志
    log.info('test方法开始执行')

    # 关键信息打印出来
    log.info('total %d url to crawler', 10)

    # 无关紧要的错误使用warn
    try:
       raise Exception('something wainning')
    except Exception, e:
        log.warn('执行text出现异常')

    # 严重错误使用error
    try:
       raise Exception('something error')
    except Exception, e:
        log.error('执行text出现异常')
        # 下面应该把异常抛出去

    # 关键任务结束打日志
    log.info('test方法执行完成')


if __name__ == '__main__':
    log = init_log('log_demo')
    test()