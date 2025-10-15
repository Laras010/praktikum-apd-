import os

USERNAME = "AADPA"
PASSWORD = "Andi Ahmad dzaky P A"

tanaman_list = [{'nama': 'Bunga Mawar','warna': 'merah', 'tanggal': '2022-08-27', 'status': 'sehat'}] 
[{'nama': 'Bunga Tulip','warna': 'pink', 'tanggal': '2024-05-30', 'status': 'sehat'}] 
[{'nama': 'Bunga Kamboja ','warna': 'putih', 'tanggal': '2020-09-24', 'status': 'sehat'}]
[{'nama': 'Bunga Matahari','warna': 'kuning', 'tanggal': '2024-04-02', 'status': 'mati'}]
[{'nama': 'Bunga Alamanda','warna': 'ungu', 'tanggal': '20233-02-07', 'status': 'mati'}]


def clear_screen():
    """Fungsi untuk membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    """Fungsi untuk autentikasi pengguna."""
    input_username = input("Masukkan username: ")
    input_password = input("Masukkan password: ")
    if input_username == USERNAME and input_password == PASSWORD:
        return True 
    else:
        print("Login gagal. Username atau password salah.")  
        return False

def create_tanaman():
    """Fungsi untuk menambahkan tanaman baru."""
    nama = input("Masukkan nama tanaman: ")
    warna = input("Masukkan warna bunga: ")
    tanggal = input("Masukkan tanggal ditanam (contoh: YYYY-MM-DD): ")
    status = "Sehat"  # Status awal selalu "Sehat"
    tanaman_list.append({'nama': nama, 'warna': warna, 'tanggal': tanggal, 'status': status})
    print("Tanaman berhasil ditambahkan.")

def read_tanaman():
    """Fungsi untuk menampilkan daftar tanaman atau mencari berdasarkan nama."""
    if not tanaman_list:  
        print("Tidak ada tanaman dalam koleksi.")
        return
    pilihan = input("1. Tampilkan semua tanaman\n2. Cari berdasarkan nama\nPilih (1/2): ")
    if pilihan == '1':
        for tanaman in tanaman_list:
            print(f"nama: {tanaman['nama']}, warna: {tanaman['warna']}, tanggal: {tanaman['tanggal']}, status: {tanaman['status']}")
           
    elif pilihan == '2':
        nama_cari = input("Masukkan nama tanaman: ")
        for tanaman in tanaman_list:
            if tanaman['nama'].lower() == nama_cari.lower():  
                print(f"nama: {tanaman['nama']}, warna: {tanaman['warna']}, tanggal: {tanaman['tanggal']}, status: {tanaman['status']}")
           
        print("Tanaman tidak ditemukan.")  
    else:
        print("Pilihan tidak valid.") 

def update_tanaman():
    """Fungsi untuk mengubah status kesehatan tanaman."""
    nama = input("Masukkan nama tanaman yang ingin diupdate: ")
    for tanaman in tanaman_list:
        if tanaman['nama'].lower() == nama.lower(): 
            status_baru = input("Masukkan status kesehatan baru (Sehat/Sakit/Mati): ")
            if status_baru in ['Sehat', 'Sakit', 'Mati']:
                tanaman['status'] = status_baru
                print("Status kesehatan tanaman berhasil diupdate.")
            else:
                print("Status tidak valid. Gunakan Sehat, Sakit, atau Mati.") 
            return
    print("Tanaman tidak ditemukan.") 

def delete_tanaman():
    """Fungsi untuk menghapus tanaman jika statusnya 'Mati'."""
    nama = input("Masukkan nama tanaman yang ingin dihapus: ")
    for i, tanaman in enumerate(tanaman_list):
        if tanaman['nama'].lower() == nama.lower():  
            if tanaman['status'] == 'Mati': 
                del tanaman_list[i]
                print("Tanaman berhasil dihapus dari koleksi.")
            else:
                print("Tanaman belum mati, tidak bisa dihapus.")  
            return
    print("Tanaman tidak ditemukan.")  

def main():
    if not login():
        return  
    
    while True:
        clear_screen()  
        print("=== Pengelolaan Tanaman Bunga ===")
        print("1. Tambah Tanaman")
        print("2. Tampilkan atau Cari Tanaman")
        print("3. Ubah Status Kesehatan")
        print("4. Hapus Tanaman jika Mati")
        print("5. Keluar Program")
        pilihan = input("Pilih operasi 1-5: ")
        
        if pilihan == '1':
            create_tanaman()
        elif pilihan == '2':
            read_tanaman()
        elif pilihan == '3':
            update_tanaman()
        elif pilihan == '4':
            delete_tanaman()
        elif pilihan == '5':
            print("Keluar program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1-5.")  
        
        input("Tekan Enter untuk melanjutkan...")  

if __name__ == "__main__":
    main()