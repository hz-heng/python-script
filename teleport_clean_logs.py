#!/usr/bin/env python
#-*- coding:utf8 -*-

import os, sys, logging, shutil
from datetime import date
import MySQLdb as mdb

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    filename='/var/log/teleport_clean_logs.log'
)

def clean_logs():
    SSH_DIR = '/usr/local/teleport/data/replay/ssh/' 
    RDP_DIR = '/usr/local/teleport/data/replay/rdp/'
    sort_clean(SSH_DIR)
    sort_clean(RDP_DIR)

def sort_clean(dir):
    today = date.today()
    files = list(os.listdir(dir))
    for file in files:
        file_stamp = os.path.getmtime(dir + file)
        file_date = date.fromtimestamp(file_stamp)
        if (today - file_date).days > 183: # 清理183天(半年)前的日志
            file_id = int(file)
            try:
                conn = mdb.connect(
                    host='localhost',
                    user='',
                    passwd='',
                    db=''
                )
                cursor = conn.cursor()
                cursor.execute('delete from tp_log where id = {0}'.format(file_id))
                shutil.rmtree(dir + file)
                conn.commit()
                logging.info("{0}日志已删除".format(file))
            except:
                logging.error(sys.exc_info()[1])
                conn.rollback()
            finally:
                conn.close()

if __name__ == '__main__':
    clean_logs()
