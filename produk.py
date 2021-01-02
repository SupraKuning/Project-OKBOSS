import sqlite3
import database

conn = sqlite3.connect('database.db')
c = conn.cursor()

#perintah sql menampilkan data pada table
c.execute('SELECT * FROM Produk')

#perulangan untuk membuat data tampil semua
for row in c.fetchall():
      print(row)
      
c.close()
conn.close()