
class Pengguna:

    def __init__(self,level,idPengguna,namaPengguna,password):
        self.level = level
        self.idPengguna = idPengguna
        self.namaPengguna = namaPengguna
        self.__password = password

    def info(self):
        return '''Jabatan = {}\n
        ID = {}\n
        Nama = {}'''.format(self.level,self.idPengguna,self.namaPengguna)

class Boss(Pengguna):

    gaji = 7000000
    
    def __init__(self,level,idPengguna,namaPengguna,password):
        super().__init__('Boss',idPengguna,namaPengguna,password)

    def info(self):
        return '''Jabatan = {}\n
        ID = {}\n
        Nama = {}\n
        Gaji = {}'''.format(self.level,self.idPengguna,self.namaPengguna,Boss.gaji)

    def tambahPengguna():
        x = None
        level = input('Masukkan level : ')
        idPengguna = int(input('Masukkan ID Pengguna : '))
        namaPengguna = input('Masukkan Nama Pengguna : ')
        password = input('Masukkan Password : ')

        if level == 'Boss':
            Boss(level,idPengguna,namaPengguna,password)
            data.append(x)
            print('Data Boss {} berhasil ditambahkan'.format(namaPengguna))
        elif level == 'Staff':
            Staff(level,idPengguna,namaPengguna,password)
            data.append(x)
            print('Data Staff {} berhasil ditambahkan'.format(namaPengguna))
        elif level == 'Pelanggan':
            Pelanggan(level,idPengguna,namaPengguna,password)
            data.append(x)
            print('Data Pelanggan {} berhasil ditambahkan'.format(namaPengguna))
        else:
            print('Unknown')

class Staff(Pengguna):

    gaji = 0
    def __init__(self,level,idPengguna,namaPengguna,password):
        super().__init__('Staff',idPengguna,namaPengguna,password)

    def info(self):
        return '''Jabatan = {}\n
        ID = {}\n
        Nama = {}\n
        Gaji = {}'''.format(self.level,self.idPengguna,self.namaPengguna,Staff.gaji)

    def gajiHarian():

        masukShift = input('Masukkan Shift Anda (pagi/malam): ')
        masukDurasi = int(input('Masukkan Durasi Anda Bekerja : '))
        if masukShift == 'Pagi':
            Staff.gaji = masukDurasi * 100000
            print('Gaji anda adalah ',Staff.gaji)
        elif masukShift == 'Malam':
            Staff.gaji = masukDurasi * 120000
            print('Gaji anda adalah ',Staff.gaji)
        else:
            print('unknown')

    def tambahPengguna():
        x = None
        level = input('Masukkan level : ')
        idPengguna = int(input('Masukkan ID Pengguna : '))
        namaPengguna = input('Masukkan Nama Pengguna : ')
        password = input('Masukkan Password : ')

        if level == 'Boss':
            Boss(level,idPengguna,namaPengguna,password)
            data.append(x)
            print('Data Boss {} berhasil ditambahkan'.format(namaPengguna))
        elif level == 'Staff':
            Staff(level,idPengguna,namaPengguna,password)
            data.append(x)
            print('Data Staff {} berhasil ditambahkan'.format(namaPengguna))
        elif level == 'Pelanggan':
            Pelanggan(level,idPengguna,namaPengguna,password)
            data.append(x)
            print('Data Pelanggan {} berhasil ditambahkan'.format(namaPengguna))
        else:
            print('Unknown')

class Pelanggan(Pengguna):

    def __init__(self,level,idPengguna,namaPengguna,password):
        super().__init__('Pelanggan',idPengguna,namaPengguna,password)

    def info(self):
        return '''ID = {}\n
        Nama = {}'''.format(self.idPengguna,self.namaPengguna)

