#!/usr/bin/env python
#-*- coding:utf8 -*-

import os, sys, logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    filename='/var/log/teleport_restart.log'
)

def run():
    try:
        res1 = os.popen('ps -C tp_core -o pid,cmd').readlines()
        res2 = os.popen('ps -C tp_web -o pid,cmd').readlines()
        if len(res1) < 2 or len(res2) < 2:
            logging.warning("teleport need to restart")
            if os.system("/etc/init.d/teleport restart") == 0: # 0表示命令执行成功，1表示失败
                logging.info("teleport restart successful")
    except:
        logging.error(sys.exc_info()[1])

if __name__ == '__main__':
    run()
