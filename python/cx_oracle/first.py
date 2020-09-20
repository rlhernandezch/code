import cx_Oracle

Connection= cx_Oracle.connect('soe/soe@ORADB')

ver = Connection.version
print (ver)
__qry = Connection.cursor()

__qry.execute('select table_name from user_tables')
for row in __qry:
    print(row[0])
Connection.close
