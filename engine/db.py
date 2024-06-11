import sqlite3
import csv
conn = sqlite3.connect("bujji.db")

cursor = conn.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key , name varchar(100) , path varchar(1000))"

# cursor.execute(query)

# # query = "INSERT INTO sys_command VALUES(null ,'notepad++','D:\\New folder (3)\\Notepad++\\notepad++.exe')"
# # cursor.execute(query)
# # conn.commit()

# query = 'CREATE TABLE IF NOT EXISTS web_command(id integer primary key , name VARCHAR(100) , url VARCHAR(1000))'

# cursor.execute(query)

query = "INSERT INTO web_command VALUES(null, 'stackoverflow' , 'https://www.stackoverflow.com/')"
cursor.execute(query)
conn.commit()

# cursor.execute(''' CREATE TABLE IF NOT EXISTS contacts (id integer primary key , name varchar(200) , mobile_no varchar(255) , email varchar(255) NULL)''')

# desired_columns_indices = [0,31]

# with open('contacts.csv','r',encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader :
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute('''INSERT INTO contacts (id,'name','mobile_no') VALUES (null , ? ,?)''',tuple(selected_data))
        
# conn.commit()
# conn.close()

# query = "pandu"
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?",('%' + query + '%' + query + '%'))
# results = cursor.fetchall()
# print(results)

# Query to search for
# query = "pandu"
# query = query.strip().lower()

# # Use parameterized query to prevent SQL injection
# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ?", ('%' + query + '%',))
# results = cursor.fetchall()

# print(results[0][0])
# conn.close()
