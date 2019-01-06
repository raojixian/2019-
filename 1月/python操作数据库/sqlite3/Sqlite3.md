sqlite3
一般流程
conn = sqlite3.connect(database)
c = conn.cursor()
c.execute(sql语句)
conn.commit()
conn.close()
1.连接数据库 
2.创建表 
    '''
        CREATE TABLE USER(
        ID INT PRIMARY KEY NOT NULL,
        NAME  TEXT NOT NULL,
        AGE  INT NOT NULL,
        ADDRESS CHAR(50),
        SALARY REAL
        );
    '''
3.插入数据
    "INSERT INTO USER (ID,NAME,AGE,ADDRESS,SALARY)"
          "VALUES(1,'RAOJIXIAN',32,'CHINA',2000.00)"
4.update
    "UPDATE USER SET SALARY = 100 WHERE ID = 1"
5.delete
    "DELETE FROM USER WHERE ID = 2"
6.查询数据
    "SELECT id,name,salary FROM USER"
    打印数据 for循环
