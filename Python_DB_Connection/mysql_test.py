import pymysql

try:
    connection = pymysql.connect(
        host = "localhost",
        user = "python_user",
        password = "PyUser#2026Secure!",
        database = "python_db")
        # port = 3306)
    with connection.cursor() as cursor:

        print("connected successfully!")
        
        print("------------------------------------------------------------")
        #####################################################################
        # either we create database in mysql terminal itself or do it here by the code below
        # if we are creating it here , remove the database="python_db" argument and then do this.

        # cursor.execute("create database python_db")

        # once the db is created we can mension it in the connect() function, 
        # so that while accessing tables  we dont have to do db_name.table_name , instead we can directly do table_name
        
        #####################################################################
        
        
        print("------------------------------------------------------------")
        #####################################################################
        cursor.execute("SELECT VERSION()") #DO NOT GIVE SEMI COLON AT THE END OF QUERIES
        print("MySQL version: ",cursor.fetchone()[0])
        #####################################################################



        print("------------------------------------------------------------")
        #####################################################################
        cursor.execute("Show tables")
        print("Tables: ",cursor.fetchall())
        #####################################################################


        print("------------------------------------------------------------")
        #####################################################################
        cursor.execute("CREATE TABLE IF NOT EXISTS exam_score (student_id INT, name VARCHAR(100),marks DECIMAL(5,2))")
        print("table is created!!")
        #####################################################################



        print("------------------------------------------------------------")
        #####################################################################
        #Insertion

        ###############---To add single single rows at a time---###################

        # cursor.execute('INSERT INTO exam_score(student_id,name,marks) VALUES (1,"JOHN",90)')
        # print("one record is inserted into the table")

        # cursor.execute('INSERT INTO exam_score(student_id,name,marks) VALUES (2,"RAJ",96)')
        # print("one record is inserted into the table")

        # cursor.execute('INSERT INTO exam_score(student_id,name,marks) VALUES (3,"MOHAN",80)')
        # print("one record is inserted into the table")

        ################--- To add multiple rows at a time---#####################

        # query = 'INSERT INTO exam_score(student_id,name,marks) VALUES (%s,%s,%s)'
        # values = [(4,"SONU",75),(5,"MONU",25),(6,"LOLAN",45)]
        # cursor.executemany(query,values)
        # print(cursor.rowcount," records are inserted into the table")
        #####################################################################


        print("------------------------------------------------------------")
        # Deletion
        #####################################################################
        # cursor.execute("DELETE FROM exam_score where marks = 90")
        # print(cursor.rowcount,"Record(s) deleted")
        #####################################################################


        print("------------------------------------------------------------")
        #Updation
        #####################################################################
        cursor.execute("update exam_score set marks = 20 where student_id = 5")
        print(cursor.rowcount,"Record(s) updated")
        #####################################################################

        print("------------------------------------------------------------")
        #####################################################################
        cursor.execute("Show tables")
        print("Tables: ",cursor.fetchall())
        #####################################################################


        print("------------------------------------------------------------")
        # Reading
        #####################################################################
        cursor.execute("SELECT * FROM exam_score")
        for row in cursor.fetchall():
            print(row)
        #####################################################################


        #####################################################################
        # Commiting the changes
        connection.commit()
        #####################################################################

except pymysql.MySQLError as error:
    print("MySQL connection failed",error)

finally:
    connection.close()
