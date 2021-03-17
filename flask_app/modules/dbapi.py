import pymysql


def get_mysql_conn(env=None):
    return dbapi(env)


class dbapi(object):
    def __init__(self, env=None):
        self.db_host = env['host']
        self.db_port = env['port']
        self.db_user = env['user']
        self.db_pwd = env['password']
        self.db_name = env['db_name']
        self._connect = pymysql.connect(host=self.db_host,
                                        port=int(self.db_port),
                                        user=self.db_user,
                                        password=self.db_pwd,
                                        charset='utf8',
                                        db=self.db_name,
                                        init_command='set names utf8')

    def queryall(self, sql, params=None):
        with self._connect.cursor() as cursor:
            try:
                if params:
                    cursor.execute(sql, params)
                else:
                    cursor.execute(sql)
            except:
                exit()
            result = cursor.fetchall()
        return result

    def update(self, sql, params=None):
        cursor = self._connect.cursor()
        try:
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            self._connect.commit()
        finally:
            cursor.close()

    def close(self):
        if self._connect:
            self._connect.close()
