#!/usr/bin/python2
# -*-coding:utf-8-*-
import random

values = ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5']
with open('data/test.txt', 'r') as test, open('data/result.csv', 'w') as result:
    while True:
        line = test.readline().strip()
        if line:
            for i in range(1, 67):
                predict = values[random.randint(0, 5)]
                print predict
                result.writelines(str(i) + ',' + line + ',' + predict + '\n')
        else:
            break

