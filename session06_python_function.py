#### REGULAR FUNCTION ####
#### Penulisan diawali dengan menuliskan def

def perkenalkanDiri():
    print("Halo, namaku Reza")

perkenalkanDiri()

def penjumlahanBilangan(angkaPertama, angkaKedua):
    return angkaPertama + angkaKedua

hasilPenjumlahan = penjumlahanBilangan(3,2)
print(hasilPenjumlahan)

def melihatNilai(nama, ipk):
    print(f"Nama Mahasiswa: {nama}")

    if ipk >= 3.5:
        print("Cumlaude.")
    elif ipk > 3:
        print("Sangat Istimewa")
    else:
        print("Istimewa")


melihatNilai("Reza", 3.8)
melihatNilai("Ghofar", 3)
melihatNilai("Dian", 4)

nama = "Reza"
ipk = 3.8

print(f"Nama Mahasiswa: {nama}")

if ipk >= 3.5:
    print("Cumlaude.")
elif ipk > 3:
     print("Sangat Istimewa")
else:
    print("Istimewa")

nama = "Ghofar"
ipk = 3

print(f"Nama Mahasiswa: {nama}")

if ipk >= 3.5:
    print("Cumlaude.")
elif ipk > 3:
     print("Sangat Istimewa")
else:
    print("Istimewa")

## Function Yang Membutuhkan Input namun Tidak mengeluarkan Output ##
def demoFunction(nilai):
    if nilai >= 80:
        print("Nilai Anda adalah A")
    elif nilai >= 70:
        print("Nilai Anda adalah AB") 
    else:
        print("Nilai Anda adalah C")

demoFunction("90")
demoFunction() # akan muncul error karena membutuhkan parameter yang harus diisi

## Function Yang Tidak Membutuhkan Input dan Tidak mengeluarkan Output ##
def perkalian():
    angka1 = 5
    angka2 = 7
    hasilPerkalian = angka1 * angka2
    print(hasilPerkalian)

perkalian()

## Function Yang  Membutuhkan Input dan Mengeluarkan Output ##
def hasilPerhitunganVolume(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume # menggunakan return untuk menghasilkan nilai

print(hasilPerhitunganVolume(5, 3, 2))


#### KONSEP FUNCTION ####
### function itu memiliki konsep yang namanya parameter.
### nama dan ipk merupakan parameter function melihatNilai()
def melihatNilai(nama, ipk):
    print(f"Nama Mahasiswa: {nama}")

    if ipk >= 3.5:
        print("Cumlaude.")
    elif ipk > 3:
        print("Sangat Istimewa")
    else:
        print("Istimewa")

melihatNilai() # akan error
melihatNilai('Reza', 4)

## function yang memiliki parameter default
def melihatNilaiWithDefaultParameter(nama = 'Miranda', ipk = 3.5):
    print(f"Nama Mahasiswa: {nama}")

    if ipk >= 3.5:
        print("Cumlaude.")
    elif ipk > 3:
        print("Sangat Istimewa")
    else:
        print("Istimewa")

melihatNilaiWithDefaultParameter()

## CALLING FUNCTION ##
# CALLBACK FUNCTION
def melihatDataMahasiswa(jurusan, namaMahasiswa = 'Miranda', ipk = 3.5):
    print(f"===== MAHASISWA JURUSAN {jurusan} =====")

    melihatNilaiWithDefaultParameter(namaMahasiswa, ipk)

melihatDataMahasiswa("Sistem Informasi", 'Firin', 3.2)
melihatDataMahasiswa("Akuntansi")

# CALL OTHER FUNCTION
def tambahBilangan(angka1, angka2):
    return angka1 + angka2

def pembagianBilangan(angka1, angka2):
    return angka1 / angka2

def operasi_matematika(functionOperasiMatematika, angka1, angka2): # function sebagai parameter
    hasilJumlah = functionOperasiMatematika(angka1, angka2)
    print(f"Hasil operasi matematika: {hasilJumlah}")

operasi_matematika(tambahBilangan, 10, 5)
operasi_matematika(pembagianBilangan, 10, 5)

## KONSEP VARIABLE ###
# contoh global variable
# karakteristik: didefinisikan secara global (untuk seluruh kode program di dalam file)
namaLengkap = "Hisyam Hawari"
print(namaLengkap)

def perkenalanNama(nama):
    print(f"Halo namaku {nama}")

perkenalanNama(namaLengkap)

# contoh local variable
# karakteristik: didefinisikan secara local di dalam function
def identitasDiri(nama):
    print(f"Halo namaku {nama}")

    namaPanggilan = "Hisyam"
    print(f"Nama panggilanku adalah {namaPanggilan}")

identitasDiri("Hisyam Hawari")
print(namaPanggilan)

