import sqlite3
## Connect to sqlite database
connection = sqlite3.connect("student.db")
## create a cursor object to insert records, create table, retrive results
cursor = connection.cursor()
## create the table
table_info = """
    Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SEACTION VARCHAR(25), MARKS INT);

"""
cursor.execute(table_info)

## insert some records
cursor.execute('''INSERT INTO STUDENT values('Prakash Singh', 'Web Developer', 'A', 70)''')
cursor.execute('''INSERT INTO STUDENT values('Amit Nigam', 'SDS Tools', 'B', 80)''')
cursor.execute('''INSERT INTO STUDENT values('SanJay', 'Web Developer', 'A', 35)''')
cursor.execute('''INSERT INTO STUDENT values('HAziq', 'DEVOPS', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT values('Pritam Kumar', 'Java Developer', 'B', 50)''')

## Display all the records
print("The insered records are")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

## close the connection
connection.commit()
connection.close()

