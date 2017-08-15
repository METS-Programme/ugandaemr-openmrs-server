import MySQLdb

from MySQLdb.cursors import DictCursor


class Database:
    host = 'localhost'
    user = 'openmrs'
    password = 'openmrs'
    db = 'ugandaemr'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.connection.ping(True)
        self.connection.set_character_set('utf8')
        self.cursor = self.connection.cursor(DictCursor)
        self.cursor.execute('SET NAMES utf8;')
        self.cursor.execute('SET CHARACTER SET utf8;')
        self.cursor.execute('SET character_set_connection=utf8;')

    def insert(self, q, d):
        try:
            self.cursor.execute(q, d)
            self.connection.commit()
            return self.cursor.lastrowid

        except _mysql.Error as e:
            self.connection.rollback()
            try:
                print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            except IndexError:
                print ("MySQL Error: %s" % str(e))

    def insert_bulk(self, q, data):
        try:
            self.cursor.executemany(q, data)
            self.connection.commit()
        except _mysql.Error as e:
            self.connection.rollback()
            try:
                print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            except IndexError:
                print ("MySQL Error: %s" % str(e))

    def query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def query_one(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def query_with_data(self, query, data):
        self.cursor.execute(query, data)
        return self.cursor.fetchall()

    def query_one_with_data(self, query, data):
        query = query % data
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def __del__(self):
        self.connection.close()
