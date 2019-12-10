import pymysql
import pymysql.cursors

query = 'select * from city'

print(query)

connection = pymysql.connect(host='epuentes-server',
                             user='root',
                             password='power',
                             db='world',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


try:
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = 'SELECT * FROM city'
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print('tet')

finally:
    connection.close()
    