
# from DBEngine import DBEngine

# class MySQLEngine(DBEngine):
#     def __init__(self, host, user, password, database):
#         self.conn = mysql.connector.connect(
#             host=host, user=user, password=password, database=database
#         )
#         self.cursor = self.conn.cursor()

#     def execute(self, sql, params=()):
#         self.cursor.execute(sql, params)

#     def fetch(self, sql, params=()):
#         self.cursor.execute(sql, params)
#         return self.cursor.fetchall()

#     def commit(self):
#         self.conn.commit()

#     def rollback(self):
#         self.conn.rollback()

#     def close(self):
#         if not self.cursor:
#             self.cursor.close()
#         if not self.conn:
#             self.conn.close()