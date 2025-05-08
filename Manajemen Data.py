# Bismillahirrahmanirrahim
data_siswa = []  # list nyimpen data siswa

while True:
    print("\n>>> Program Data Siswa <<<")
    print("1. Tambah Siswa🧑‍💻")
    print("2. Lihat Siswa🧑‍🎓")
    print("3. Edit Siswa🧑‍🔬")
    print("4. Hapus Siswa🙅")
    print("5. Keluar🏃")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        # tambah siswa
        nama = input("Masukkan nama siswa: ")
        umur = input("Masukkan umur siswa: ")
        rata_rata = input("Masukkan nilai rata-rata siswa: ")
        # tambahkan ke data
        data_siswa.append({"nama": nama, "umur": umur, "rata_rata": rata_rata})
        print("Siswa berhasil ditambahkan")

    elif pilihan == "2":
        # lihat semua siswa
        if len(data_siswa) == 0:
            print("Belum ada data siswa")
        else:
            print("\nDaftar Siswa:")
            for nomor, siswa in enumerate(data_siswa, start=1):
                print(f"{nomor}. {siswa['nama']} ({siswa['umur']} tahun) - Rata-rata: {siswa['rata_rata']}")

    elif pilihan == "3":
        # edit data siswa
        if len(data_siswa) == 0:
            print("Data kosong, gak ada yang di-edit")
        else:
            print("\nDaftar Siswa:")
            for nomor, siswa in enumerate(data_siswa, start=1):
                print(f"{nomor}. {siswa['nama']} ({siswa['umur']} tahun) - Rata-rata: {siswa['rata_rata']}")
            try:
                indeks = int(input("Pilih nomor siswa yang akan diedit: "))
                if 1 <= indeks <= len(data_siswa):
                    nama_baru = input("Nama baru (tekan Enter jika tidak diubah): ")
                    umur_baru = input("Umur baru (tekan Enter jika tidak diubah): ")
                    rata_rata_baru = input("Rata-rata baru (tekan Enter jika tidak diubah): ")
                    if nama_baru != "":
                        data_siswa[indeks-1]["nama"] = nama_baru
                    if umur_baru != "":
                        data_siswa[indeks-1]["umur"] = umur_baru
                    if rata_rata_baru != "":
                        data_siswa[indeks-1]["rata_rata"] = rata_rata_baru
                    print("Data berhasil diperbarui")
                else:
                    print("Pilihan tidak valid")
            except:
                print("Input tidak valid")

    elif pilihan == "4":
        # hapus siswa
        if len(data_siswa) == 0:
            print("Data kosong, gak ada yang dihapus")
        else:
            print("\nDaftar Siswa:")
            for nomor, siswa in enumerate(data_siswa, start=1):
                print(f"{nomor}. {siswa['nama']} ({siswa['umur']} tahun) - Rata-rata: {siswa['rata_rata']}")
            try:
                indeks = int(input("Pilih nomor siswa yang akan dihapus: "))
                if 1 <= indeks <= len(data_siswa):
                    data_siswa.pop(indeks-1)
                    print("Data berhasil dihapus")
                else:
                    print("Pilihan tidak valid")
            except:
                print("Input tidak valid")

    elif pilihan == "5":
        print("Terimakasih, Sampai jumpa kembali!!")
        break
    else:
        print("Pilihan tidak tersedia, coba lagi. Mungkin hatimu udah terhubung ke orang lain, bukan aku lagi")

# Alhamdullillah selesaiii😎
