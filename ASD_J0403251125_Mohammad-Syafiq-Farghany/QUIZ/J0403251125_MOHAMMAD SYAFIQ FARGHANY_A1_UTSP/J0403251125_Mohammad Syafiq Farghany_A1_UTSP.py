#====================================================
# Nama    : Mohammad Syafiq Farghany
# NIM     : J0403251125
# Kelas  : Teknologi Rekayasa Perangkat Lunak A1/P1
# Mata Kuliah : Algoritma dan Struktur Data
# Tanggal : 25 Maret 2024
# Deskripsi : UTS Praktikum Algoritma & Struktur Data
#====================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1) [cite: 31]
def muat_data_buku(buku_file):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    
    Args:
        buku_file (str): Nama file yang akan dibaca
    
    Returns:
        dict: Dictionary dengan kode_buku sebagai key dan data buku sebagai value
    """
    database_buku = {}
    
    try:
        # Membuka file dalam mode read
        with open(buku_file, 'r', encoding='utf-8') as file:
            # Membaca setiap baris dalam file
            for line in file:
                # Menghilangkan whitespace dan newline
                line = line.strip()
                
                # Memisahkan data berdasarkan koma
                if line:  # pastikan baris tidak kosong
                    data = line.split(',')
                    
                    # Validasi format data (harus ada 3 elemen)
                    if len(data) == 3:
                        kode_buku = data[0]
                        judul = data[1]
                        harga = int(data[2])
                        
                        # Menyimpan ke dictionary dengan kode_buku sebagai key
                        database_buku[kode_buku] = {
                            'judul': judul,
                            'harga': harga
                        }
        
        print(f"✓ Berhasil memuat {len(database_buku)} data buku dari {buku_file}")
        
    except FileNotFoundError:
        # Menangani error jika file tidak ditemukan
        print(f"✗ Error: File '{buku_file}' tidak ditemukan!")
        print("  Pastikan file buku.txt ada di folder yang sama dengan program ini.")
        
    except Exception as e:
        # Menangani error lainnya
        print(f"✗ Error saat membaca file: {e}")
    
    return database_buku


# 2. LINKED LIST - MANAJEMEN PROMOSI 
class Node:
    """
    Class Node untuk merepresentasikan sebuah simpul dalam Linked List.
    Setiap node berisi data (judul buku) dan pointer ke node berikutnya.
    """
    def __init__(self, judul):
        """
        Inisialisasi Node baru
        
        Args:
            judul (str): Judul buku yang disimpan dalam node
        """
        self.data = judul      # Menyimpan data judul buku
        self.next = None       # Pointer ke node berikutnya (default: None)


class LinkedListPromosi:
    """
    Class LinkedListPromosi untuk mengelola daftar buku promosi menggunakan
    struktur data Single Linked List.
    """
    def __init__(self):
        """
        Inisialisasi Linked List kosong dengan head = None
        """
        self.head = None

    def tambah_buku_promosi(self, judul):
        """
        Menambahkan buku ke daftar promosi (Linked List)
        Buku baru ditambahkan di akhir list (append)
        
        Args:
            judul (str): Judul buku yang akan ditambahkan ke promosi
        """
        # Membuat node baru dengan data judul
        node_baru = Node(judul)
        
        # Jika linked list masih kosong (head = None)
        if self.head is None:
            # Node baru menjadi head (node pertama)
            self.head = node_baru
            print(f"✓ Buku '{judul}' ditambahkan sebagai promosi pertama")
        else:
            # Jika sudah ada node, cari node terakhir
            current = self.head
            
            # Traverse hingga menemukan node terakhir (next = None)
            while current.next is not None:
                current = current.next
            
            # Tambahkan node baru di akhir
            current.next = node_baru
            print(f"✓ Buku '{judul}' ditambahkan ke daftar promosi")

    def tampilkan_promosi(self):
        """
        Menampilkan semua buku dalam daftar promosi
        Melakukan traversal dari head hingga akhir linked list
        """
        # Cek apakah linked list kosong
        if self.head is None:
            print("\n═══════════════════════════════════════")
            print("  Belum ada buku dalam daftar promosi")
            print("═══════════════════════════════════════")
            return
        
        # Tampilkan header
        print("\n═══════════════════════════════════════")
        print("       DAFTAR BUKU PROMOSI")
        print("═══════════════════════════════════════")
        
        # Mulai traversal dari head
        current = self.head
        nomor = 1
        
        # Traverse seluruh linked list
        while current is not None:
            print(f"  {nomor}. {current.data}")
            current = current.next  # Pindah ke node berikutnya
            nomor += 1
        
        print("═══════════════════════════════════════\n")


# 3. QUEUE - ANTIREAN KASIR 
class AntreanKasir:
    """
    Class AntreanKasir untuk mengelola antrean pelanggan menggunakan
    konsep Queue (FIFO - First In First Out)
    """
    def __init__(self):
        """
        Inisialisasi Queue kosong menggunakan list Python
        """
        self.antrean = []

    def tambah_antrean(self, nama_pelanggan):
        """
        Menambah antrean (Enqueue)
        Pelanggan baru ditambahkan di akhir antrean
        
        Args:
            nama_pelanggan (str): Nama pelanggan yang masuk antrean
        """
        # Menambahkan pelanggan ke akhir antrean (FIFO)
        self.antrean.append(nama_pelanggan)
        print(f"✓ {nama_pelanggan} masuk ke antrean")
        print(f"  Posisi antrean: {len(self.antrean)}")
        
        # Tampilkan status antrean
        self.tampilkan_antrean()

    def layani_pelanggan(self):
        """
        Menghapus antrean (Dequeue)
        Melayani pelanggan pertama dalam antrean (FIFO)
        
        Returns:
            str: Nama pelanggan yang dilayani, atau None jika antrean kosong
        """
        # Cek apakah antrean kosong
        if len(self.antrean) == 0:
            print("✗ Antrean kosong! Tidak ada pelanggan yang dilayani.")
            return None
        
        # Menghapus dan mengembalikan elemen pertama (index 0)
        pelanggan_dilayani = self.antrean.pop(0)
        print(f"✓ Melayani: {pelanggan_dilayani}")
        print(f"  Sisa antrean: {len(self.antrean)} orang")
        
        return pelanggan_dilayani
    
    def tampilkan_antrean(self):
        """
        Menampilkan seluruh isi antrean saat ini
        """
        if len(self.antrean) == 0:
            print("\n  [ Antrean Kosong ]\n")
        else:
            print("\n  ╔════════════════════════════════╗")
            print("  ║      ANTREAN KASIR SAAT INI    ║")
            print("  ╠════════════════════════════════╣")
            for i, nama in enumerate(self.antrean, 1):
                print(f"  ║  {i}. {nama:<27}║")
            print("  ╚════════════════════════════════╝\n")


# 4. SORTING - LAPORAN TRANSAKSI 
def urutkan_transaksi(list_harga):
    """
    Mengurutkan list harga secara manual menggunakan Insertion Sort.
    Algoritma ini mengurutkan data dari kecil ke besar.
    
    Cara kerja Insertion Sort:
    1. Mulai dari elemen kedua (index 1)
    2. Bandingkan dengan elemen sebelumnya
    3. Sisipkan elemen di posisi yang tepat
    4. Ulangi hingga semua elemen terurut
    
    Args:
        list_harga (list): List harga yang akan diurutkan
    
    Returns:
        list: List harga yang sudah terurut dari kecil ke besar
    """
    # Membuat copy dari list agar tidak mengubah list asli
    arr = list_harga.copy()
    n = len(arr)
    
    # Insertion Sort Algorithm
    # Loop mulai dari elemen kedua (index 1) hingga akhir
    for i in range(1, n):
        # Simpan nilai yang akan disisipkan
        key = arr[i]
        
        # Posisi untuk membandingkan (elemen sebelumnya)
        j = i - 1
        
        # Geser elemen yang lebih besar dari key ke kanan
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Geser ke kanan
            j -= 1
        
        # Sisipkan key di posisi yang tepat
        arr[j + 1] = key
    
    return arr


def format_rupiah(angka):
    """
    Fungsi helper untuk memformat angka menjadi format Rupiah
    
    Args:
        angka (int): Angka yang akan diformat
    
    Returns:
        str: String angka dalam format Rupiah
    """
    return f"Rp {angka:,}".replace(',', '.')


def tampilkan_katalog_lengkap(data_buku):
    """
    Menampilkan katalog buku dalam format yang lebih rapi dan terstruktur
    
    Args:
        data_buku (dict): Dictionary berisi data buku
    """
    if not data_buku:
        print("\n✗ Katalog buku kosong atau gagal dimuat!")
        return
    
    print("\n" + "="*70)
    print("                        KATALOG BUKU TOKO                          ")
    print("="*70)
    print(f"{'No.':<5} {'Kode':<8} {'Judul Buku':<35} {'Harga':<20}")
    print("-"*70)
    
    nomor = 1
    for kode, info in data_buku.items():
        judul = info['judul']
        harga = format_rupiah(info['harga'])
        print(f"{nomor:<5} {kode:<8} {judul:<35} {harga:<20}")
        nomor += 1
    
    print("="*70 + "\n")


def menu_kelola_promosi(list_promosi):
    """
    Sub-menu untuk mengelola daftar promosi
    
    Args:
        list_promosi (LinkedListPromosi): Object linked list promosi
    """
    while True:
        print("\n╔════════════════════════════════════════╗")
        print("║     KELOLA DAFTAR PROMOSI BUKU        ║")
        print("╠════════════════════════════════════════╣")
        print("║  1. Tambah Buku ke Promosi            ║")
        print("║  2. Lihat Daftar Promosi              ║")
        print("║  3. Kembali ke Menu Utama             ║")
        print("╚════════════════════════════════════════╝")
        
        pilihan = input("\nPilih menu (1-3): ").strip()
        
        if pilihan == '1':
            judul_baru = input("Masukkan judul buku untuk promosi: ").strip()
            if judul_baru:
                list_promosi.tambah_buku_promosi(judul_baru)
            else:
                print("✗ Judul tidak boleh kosong!")
        
        elif pilihan == '2':
            list_promosi.tampilkan_promosi()
        
        elif pilihan == '3':
            break
        
        else:
            print("✗ Pilihan tidak valid! Silakan pilih 1-3.")


def menu_kelola_antrean(antrean_toko):
    """
    Sub-menu untuk mengelola antrean kasir
    
    Args:
        antrean_toko (AntreanKasir): Object antrean kasir
    """
    while True:
        print("\n╔════════════════════════════════════════╗")
        print("║       KELOLA ANTREAN KASIR            ║")
        print("╠════════════════════════════════════════╣")
        print("║  1. Tambah Pelanggan ke Antrean       ║")
        print("║  2. Layani Pelanggan                  ║")
        print("║  3. Lihat Antrean Saat Ini            ║")
        print("║  4. Kembali ke Menu Utama             ║")
        print("╚════════════════════════════════════════╝")
        
        pilihan = input("\nPilih menu (1-4): ").strip()
        
        if pilihan == '1':
            nama = input("Nama Pelanggan: ").strip()
            if nama:
                antrean_toko.tambah_antrean(nama)
            else:
                print("✗ Nama tidak boleh kosong!")
        
        elif pilihan == '2':
            antrean_toko.layani_pelanggan()
            if len(antrean_toko.antrean) > 0:
                antrean_toko.tampilkan_antrean()
        
        elif pilihan == '3':
            antrean_toko.tampilkan_antrean()
        
        elif pilihan == '4':
            break
        
        else:
            print("✗ Pilihan tidak valid! Silakan pilih 1-4.")


# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    """
    Fungsi utama program yang menampilkan menu dan mengelola alur program
    """
    print("\n" + "="*70)
    print("        SISTEM MANAJEMEN RIWAYAT TRANSAKSI TOKO BUKU")
    print("="*70)
    
    # Inisialisasi Data
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    # Main Loop
    while True:
        print("\n╔════════════════════════════════════════════════════════╗")
        print("║          SISTEM MANAJEMEN TOKO BUKU                   ║")
        print("╠════════════════════════════════════════════════════════╣")
        print("║  1. Lihat Katalog Buku (Dictionary/File)              ║")
        print("║  2. Kelola Daftar Promosi (Linked List)               ║")
        print("║  3. Kelola Antrean Kasir (Queue)                      ║")
        print("║  4. Lihat Laporan Penjualan Terurut (Sorting)         ║")
        print("║  5. Keluar                                            ║")
        print("╚════════════════════════════════════════════════════════╝")
        
        pilihan = input("\nPilih menu (1-5): ").strip()

        # Menu 1: Lihat Katalog Buku
        if pilihan == '1':
            tampilkan_katalog_lengkap(data_buku)
        
        # Menu 2: Kelola Daftar Promosi
        elif pilihan == '2':
            menu_kelola_promosi(list_promosi)

        # Menu 3: Kelola Antrean Kasir
        elif pilihan == '3':
            menu_kelola_antrean(antrean_toko)

        # Menu 4: Lihat Laporan Penjualan Terurut
        elif pilihan == '4':
            print("\n" + "="*70)
            print("              LAPORAN RIWAYAT TRANSAKSI PENJUALAN")
            print("="*70)
            
            print("\nHarga Transaksi Sebelum Diurutkan:")
            print("  ", [format_rupiah(h) for h in riwayat_transaksi])
            
            # Proses sorting menggunakan Insertion Sort
            hasil_sort = urutkan_transaksi(riwayat_transaksi)
            
            print("\nHarga Transaksi Sesudah Diurutkan (Insertion Sort):")
            print("  ", [format_rupiah(h) for h in hasil_sort])
            
            print("\n" + "-"*70)
            print(f"Total Transaksi: {len(hasil_sort)} transaksi")
            print(f"Transaksi Terkecil: {format_rupiah(hasil_sort[0])}")
            print(f"Transaksi Terbesar: {format_rupiah(hasil_sort[-1])}")
            print(f"Total Penjualan: {format_rupiah(sum(hasil_sort))}")
            print("="*70 + "\n")

        # Menu 5: Keluar dari Program
        elif pilihan == '5':
            print("\n" + "="*70)
            print("           Terima kasih telah menggunakan sistem ini!")
            print("                Program selesai. Sampai jumpa!")
            print("="*70 + "\n")
            break
        
        # Input tidak valid
        else:
            print("\n✗ Pilihan tidak valid! Silakan pilih menu 1-5.")


# Entry point program
if __name__ == "__main__":
    main()





