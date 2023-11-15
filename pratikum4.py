def hitung_nilai_akhir(tugas, uts, uas):
    return round(0.3 * tugas + 0.35 * uts + 0.35 * uas, 1)

# Inisialisasi list untuk menyimpan data
data_mahasiswa = []

# Input data menggunakan perulangan
while True:
    print("\nMasukkan data mahasiswa:")
    nama = input("Nama        : ")
    nim = int(input("NIM         : "))
    nilai_tugas = int(input("Nilai Tugas : "))
    nilai_uts = int(input("Nilai UTS   : "))
    nilai_uas = int(input("Nilai UAS   : "))

    # Hitung nilai akhir
    nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)

    # Tambahkan data ke dalam list
    data_mahasiswa.append({
        'Nama': nama,
        'NIM': nim,
        'Nilai Tugas': nilai_tugas,
        'Nilai UTS': nilai_uts,
        'Nilai UAS': nilai_uas,
        'Nilai Akhir': nilai_akhir
    })

    tambah_data = input("\nTambah Data(y/t)? ").lower()
    if tambah_data != 'y':
        break

# Tampilkan output dengan format tabel
print("\n{:=^65}".format(""))
print("| No | {:<10} | {:^14} | {:^5} | {:^4} | {:^4} | {:^5} |".format("Nama", "NIM", "Tugas", "UTS", "UAS", "Akhir"))
print("{:=^65}".format(""))

for idx, mahasiswa in enumerate(data_mahasiswa, start=1):
    print("| {:<2} | {:<10} | {:^14} | {:^5} | {:^4} | {:^4} | {:.1f} |".format(idx, mahasiswa['Nama'], mahasiswa['NIM'],
                                                                                   mahasiswa['Nilai Tugas'], mahasiswa['Nilai UTS'],
                                                                                   mahasiswa['Nilai UAS'], mahasiswa['Nilai Akhir']))
print("{:=^65}".format(""))
