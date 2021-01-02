import sqlite3
import main

class getDatabase:
    def __init__(self):
        self.database= sqlite3.connect('database.db')
        self.cursor = self.database.cursor()

    def deleteScreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    #merubah data
    def setData(self, Level, ID, Nama, Password):
        connect = sqlite3.connect('database.db')
        cursor = connect.cursor()
        cursor.execute("UPDATE Menu set Pengguna = ? WHERE Pengguna = ?", (level, idPengguna, namaPengguna, password))

        connect.commit()
        connect.close()

