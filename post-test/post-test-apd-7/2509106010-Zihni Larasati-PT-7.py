import os

#VARIABEL GLOBAL
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

login_sukses = False  

#PROSEDUR TANPA RETURN
def tampilkan_data():
    """Menampilkan semua data tanaman"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== DAFTAR TANAMAN ===")
    if not tanaman_dict:
        print("Belum ada data tanaman.")
    else:
        for nama, data in tanaman_dict.items():
            print(f"{nama} | Warna: {data['warna']} | Tanggal: {data['tanggal']} | Status: {data['status']}")
    input("\nTekan Enter untuk melanjutkan...")

def tampilkan_menu_admin():
    """Menampilkan menu untuk admin"""
    print("=== MENU ADMIN ===")
    print("1. Tambah Tanaman")
    print("2. Tampilkan/Cari Tanaman")
    print("3. Ubah Status Tanaman")
    print("4. Hapus Tanaman (Mati)")
    print("5. Logout")


#FUNGSI DENGAN PARAMETER
def ubah_status_tanaman(nama_tanaman): 
    """Mengubah status tanaman tertentu"""
    global tanaman_dict
    if nama_tanaman in tanaman_dict:
        status_baru = input("Masukkan status baru (sehat/sakit/mati): ").lower().strip()
        if status_baru in ['sehat', 'sakit', 'mati']:
            tanaman_dict[nama_tanaman]['status'] = status_baru
            return f"Status {nama_tanaman} berhasil diubah menjadi {status_baru}."
        else:
            return "Status tidak valid."
    else:
        return "Tanaman tidak ditemukan."


#FUNGSI TANPA PARAMETER
def tambah_tanaman():  
    """Menambahkan tanaman baru"""
    global tanaman_dict
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== TAMBAH TANAMAN BARU ===")

    nama = input("Masukkan nama tanaman: ").strip()
    warna = input("Masukkan warna bunga: ").strip()
    tanggal = input("Masukkan tanggal ditanam (YYYY-MM-DD): ").strip()

    if nama in tanaman_dict:
        print("Tanaman sudah ada.")
    else:
        tanaman_dict[nama] = {"warna": warna, "tanggal": tanggal, "status": "sehat"}
        print("Tanaman berhasil ditambahkan.")
    input("Tekan Enter untuk melanjutkan...")


#FUNGSI REKURSIF
def hitung_tanaman_mati(daftar_tanaman, indeks=0, jumlah=0):
    """Fungsi rekursif untuk menghitung jumlah tanaman mati"""
    if indeks == len(daftar_tanaman):
        return jumlah
    nama = daftar_tanaman[indeks]
    if tanaman_dict[nama]["status"] == "mati":
        jumlah += 1
    return hitung_tanaman_mati(daftar_tanaman, indeks + 1, jumlah)


#PROGRAM UTAMA
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== SISTEM PENGELOLAAN TANAMAN BUNGA ===")
    print("1. Login")
    print("2. Register")
    print("3. Lihat Total Tanaman Mati (Rekursif)")
    print("4. Keluar")
    menu_awal = input("Pilih (1-4): ").strip()

    if menu_awal == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN ===")
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ").strip()

        #ERROR HANDLING LOGIN
        try:
            if username in akun and akun[username]["password"] == password:
                role = akun[username]["role"]
                login_sukses = True
                print(f"Login berhasil sebagai {role}")
                input("Tekan Enter untuk melanjutkan...")

                #ADMIN
                if role == "admin":
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        tampilkan_menu_admin()
                        pilihan = input("Pilih (1-5): ").strip()

                        try:
                            if pilihan == '1':
                                tambah_tanaman()
                            elif pilihan == '2':
                                tampilkan_data()
                            elif pilihan == '3':
                                nama = input("Masukkan nama tanaman: ").strip()
                                print(ubah_status_tanaman(nama))
                                input("Tekan Enter untuk melanjutkan...")
                            elif pilihan == '4':
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
                                raise ValueError("Pilihan menu tidak valid.")
                        except ValueError as e:
                            print(f"Terjadi kesalahan: {e}")
                            input("Tekan Enter untuk lanjut...")

                #USER
                elif role == "user":
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=== MENU USER ===")
                        print("1. Lihat Tanaman")
                        print("2. Ubah Status Tanaman")
                        print("3. Logout")
                        pilihan = input("Pilih (1-3): ").strip()

                        try:
                            if pilihan == '1':
                                tampilkan_data()
                            elif pilihan == '2':
                                nama = input("Masukkan nama tanaman: ").strip()
                                print(ubah_status_tanaman(nama))
                                input("Tekan Enter untuk melanjutkan...")
                            elif pilihan == '3':
                                print("Logout berhasil.")
                                input("Tekan Enter untuk kembali ke menu utama...")
                                break
                            else:
                                raise ValueError("Pilihan menu tidak valid.")
                        except ValueError as e:
                            print(f"Terjadi kesalahan: {e}")
                            input("Tekan Enter untuk lanjut...")

            else:
                print("Login gagal. Username atau password salah.")
                input("Tekan Enter untuk melanjutkan...")

        except Exception as e:
            print(f"Terjadi kesalahan sistem: {e}")
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
        daftar = list(tanaman_dict.keys())
        total_mati = hitung_tanaman_mati(daftar)
        print(f"Jumlah tanaman yang mati: {total_mati}")
        input("Tekan Enter untuk melanjutkan...")

    elif menu_awal == '4':
        print("Terima kasih telah menggunakan program ini!")
        break

    else:
        print("Pilihan tidak valid.")
        input("Tekan Enter untuk melanjutkan...")
