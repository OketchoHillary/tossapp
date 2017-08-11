import sqlite3

sqlite_file = 'db.sqlite3'    # name of the sqlite database file
table_name = 'accounts_tuser'   # name of the table to be queried
column_name = 'username'

conn = sqlite3.connect(sqlite_file)
conn.row_factory = sqlite3.Row
c = conn.cursor()

c.execute('SELECT * FROM {tn} WHERE {cn}="{usr}"'.\
        format("emma",tn=table_name, cn=column_name,usr="emma"))
all_rows = c.fetchone()

print all_rows['username']