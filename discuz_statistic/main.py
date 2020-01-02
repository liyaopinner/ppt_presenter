import pymysql.cursors
from discuz_statistic.tables import all_tables
# Connect to the database
connection = pymysql.connect(host='47.98.111.119',
                             user='sql47_98_111_11',
                             password='Xjx3Hsie6d',
                             db='INFORMATION_SCHEMA',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

connection2 = pymysql.connect(host='47.98.111.119',
                             user='sql47_98_111_11',
                             password='Xjx3Hsie6d',
                             db='sql47_98_111_11',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = """SELECT table_name, table_rows
                    FROM INFORMATION_SCHEMA.TABLES
                    WHERE TABLE_SCHEMA = 'sql47_98_111_11' and TABLE_ROWS>0 ORDER BY TABLE_ROWS desc ;
            """
        cursor.execute(sql, )
        result = cursor.fetchall()
        for item in result:
            table_name = item["table_name"]
            table_rows = item["table_rows"]
            print('"{}":{}'.format(table_name, table_rows))
            # if table_rows>10:
            #     continue
            # if table_name not in all_tables:
            #     pass
            #     print(table_name)
            # else:
            #     print("{}({})表的内容如下:".format(table_name,  all_tables[table_name]))
            #     select_sql = "select * from {}".format(table_name)
            #     with connection2.cursor() as cursor2:
            #         cursor2.execute(select_sql, )
            #         result2 = cursor2.fetchall()
            #         for item2 in result2:
            #             print(item2)
            #     print(table_name, all_tables[table_name])
finally:
    connection.close()