import mysql.connector as sql

def createcustomertable():
    create_table_query = '''
                    CREATE TABLE IF NOT EXISTS CUSTOMERS (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(30),
                    password VARCHAR(300),
                    name VARCHAR(40),
                    email VARCHAR(80),
                    age INTEGER,
                    city VARCHAR(40),
                    balance INTEGER,
                    account_number INTEGER,
                    status BOOLEAN)'''
    cursor.execute(create_table_query)
    mydb.commit()

def db_query(query):
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# Connect to the database
mydb = sql.connect(
    host='localhost',
    user='root',
    password='2254',
    database='Bbank'
)
cursor = mydb.cursor()
createcustomertable()
