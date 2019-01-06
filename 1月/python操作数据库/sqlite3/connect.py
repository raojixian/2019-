# coding:utf-8
import sqlite3
def connectDatabase(file):
    conn = sqlite3.connect(file)
    return conn

if __name__ == '__main__':
    file = 'database/test.db'
    connectDatabase()
    print('success')