class Produk:

    stok = 0
    total = 0

    def __init__(self,idProduk,namaProduk,kategori,hargaBeli,harga):
        self.idProduk = idProduk
        self.namaProduk = namaProduk
        self.kategori = kategori
        self.hargaBeli = hargaBeli
        self.harga = harga

    def cari():
        cari = input('Cari berdasarkan (id/nama) : ')

        if cari == b1.idProduk or cari == b1.namaProduk:
            return '''\nID : {}\n
            Nama : {}\n
            Kategori : {}\n
            Harga : {}'''.format(b1.idProduk,b1.namaProduk,b1.kategori,b1.harga)
        elif cari == b2.idProduk or cari == b2.namaProduk:
            return '''\nID : {}\n
            Nama : {}\n
            Kategori : {}\n
            Harga : {}'''.format(b2.idProduk,b2.namaProduk,b2.kategori,b2.harga)
        elif cari == b3.idProduk or cari == b3.namaProduk:
            return '''\nID : {}\n
            Nama : {}\n
            Kategori : {}\n
            Harga : {}'''.format(b3.idProduk,b3.namaProduk,b3.kategori,b3.harga)
        elif cari == a1.idProduk or cari == a1.namaProduk:
            return '''\nID : {}\n
            Nama : {}\n
            Kategori : {}\n
            Harga : {}'''.format(a1.idProduk,a1.namaProduk,a1.kategori,a1.harga)
        elif cari == a2.idProduk or cari == a2.namaProduk:
            return '''\nID : {}\n
            Nama : {}\n
            Kategori : {}\n
            Harga : {}'''.format(a2.idProduk,a2.namaProduk,a2.kategori,a2.harga)
        else:
            print('Maaf kami tidak menemukan apa yang anda cari')


    def beli():
        barang = input('Mau beli apa? : ')
        banyak = int(input('Berapa banyak? : '))

        if barang == b1.namaProduk:
            Produk.total = banyak * b1.harga
            print('''\n\tAnda telah membeli {} sebanyak {}
            Jumlah yang harus dibayar adalah {}'''.format(b1.namaProduk,banyak,Produk.total))
        elif barang == b2.namaProduk:
            Produk.total = banyak * b2.harga
            print('''\n\tAnda telah membeli {} sebanyak {}
            Jumlah yang harus dibayar adalah {}'''.format(b2.namaProduk,banyak,Produk.total))
        elif barang == b3.namaProduk:
            Produk.total = banyak * b3.harga
            print('''\n\tAnda telah membeli {} sebanyak {}
            Jumlah yang harus dibayar adalah {}'''.format(b3.namaProduk,banyak,Produk.total))
        elif barang == a1.namaProduk:
            Produk.total = banyak * a1.harga
            print('''\n\tAnda telah membeli {} sebanyak {}
            Jumlah yang harus dibayar adalah {}'''.format(a1.namaProduk,banyak,Produk.total))
        elif barang == a2.namaProduk:
            Produk.total = banyak * a2.harga
            print('''\n\tAnda telah membeli {} sebanyak {}
            Jumlah yang harus dibayar adalah {}'''.format(a2.namaProduk,banyak,Produk.total)) 
        else:
            print('Maaf kami tidak menjual barang tersebut')

def menu():
    while True:
        print('''~~~~~Selamat Datang~~~~~''')

        user = input('Masuk sebagai (Boss/Staff/Pelanggan) : ')
        if user == 'Boss':
            key = input('Password : ')
            if key == 'luwakwhitecoffee':
                print('''Hello Boss !\nSilahkan Pilih Menu :\n
                1. Tampilkan info detail Boss\n
                2. Menambahkan pengguna\n
                3. Logout''')
                pilih = input('Masukkan angka : ')
                if pilih == '1':
                    print(boss.info())
                elif pilih == '2':
                    Boss.tambahPengguna()
                elif pilih == '3':
                    print('Terimakasih')
                    break
                else:
                    print('Angka yang anda masukkan salah')
            else:
                print('Anda siapa?')
        elif user == 'Staff':
            key = input('Password : ')
            if key == 'nyamandilambung':
                print('''Hello Staff !\nSilahkan Pilih Menu :\n
                1. Tampilkan info detail Staff\n
                2. Menambahkan pengguna\n
                3. Menghitung gaji harian\n
                4. Logout''')
                pilih = input('Masukkan angka : ')
                if pilih == '1':
                    id = int(input('Masukkan ID : '))
                    if id == 11:
                        print(staff1.info())
                    elif id == 12:
                        print(staff2.info())
                elif pilih == '2':
                    Staff.tambahPengguna()
                elif pilih == '3':
                    Staff.gajiHarian()
                elif pilih == '4':
                    print('Terimakasih')
                    break
                else:
                    print('Angka yang anda masukkan salah')
            else:
                print('Anda siapa?')
        elif user == 'Pelanggan':
            print('''Hello Stranger !\nSilahkan Pilih Menu :\n
            1. Tampilkan info detail Pelanggan\n
            2. Cari Produk\n
            3. Belanja Produk\n
            4. Logout''')
            pilih = input('Masukkan angka : ')
            if pilih == '1':
                print(pelanggan.info())
            elif pilih == '2':
                Produk.cari()
            elif pilih == '3':
                Produk.beli()
            elif pilih == '4':
                print('Terimakasih\nSilahkan datang kembali')
                break
            else:
                print('Angka yang anda masukkan salah')
        else:
            print('Anda Siapa?')
    

data = []

boss = Boss('Boss',0,'Kharisma','kharis88')
data.append(boss)
staff1 = Staff('Staff',11,'Jamal','jamal13')
data.append(staff1)
staff2 = Staff('Staff',12,'Panjul','panjul54')
data.append(staff2)
pelanggan = Pelanggan('Pelanggan',2,'Samsul','samsul20')
data.append(pelanggan)

b1 = Produk('0','Semen','Bahan',45000,50000)
b2 = Produk('1','Paku','Bahan',16000,20000)
b3 = Produk('2','Pipa','Bahan',25000,28000)
a1 = Produk('3','Sekop','Alat',24000,30000)
a2 = Produk('4','Gergaji','Alat',35000,40000)

menu()
