'''
Created on 2015-6-4

@author: yujing
'''
#encoding=utf-8
import MySQLdb
import sys

import MySQLdb

con= MySQLdb.connect(host="117.79.93.202",user="bi",passwd="bi_DFsdfiIFDH",db="bi")

cursor =con.cursor()

sql ="select * from info_geteducation limit 1"
sql1 ="insert into cdinfo values(0,%s,%s,%s,%s,%s)" #插入

cursor.execute(sql)

row=cursor.fetchone()

print row

cursor.close()

con.close()