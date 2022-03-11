#hak akses publik
class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi

segitiga_besar = Segitiga(100,80)

#akses variabel publik: alas, tinggi, dan luas dari luar kelas Segitiga
print("alas: ", segitiga_besar.alas)
print("tinggi: ", segitiga_besar.tinggi)
print("luas: ", segitiga_besar.luas)

#hak akses protected
class Utama:
  def __init__(self):
    self._a = 2

class Turunan:
  def __init__(self):
    #memanggil konstruktor pada kelas Utama
    Utama.__init__(self)
    print("Memanggil Variabel protected pada class Utama: ", self._a)

    #Modify the protected variable:
    self._a = 3
    print("Memanggil Variabel protected yang dimodifikasi diluar class: ",self._a)


objek1 = Turunan()
objek2 = Utama()

#memanggil variabel protected
print("Memanggil variabel protected dari objek1: ", objek1._a)
print("Memanggil variabel protected dari objek2: ", objek2._a)

#hak akses private
class Hitung:
  def __init__(self):
    self.__angkaRahasia=0

  def tampilkanHitung(self):
    self.__angkaRahasia += 1
    print(self.__angkaRahasia)

hitungan=Hitung()
hitungan.tampilkanHitung()
hitungan.tampilkanHitung()
hitungan._Hitung__angkaRahasia

#semua variabel bersifat publik
class Mobil():
  def __init__(self,jendela,pintu,mesin):
    self.jendela = jendela
    self.pintu = pintu
    self.mesin = mesin

audi= Mobil(4,5,"Diesel")
print(audi.jendela)
print(audi.pintu)
print(audi.mesin)

#semua variabel bersifat protected
class Mobil():
    def __init__(self,jendela,pintu,mesin):
        self._jendela=jendela
        self._pintu=pintu
        self.__mesin=mesin

audi=Mobil(4,4,"Diesel")
print(audi._Mobil__mesin)

class Truk(Mobil):
  def __init__(self,jendela,pintu,mesin,tipe):
    super().__init__(jendela,pintu,mesin)
    self.mesin=mesin
    self.tipebak=tipe

truk = Truk(4,4,"Diesel","bak terbuka")
print(truk.mesin)
print(truk.tipebak)

#semua variabel bersifat privat
class Mobil():
  def __init__(self,jendela,pintu,mesin):
    self.__jendela = jendela
    self.__pintu = pintu
    self.__mesin = mesin

audi=Mobil(4,4,"Diesel")
audi._Mobil__mesin
print(audi._Mobil__mesin)

#fungsi privat dan publik
class Pegawai:
    __nama= ""
    __alamat= ""
    __gaji=0

    def __init__(self,nama,alamat):
        self.__nama=nama
        self.__alamat=alamat
    def __hitunggaji(self):
        upahlembur=20000
        gajipokok=2000000
        jumlahlembur=int(input("total jam lembur: "))
        self.__gaji=(upahlembur*jumlahlembur)+gajipokok

    def tampilDetail(self):
        print("\n--Menghitung dan menampilkan detail gaji pegawai--")
        print("Nama: ",self.__nama)
        print("Alamat: ",self.__alamat)
        self.__hitunggaji
        print("Total gaji: ",self.__gaji)

pgw1 = Pegawai("Mikasa","wall Rose")
pgw1.tampilDetail()

pgw2 = Pegawai("Dora","Selokan")
pgw2.tampilDetail()

"""TUGAS"""

#menambahkan atribut privat pada kelas menu
#class menu
class menuminuman:  
    def __init__(self,nama,deskripsi,harga,diskon):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
        self.__diskon = diskon

mnm1 = menuminuman('Jus Jambu','Jus Jambu Merah Tanpa Gula',8500,"10%")
mnm2 = menuminuman('Jus Alpukat','Jus Alpukat dengan gula merah',15000,"20%")
mnm3 = menuminuman("Jus Alpukat Xtra Milk",'Jus Alpukat dengan susu coklat',15000,"10%")
mnm4 = menuminuman('Red and Smooth','Smoothie dengan pisang dan susu',17500,"15%")

pilihan = [mnm1,mnm2,mnm3,mnm4]
print('Daftar menu minuman Healthy')
for mn in pilihan:
    t = '{} harga Rp {},{},{}'.format(mn.nama,mn.harga,mn.deskripsi,mn._menuminuman__diskon)
    print(t)

#menambahkan atribut privat pada kelas mahasiswa
#class mahasiswa
class Mahasiswa: 
    def __init__(self,nama,nim,prodi,thn_masuk,SPP,IPK):
        self.nama =  nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk
        self.__SPP = SPP
        self.__IPK = IPK

m1 = Mahasiswa('Udin','10120371','Sistem Informasi',2020,3.80,4180000)
teks = '{} adalah mahasiswa {} angkatan {} dengan nim {} dan IPK {} serta memiliki tagihan SPP {}'.format(m1.nama,m1.prodi,m1.thn_masuk,m1.nim,m1._Mahasiswa__SPP,m1._Mahasiswa__IPK)
print(teks)

#menambahkan atribut privat pada kelas buku
#class buku
class Buku:
    def __init__(self,judul,pengarang,tahun_terbit,harga,terjual):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit =  tahun_terbit
        self.__harga= harga
        self.__terjual= terjual

buku = Buku('Tenggelamnya Kapal Van Der Wijck','HAMKA', 1938, 120000,900)
t = 'Buku {} karangan {} pertama kali terbit {} dengan harga {} dan laku terjual hingga {} buku'.format(buku.judul,buku.pengarang,buku.tahun_terbit,buku._Buku__harga,buku._Buku__terjual)
print(t)