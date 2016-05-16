#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-16 00:00:31
# @Author  : xchaoinfo (xchaoinfo@qq.com)
# @Link    : https://github.com/xchaoinfo
# @Version : v.0.0

import mysql.connector as my
import configparser


def get_config():
    config = configparser.ConfigParser()
    config.read("statics/config.ini", encoding="utf-8")
    sql = config['mysql']
    user = sql['user']
    password = sql['password']
    host = sql['host']
    return user, password, host


def connect_mysql(db):
    user, password, host = get_config()
    conn = my.connect(user=user, password=password, host=host, database=db)
    cur = conn.cursor()
    # do some sql
    cur.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    connect_mysql('xchao')
