data_mahasiswa = []

def hitung_nilai_akhir(tugas, uts, uas):
    nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas
    return nilai_akhir

while True:

    nama = input("Masukkan Nama Mahasiswa: ")
    nim = float(input("Masukkan Nim:"))
    tugas = float(input("Masukkan Nilai Tugas: "))
    uts = float(input("Masukkan Nilai UTS: "))
    uas = float(input("Masukkan Nilai UAS: "))

    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

    data_mahasiswa.append({
        "Nama": nama,
        "Tugas": tugas,
        "UTS": uts,
        "UAS": uas,
        "Nilai Akhir": nilai_akhir
    })

    jawaban = input("Tambah data lagi? (y/t): ")
    if jawaban.lower() != 'y':
        break

print("\nDaftar Data Mahasiswa:")
for data in data_mahasiswa:
    print(f"Nama: {data['Nama']}, Tugas: {data['Tugas']}, UTS: {data['UTS']}, UAS: {data['UAS']}, Nilai Akhir: {data['Nilai Akhir']}")
    