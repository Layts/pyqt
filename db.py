from mysql.connector import connection
from secrets import *


def get_data():
    '''
    Подключение к БД, возвращает данные из заданной таблицы
    '''
    cnx = connection.MySQLConnection(user=user, password=password,
                                        host=host,
                                        database=database)
    query = 'SELECT name, price, url, descr FROM goods'
    cn = cnx.cursor()
    cn.execute(query)
    data = cn.fetchall()
    cnx.close()
    return data
