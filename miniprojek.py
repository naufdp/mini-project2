nama = input("Masukkan nama: ")

while True:
        kelas = input("Masukkan kelas: ")
        if kelas == "XII KI 1" or kelas == "XII KI 2":
            print("Kelas valid")
            break

        print("PERINGATAN!")
        print("Kelas harus antara lain XII KI 1 / XII KI 2")

while True:
    try:
        no_absen = int(input("Masukkan nomor absen: "))
        if (no_absen >= 1 and no_absen <= 36):
                    print("Nomor absen berhasil diterima")
                    break
        print("Nomor absen hanya bisa untuk angka 1-36")
    except:
        print("PERINGATAN!")
        print("Nomor absen harus berupa angka")

while True:
    try:
        umur = int(input("Masukkan umur: "))
        if (umur >= 15 and umur <= 17):
            print("Umur berhasil diterima")
            break
        print("Umur hanya bisa untuk angka 15-17")
    except:
        print("PERINGATAN!")
        print("Umur harus berupa angka")

while True:
    try:
        nilai_tugas = float(input("Masukkan nilai tugas: "))
        if (nilai_tugas >= 0 and nilai_tugas <= 100):
            print("Nilai tugas berhasil diterima")
            break
        print("Nilai tugas hanya bisa untuk angka 0-100")
    except:
        print("PERINGATAN!")
        print("Nilai tugas harus berupa angka")

while True:
    try:
        nilai_uts = float(input("Masukkan nilai UTS: "))
        if (nilai_uts >= 0 and nilai_uts <= 100):
            print("Nilai UTS berhasil diterima")
            break
        print("Niai UTS hanya bisa untuk angka 0-100")
    except:
        print("PERINGATAN!")
        print("Nilai UTS harus berupa angka")
        
while True:
    try:
        nilai_uas = float(input("Masukkan nilai UAS: "))
        if (nilai_uas >= 0 and nilai_uas <= 100):
            print("Nilai UAS berhasil diterima")
            break
        print("Nilai UAS hanya bisa untuk angka 0-100")
    except:
        print("PERINGATAN!")
        print("Nilai UAS harus berupa angka")


bobot_tugas = 0.30
bobot_uts = 0.30
bobot_uas = 0.40


print("================================")
print("         DATA SISWA")
print("================================")
print("")


print("Nama        :", nama)
print("Kelas       :", kelas)
print("No. Absen   :", no_absen)
print("Umur        :", umur)
print("Nilai tugas :", nilai_tugas)
print("Nilai UTS   :", nilai_uts)
print("Nilai UAS   :", nilai_uas)


perhitungan = (nilai_tugas * bobot_tugas 
    + nilai_uts * bobot_uts 
    + nilai_uas * bobot_uas
)

print("Nilai akhir :", perhitungan)


if perhitungan >= 75:
    print("Status      : LULUS")
else:
    print("Status      : TIDAK LULUS")


if perhitungan >= 90:
    print("Grade       : A")
    print("Keterangan  : Sangat Baik")
elif perhitungan >= 80:
    print("Grade       : B")
    print("Keterangan  : Baik")
elif perhitungan >= 70:
    print("Grade       : C")
    print("Keterangan  : Cukup")
elif perhitungan >= 60:
    print("Grade       : D")
    print("Keterangan  : Kurang")
else:
    print("Grade       : E")
    print("Keterangan  : Sangat Kurang")


print("================================")