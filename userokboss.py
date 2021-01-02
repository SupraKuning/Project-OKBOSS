import sqlite3
import database

class User(database.getDatabase):
   def tambahPengguna(self):
        x = None
        level = str(input('Masukkan level : '))
        idPengguna = int(input('Masukkan ID Pengguna : '))
        namaPengguna = str(input('Masukkan Nama Pengguna : '))
        password = str(input('Masukkan Password : '))

        query = "INSERT INTO Pengguna (Level, ID, Nama, Password) VALUES('{}', '{}', '{}', '{}');".format(level, idPengguna, namaPengguna, password)
        self.cursor.execute(query)
        self.database.commit()

        cont = str('Selamat anda berhasil menambahkan')
        if level == 'Boss':
            Boss(level,idPengguna,namaPengguna,password)
            data.append(x)
            print('Data Boss berhasil ditambahkan')
        elif level == 'Staff':
            Staff(level,idPengguna,namaPengguna,password)
            data.append(x)
            print('Data Staff berhasil ditambahkan')
        elif level == 'Pelanggan':
            Pelanggan(level,idPengguna,namaPengguna,password)
            data.append(x)
            print('Data Pelanggan berhasil ditambahkan')
        else:
            print('Unknown')
    
conn = sqlite3.connect('database.db')

# supaya tidak ada lagi akses dari database sehingga tidak proses jalan terus menurus

conn.close()