import sqlite3

import _sqlite3

conn = sqlite3.connect("test.db")
print("opened databese sucessfully")

conn.execute("delete from Company where id = 2;")
conn.commit()
print("total number of rows deleted :", conn.total_changes)

cursor = conn.execute("select id, name address, salary from company")
for row in cursor;
    print("id = ",row[0])
    print("name = ", row[1])
    print("address = ", row[2])
    print("salary = ", row[3]), "\n"

print("operation done successfully")
conn.close()