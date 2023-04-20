
#This is to test the database connection
import unittest 
import mysql.connector


class TestDatabaseConnection(unittest.TestCase):
    def test_connection(self):
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            database = "mydatabase",
            
        )
        self.assertTrue(conn.is_connected())

if __name__ == '__main__':
    unittest.main()