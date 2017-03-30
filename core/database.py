import MySQLdb


class Database:
    host = 'localhost'
    user = 'openmrs'
    password = 'openmrs'
    db = 'ugandaemr'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.connection.set_character_set('utf8')
        self.cursor = self.connection.cursor()
        self.cursor.execute('SET NAMES utf8;')
        self.cursor.execute('SET CHARACTER SET utf8;')
        self.cursor.execute('SET character_set_connection=utf8;')

    def insert(self, q, d):
        try:
            self.cursor.execute(q, d)
            self.connection.commit()
            return self.cursor.lastrowid

        except MySQLdb.Error, e:
            self.connection.rollback()
            try:
                print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
            except IndexError:
                print "MySQL Error: %s" % str(e)

    def insert_bulk(self, q, data):
        try:
            self.cursor.executemany(q, data)
            self.connection.commit()
        except MySQLdb.Error, e:
            self.connection.rollback()
            try:
                print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
            except IndexError:
                print "MySQL Error: %s" % str(e)

    def query(self, query):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query)
        return cursor.fetchall()

    def query_one(self, query):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query)
        return cursor.fetchone()

    def query_with_data(self, query, data):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query, data)
        return cursor.fetchall()

    def query_one_with_data(self, query, data):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)

        query = query % data
        cursor.execute(query)
        return cursor.fetchone()

    def __del__(self):
        self.connection.close()
