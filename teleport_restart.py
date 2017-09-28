#!/usr/bin/env python
#-*- coding:utf8 -*-

import os, sys, time, logging

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s') #设定日志格式
while True:
    time.sleep(4)
    try:
        res = os.popen('ps -C tp_core -o pid,cmd').readlines() #查询tp_core进程
        if len(res) < 2: #res长度小于2，tp_core进程不存在
            logging.warning("teleport core need restart")
            time.sleep(3)
            os.system("service teleport restart") #重启服务
    except:
        logging.warning("Error", sys.exc_info()[1])
