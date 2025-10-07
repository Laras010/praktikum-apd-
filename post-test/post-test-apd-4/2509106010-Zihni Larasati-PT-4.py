import os

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_header(judul):
    print("=" * 50)
    print(f"{judul:^50}")
    print("=" * 50)

def proses_login():
    maksimal_percobaan = 3
    percobaan = 0
    
    data_pengguna = {
        "anindya riza al-fath": "anindya21",
        "zihni larasati": "zihnianakmanise", 
        "nia ramadani": "niar987"
    }
    
    while percobaan < maksimal_percobaan:
        print("\n" + "-" * 30)
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if not username or not password:
            print("Username dan password wajib diisi!")
            percobaan += 1
            print(f"Sisa percobaan: {maksimal_percobaan - percobaan}")
            continue
        
        if username in data_pengguna and data_pengguna[username] == password:
            print(f"Selamat datang {username}!")
            return True, username
        else:
            percobaan += 1
            print("Username atau password tidak sesuai!")
            if percobaan < maksimal_percobaan:
                print(f"Sisa percobaan: {maksimal_percobaan - percobaan}")
    
    print("Anda telah gagal login 3 kali. Status: Non-Member.")
    return False, "Non-Member"

def tampilkan_produk():
    print("\nDaftar Produk:")
    print("-" * 40)
    print("1. Gula           - Rp 19.000")
    print("2. Susu kental    - Rp  9.000") 
    print("3. Tepung         - Rp  10.000")
    print("4. Telur          - Rp  2.500")
    print("5. Coklat         - Rp  25.000")
    print("6. Selesai Belanja")
    print("-" * 40)

def main():
    daftar_produk = {
        '1': {'nama': 'Gula', 'harga': 19000},
        '2': {'nama': 'Susu kental', 'harga': 9000},
        '3': {'nama': 'Tepung', 'harga': 10000},
        '4': {'nama': 'Telur', 'harga': 2500},
        '5': {'nama': 'Coklat batang', 'harga': 25000},
    }
    
    while True:
        bersihkan_layar()
        tampilkan_header("TOKO SEMBAKO LARAS")
        
        print("\nKeuntungan Member:")
        print("   - Diskon khusus 15% untuk semua produk")
        
        input_member = input("\nApakah Anda member? (y/n): ").strip().lower()
        status_member = False
        nama_pengguna = "Non-Member"
        persentase_diskon = 0.15
        
        if input_member == 'y':
            bersihkan_layar()
            tampilkan_header("MASUK SEBAGAI MEMBER")
            status_member, nama_pengguna = proses_login()
        else:
            print("\nStatus: Non-Member")
        
        input("\nTekan Enter untuk mulai belanja...")
        bersihkan_layar()
        
        keranjang = []
        total_harga = 0
        
        while True:
            bersihkan_layar()
            tampilkan_header("TOKO SEMBAKO LARAS")
            
            if status_member:
                print(f"Pelanggan: {nama_pengguna} (Member)")
            else:
                print(f"Pelanggan: {nama_pengguna}")
            
            tampilkan_produk()
            print(f"\nJumlah item di keranjang: {len(keranjang)}")
            print(f"Total sementara: Rp {total_harga:,}")
            
            pilihan = input("\nPilih nomor produk (1-5) atau 6 untuk selesai: ").strip()
            
            if pilihan == '6':
                if not keranjang:
                    print("Keranjang masih kosong, silakan pilih produk terlebih dahulu.")
                    input("\nTekan Enter untuk melanjutkan...")
                    continue
                break
            elif pilihan in daftar_produk:
                produk = daftar_produk[pilihan]
                
                keranjang.append({
                    'nama': produk['nama'],
                    'harga': produk['harga']
                })
                
                total_harga += produk['harga']
                print(f"\n{produk['nama']} telah dimasukkan ke keranjang!")
                print(f"Total saat ini: Rp {total_harga:,}")
            else:
                print("Nomor produk tidak valid. Silakan pilih 1-6.")
            
            input("\nTekan Enter untuk melanjutkan...")
        
        bersihkan_layar()
        tampilkan_header("STRUK BELANJA")
        print(f"Pelanggan: {nama_pengguna}")
        print("=" * 50)
        print(f"{'No.':<3} {'Produk':<20} {'Harga':<15}")
        print("-" * 50)
        
        for nomor, item in enumerate(keranjang, 1):
            print(f"{nomor:<3} {item['nama']:<20} Rp {item['harga']:,}")
        
        print("=" * 50)
        
        if status_member:
            diskon = total_harga * persentase_diskon
            total_akhir = total_harga - diskon
            print(f"Total sebelum diskon: Rp {total_harga:,}")
            print(f"Diskon member 15%:    Rp {diskon:,}")
            print(f"Total pembayaran:     Rp {total_akhir:,}")
            print("\nTerima kasih telah menjadi member setia kami!")
        else:
            print(f"Total pembayaran:     Rp {total_harga:,}")
            print("\nDaftar menjadi member untuk mendapatkan diskon 15%!")
        
        print("=" * 50)
        
        while True:
            print("\nApakah ingin melakukan transaksi lagi?")
            ulang = input("Ketik 'y' untuk Ya atau 'n' untuk Tidak: ").strip().lower()
            if ulang in ['y', 'n']:
                break
            print("Pilihan tidak valid. Silakan ketik 'y' atau 'n'.")
        
        if ulang == 'n':
            bersihkan_layar()
            tampilkan_header("TERIMA KASIH")
            print("\nTerima kasih sudah berbelanja di toko kami!")
            print("Semoga hari Anda menyenangkan!")
            break
        else:
            print("\nMenyiapkan transaksi baru...")
            input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()