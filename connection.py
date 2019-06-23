__author__ = 'monesh'

import cx_Oracle
con = cx_Oracle.connect("system/tiger@localhost:1521/orcl")
cur = con.cursor()
