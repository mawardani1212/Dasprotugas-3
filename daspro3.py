# NOMOR 1
data_mahasiswa = {
    "Devimarni": "07352111025",
    "PutJum"   : "07352111007",
    "Suci"     : "07352111048",
    "Laila"    : "07352111027",
    "Mimiyanti": "07352111029",
    "Nabila"   : "07352111037",
    "Andini"   : "07352111005",
    "Lini"     : "07352111016",
    "Tin"      : "07352111022",
    "Mawar"    : "07352111035",
}
def login():
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    if username in data_mahasiswa and data_mahasiswa[username].lower() == password.lower():
        print("Selamat datang, {}!".format(username))
    else:
        print("Data yang Anda masukkan salah!")

while True:
    login()
    lanjut = input("Coba lagi? (y/t): ")
    if lanjut.lower() == "t":
        break
print("Terima kasih!")




#NOMOR 2
# Data list pertama sebagai kunci
keys = ['1 Minggu', '1 Bulan', '1 Tahun']

# Data list kedua sebagai nilai
values = [ '7 Hari' , '4 Minggu', '12 Bulan']

# Menggabungkan kedua list menjadi dictionary
data_dict = dict(zip(keys, values))

# Mencetak data dictionary
print("Data Dictionary:")
print(data_dict)





#NOMOR 3
# Data dictionary jadwal daspro IF2
jadwalDasproIF2 = {
    'Senin': 'Jam 10.50 - 14.10',
    'Selasa': 'Jam 08.00 - 11.30',
}

# Data dictionary jadwal daspro IF3
jadwalDasproIF3 = {
    'Rabu': 'Jam 14.20 - 17.00',
    'Kamis': 'Jam 10.50 - 14.10',
}

# Menggabungkan kedua dictionary
jadwal_gabung = {}
jadwal_gabung.update(jadwalDasproIF2)
jadwal_gabung.update(jadwalDasproIF3)

# Mencetak data dictionary gabungan
print("Jadwal Mata Kuliah Gabungan:")
print(jadwal_gabung)






