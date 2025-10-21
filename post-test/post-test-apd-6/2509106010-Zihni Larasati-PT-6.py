import os

akun = {
    "admin": {"password": "andi laras nee", "role": "admin"},
    "AADPA": {"password": "Andi Ahmad dzaky P A", "role": "user"},
    "Laras": {"password": "Z Larasati", "role": "user"}
}

tanaman_dict = {
    "Bunga Mawar": {"warna": "merah", "tanggal": "2022-08-27", "status": "sehat"},
    "Bunga Tulip": {"warna": "pink", "tanggal": "2024-05-30", "status": "sehat"},
    "Bunga Kamboja": {"warna": "putih", "tanggal": "2020-09-24", "status": "sehat"},
    "Bunga Matahari": {"warna": "kuning", "tanggal": "2024-04-02", "status": "mati"},
    "Bunga Alamanda": {"warna": "ungu", "tanggal": "2023-02-07", "status": "mati"}
}

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== SISTEM PENGELOLAAN TANAMAN BUNGA ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu_awal = input("Pilih (1-3): ").strip()

 
    if menu_awal == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN ===")
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ").strip()

        if username in akun and akun[username]["password"] == password:
            role = akun[username]["role"]
            print(f"Login berhasil sebagai {role}")
            input("Tekan Enter untuk melanjutkan...")

            
            if role == "admin":
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== MENU ADMIN ===")
                    print("1. Tambah Tanaman")
                    print("2. Tampilkan/Cari Tanaman")
                    print("3. Ubah Status Tanaman")
                    print("4. Hapus Tanaman (Mati)")
                    print("5. Logout")
                    pilihan = input("Pilih (1-5): ").strip()

                   
                    if pilihan == '1':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== TAMBAH TANAMAN BARU ===")
                        nama = input("Masukkan nama tanaman: ").strip()
                        if nama in tanaman_dict:
                            print("Tanaman sudah ada.")
                        else:
                            warna = input("Masukkan warna bunga: ").strip()
                            tanggal = input("Masukkan tanggal ditanam (YYYY-MM-DD): ").strip()
                            tanaman_dict[nama] = {"warna": warna, "tanggal": tanggal, "status": "sehat"}
                            print("Tanaman berhasil ditambahkan.")
                        input("Tekan Enter untuk melanjutkan...")

                    
                    elif pilihan == '2':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== LIHAT DATA TANAMAN ===")
                        if not tanaman_dict:
                            print("Belum ada data tanaman.")
                        else:
                            print("1. Tampilkan semua\n2. Cari tanaman")
                            pilih_cari = input("Pilih (1/2): ").strip()
                            if pilih_cari == '1':
                                for nama, data in tanaman_dict.items():
                                    print(f"{nama} | Warna: {data['warna']} | Tanggal: {data['tanggal']} | Status: {data['status']}")
                            elif pilih_cari == '2':
                                nama_cari = input("Masukkan nama tanaman: ").strip()
                                if nama_cari in tanaman_dict:
                                    data = tanaman_dict[nama_cari]
                                    print(f"{nama_cari} | Warna: {data['warna']} | Tanggal: {data['tanggal']} | Status: {data['status']}")
                                else:
                                    print("Tanaman tidak ditemukan.")
                            else:
                                print("Pilihan tidak valid.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == '3':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== UBAH STATUS TANAMAN ===")
                        nama = input("Masukkan nama tanaman: ").strip()
                        if nama in tanaman_dict:
                            status_baru = input("Masukkan status baru (sehat/sakit/mati): ").lower().strip()
                            if status_baru in ['sehat', 'sakit', 'mati']:
                                tanaman_dict[nama]['status'] = status_baru
                                print("Status berhasil diperbarui.")
                            else:
                                print("Status tidak valid.")
                        else:
                            print("Tanaman tidak ditemukan.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == '4':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== HAPUS TANAMAN ===")
                        nama = input("Masukkan nama tanaman: ").strip()
                        if nama in tanaman_dict:
                            if tanaman_dict[nama]['status'] == 'mati':
                                del tanaman_dict[nama]
                                print("Tanaman berhasil dihapus.")
                            else:
                                print("Tanaman belum mati, tidak bisa dihapus.")
                        else:
                            print("Tanaman tidak ditemukan.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == '5':
                        print("Logout berhasil.")
                        input("Tekan Enter untuk kembali ke menu utama...")
                        break
                    else:
                        print("Pilihan tidak valid.")
                        input("Tekan Enter untuk melanjutkan...")

            elif role == "user":
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== MENU USER ===")
                    print("1. Lihat Tanaman")
                    print("2. Ubah Status Tanaman")
                    print("3. Logout")
                    pilihan = input("Pilih (1-3): ").strip()

                    if pilihan == '1':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== LIHAT TANAMAN ===")
                        for nama, data in tanaman_dict.items():
                            print(f"{nama} | Warna: {data['warna']} | Tanggal: {data['tanggal']} | Status: {data['status']}")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == '2':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== UBAH STATUS TANAMAN ===")
                        nama = input("Masukkan nama tanaman: ").strip()
                        if nama in tanaman_dict:
                            status_baru = input("Masukkan status baru (sehat/sakit/mati): ").lower().strip()
                            if status_baru in ['sehat', 'sakit', 'mati']:
                                tanaman_dict[nama]['status'] = status_baru
                                print("Status berhasil diperbarui.")
                            else:
                                print("Status tidak valid.")
                        else:
                            print("Tanaman tidak ditemukan.")
                        input("Tekan Enter untuk melanjutkan...")

                    elif pilihan == '3':
                        print("Logout berhasil.")
                        input("Tekan Enter untuk kembali ke menu utama...")
                        break

                    else:
                        print("Pilihan tidak valid.")
                        input("Tekan Enter untuk melanjutkan...")

        else:
            print("Login gagal. Username atau password salah.")
            input("Tekan Enter untuk melanjutkan...")

    elif menu_awal == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER PENGGUNA BARU ===")
        username = input("Masukkan username baru: ").strip()
        if username in akun:
            print("Username sudah terdaftar!")
        else:
            password = input("Masukkan password: ").strip()
            akun[username] = {"password": password, "role": "user"}
            print("Registrasi berhasil! Silakan login.")
        input("Tekan Enter untuk melanjutkan...")

    elif menu_awal == '3':
        print("Terima kasih telah menggunakan program ini!")
        break

    else:
        print("Pilihan tidak valid.")
        input("Tekan Enter untuk melanjutkan...")
