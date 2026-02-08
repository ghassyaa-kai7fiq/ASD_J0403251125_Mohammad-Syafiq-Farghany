# File path untuk data stok barang
STOK_BARANG_FILE = "stok_barang.txt"

# ===============================================
# 1) READ: Baca data dari file stok_barang.txt
# ===============================================
def baca_stok_barang(filepath):
    """
    Membaca data stok barang dari file.
    Format per baris: KodeBarang,NamaBarang,Stok
    Mengembalikan dictionary dengan struktur:
    {KodeBarang: {"nama": NamaBarang, "stok": Stok}, ...}
    """
    data_dict = {}
    
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    parts = line.split(",")
                    if len(parts) == 3:
                        kode, nama, stok = parts
                        data_dict[kode] = {"nama": nama, "stok": int(stok)}
    except FileNotFoundError:
        print(f"File '{filepath}' tidak ditemukan. Memulai dengan data kosong.")
    except ValueError:
        print("Error: Format stok tidak valid. Pastikan stok berupa angka.")
    
    return data_dict

# ===============================================
# 2) TAMPILKAN: Tampilkan semua barang
# ===============================================
def tampilkan_semua_barang(data_dict):
    """
    Menampilkan semua data stok barang dalam format tabel.
    """
    if len(data_dict) == 0:
        print("Data barang kosong.")
        return
    
    print("\n=== DAFTAR STOK BARANG ===")
    print(f"{'Kode':<10} | {'Nama Barang':<15} | {'Stok':>5}")
    print("-" * 40)
    
    for kode in sorted(data_dict.keys()):
        nama = data_dict[kode]["nama"]
        stok = data_dict[kode]["stok"]
        print(f"{kode:<10} | {nama:<15} | {stok:>5}")

# ===============================================
# 3) CARI: Cari barang berdasarkan kode
# ===============================================
def cari_barang(data_dict):
    """
    Mencari barang berdasarkan kode barang.
    """
    kode_cari = input("Masukkan kode barang yang ingin dicari (contoh: BRG001): ").strip()
    
    if kode_cari in data_dict:
        nama = data_dict[kode_cari]["nama"]
        stok = data_dict[kode_cari]["stok"]
        
        print("\n=== Data Barang Ditemukan ===")
        print(f"Kode : {kode_cari}")
        print(f"Nama : {nama}")
        print(f"Stok : {stok}")
    else:
        print("\nBarang tidak ditemukan.")

# ===============================================
# 4) TAMBAH: Tambah barang baru
# ===============================================
def tambah_barang_baru(data_dict):
    """
    Menambahkan barang baru ke dalam stok.
    Aturan:
    - Kode barang harus unik (tidak boleh duplikat)
    - Stok awal harus >= 0
    """
    kode = input("Masukkan kode barang (contoh: BRG004): ").strip()
    
    # Validasi kode sudah ada
    if kode in data_dict:
        print("Kode sudah digunakan. Tambah barang dibatalkan.")
        return
    
    nama = input("Masukkan nama barang: ").strip()
    
    # Validasi input stok
    try:
        stok_awal = int(input("Masukkan stok awal (harus >= 0): ").strip())
    except ValueError:
        print("Stok harus berupa angka. Tambah barang dibatalkan.")
        return
    
    if stok_awal < 0:
        print("Stok tidak boleh negatif. Tambah barang dibatalkan.")
        return
    
    # Tambahkan barang ke dictionary
    data_dict[kode] = {"nama": nama, "stok": stok_awal}
    print(f"Barang '{nama}' (Kode: {kode}) berhasil ditambahkan dengan stok awal {stok_awal}.")

# ===============================================
# 5) UPDATE: Update stok barang (tambah/kurangi)
# ===============================================
def update_stok_barang(data_dict):
    """
    Mengubah stok barang (menambah atau mengurangi).
    Aturan:
    - Kode barang harus ada
    - Stok tidak boleh negatif
    """
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()
    
    # Validasi kode ada
    if kode not in data_dict:
        print("Kode barang tidak ditemukan. Update dibatalkan.")
        return
    
    print("\n=== Update Stok ===")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    
    pilihan_update = input("Pilih operasi (1/2): ").strip()
    
    try:
        jumlah = int(input("Masukkan jumlah: ").strip())
    except ValueError:
        print("Jumlah harus berupa angka. Update dibatalkan.")
        return
    
    if jumlah < 0:
        print("Jumlah tidak boleh negatif. Update dibatalkan.")
        return
    
    stok_lama = data_dict[kode]["stok"]
    
    if pilihan_update == "1":
        # Tambah stok
        stok_baru = stok_lama + jumlah
        data_dict[kode]["stok"] = stok_baru
        print(f"Stok berhasil ditambah. Stok {kode} berubah dari {stok_lama} menjadi {stok_baru}.")
    
    elif pilihan_update == "2":
        # Kurangi stok
        stok_baru = stok_lama - jumlah
        
        if stok_baru < 0:
            print(f"Stok tidak boleh negatif. Stok saat ini: {stok_lama}. Update dibatalkan.")
            return
        
        data_dict[kode]["stok"] = stok_baru
        print(f"Stok berhasil dikurangi. Stok {kode} berubah dari {stok_lama} menjadi {stok_baru}.")
    
    else:
        print("Pilihan tidak valid. Update dibatalkan.")

# ===============================================
# 6) WRITE: Simpan data ke file
# ===============================================
def simpan_stok_barang(filepath, data_dict):
    """
    Menyimpan data stok barang dari dictionary ke file.
    Format per baris: KodeBarang,NamaBarang,Stok
    """
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            for kode in sorted(data_dict.keys()):
                nama = data_dict[kode]["nama"]
                stok = data_dict[kode]["stok"]
                file.write(f"{kode},{nama},{stok}\n")
        print("Data berhasil disimpan ke file.")
    except IOError:
        print("Error: Gagal menyimpan file.")

# ===============================================
# PROGRAM UTAMA: Menu Interaktif
# ===============================================
def main():
    """
    Program utama dengan menu interaktif untuk mengelola stok barang.
    """
    # Load data saat program mulai
    data_barang = baca_stok_barang(STOK_BARANG_FILE)
    
    while True:
        print("\n" + "="*40)
        print("=== MENU MANAJEMEN STOK BARANG ===")
        print("="*40)
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        print("="*40)
        
        pilihan = input("Pilih menu (0-5): ").strip()
        
        if pilihan == "1":
            tampilkan_semua_barang(data_barang)
        
        elif pilihan == "2":
            cari_barang(data_barang)
        
        elif pilihan == "3":
            tambah_barang_baru(data_barang)
        
        elif pilihan == "4":
            update_stok_barang(data_barang)
        
        elif pilihan == "5":
            simpan_stok_barang(STOK_BARANG_FILE, data_barang)
        
        elif pilihan == "0":
            print("\nProgram selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# ===============================================
# Entry Point Program
# ===============================================
if __name__ == "__main__":
    main()