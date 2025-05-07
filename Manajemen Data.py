#  Bismillahirrah`manirrahim
dt = []  # list nyimpen data siswa
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
        n = input("Masukkan nama siswa: ")
        u = input("Masukkan umur siswa: ")
        # tambahkan ke data
        dt.append({"nama": n, "umur": u})
        print("Siswa berhasil ditambahkan")
        
    elif pilihan == "2":
        # lihat semua siswa
        if len(dt) == 0:
            print("Belum ada data siswa")
        else:
            print("\nDaftar Siswa:")
            for i, s in enumerate(dt, start=1):
                print(str(i) + ". " + s['nama'] + " (" + s['umur'] + " tahun)")
        
    elif pilihan == "3":
        # edit data siswa
        if len(dt) == 0:
            print("Data kosong, gak ada yang di-edit")
        else:
            print("\nDaftar Siswa:")
            for i, s in enumerate(dt, start=1):
                print(str(i) + ". " + s['nama'] + " (" + s['umur'] + " tahun)")
            # pilih nomor yg mau diedit
            try:
                idx = int(input("Pilih nomor siswa yang akan diedit: "))
                if 1 <= idx <= len(dt):
                    nm_baru = input("Nama baru (tekan Enter jika tidak diubah): ")
                    umur_baru = input("Umur baru (tekan Enter jika tidak diubah): ")
                    if nm_baru != "":
                        dt[idx-1]["nama"] = nm_baru  # ganti nama
                    if umur_baru != "":
                        dt[idx-1]["umur"] = umur_baru  # ganti umur
                    print("Data berhasil diperbarui")
                else:
                    print("Pilihan tidak valid")
            except:
                print("Input tidak valid")
        
    elif pilihan == "4":
        # hapus siswa
        if len(dt) == 0:
            print("Data kosong, gak ada yang dihapus")
        else:
            print("\nDaftar Siswa:")
            for i, s in enumerate(dt, start=1):
                print(str(i) + ". " + s['nama'] + " (" + s['umur'] + " tahun)")
            try:
                idx = int(input("Pilih nomor siswa yang akan dihapus: "))
                if 1 <= idx <= len(dt):
                    dt.pop(idx-1)
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
        
