#Membuat list
data_list = ('Samsung', 'OPPO', 'Realme', 'Vivo')
print(data_list)
#Mengubah list menjadi set
merk_hp = set(['Samsung', 'OPPO', 'Realme', 'Vivo'])
print(merk_hp)
#Membuat Set dengan berbagai tipe data
data_set = {'Jeruk', 'Mobil', 18, True, ('A', 'B')}
print(data_set)

print("")
himpunan_huruf = {'a', 'b', 'c'}
print(himpunan_huruf)
#Fungsi Add
himpunan_huruf.add('d')
himpunan_huruf.add('e')
print(himpunan_huruf)
#Fungsi Update
himpunan_huruf.update({ 'h', 'i' })
print(himpunan_huruf)

print("")
himpunan = {'Venus', 'Alfa', 18, ('a', 'b'), False, True}
print(himpunan)
#Fungsi Remove
himpunan.remove(18)
print(himpunan)
#Fungsi Discard
himpunan.discard(('a', 'b'))
print(himpunan)
#Fungsi Pop
hapus = himpunan.pop()
print('Berhasil dihapus =', hapus)
print(himpunan)
#Fungsi Clear
himpunan.clear()
print(himpunan)

laki = {
  'Venus', 'Alfa', 'Patrick', 'Jerry'
}
perempuan = {
  'Asti', 'Cindhi', 'Putri', 'Anggun'
}
print("")
#Fungsi Union (Gabungan)
print(laki.union(perempuan))
#Fungsi Intersection (Irisan)
print(laki.intersection(perempuan))
#Fungsi Difference (Selisih)
print(laki - perempuan)
print(laki.difference(perempuan))

print('\nanggota grup perempuan yang bukan anggota grup laki:')
print(perempuan - laki)
print(perempuan.difference(laki))
#Symmetric Difference
print('\nanggota yang ada digrup:')
print(perempuan.symmetric_difference(laki))

#Membuat String lalu menambahkan variable
str='Aku cinta Indonesia'
str=str[:10]+'tanah airku'+str[9:]
print(str)
#Menghapus seluruh variable pada string
str=''
print(str)
#Mengetahui jumlah variable pada string
str=len(str)
print(str)
#Menghapus variable pada bagian tengah string
strl='Aku cinta tanah airku Indonesia'
strl=strl[:9]+''+strl[22:]
print(strl)
#Mengubah font pada string
kelas='praktikum Pemrograman berorientasi objek'
up=kelas.upper()
low=kelas.lower()
print(up)
print(low)
#Mengganti variable pada string
print(kelas.index('a'))
kelas2=kelas.replace('praktikum','praktik')
print(kelas2)
print(kelas.split())
#Menghapus spasi pada string
s='    python'
q=s.strip()
print(q)
#Menambahkan 2 variable string
s1='python '
s2='programing'
k=s1+s2
print(k)
#Memanggil string pada kalimat
a='satu'
b='dua'
c='tiga'
print('saya punya %s mangga'%(b))

#Membuat list
list=[0,1,2,3,4,5,6,7,8,9]
#Beberapa cara print data pada list
print(list)
print(list[3])
print(list[:3])
print(list[10-3:])
print(list[2:9])
print(list[-10])