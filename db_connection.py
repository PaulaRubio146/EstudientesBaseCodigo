import mysql.connector

class MySQLConnectionSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        if MySQLConnectionSingleton._instance is None:
            MySQLConnectionSingleton._instance = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345",
                database="escuela"
            )
        return MySQLConnectionSingleton._instance
