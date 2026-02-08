# File path for data
DATA_MAHASISWA = "data_mahasiswa.txt"

# ------------------------------- 
# 1) Read: Baca data dari file 
# ------------------------------- 
def baca_data_mahasiswa(filepath):
    """
    Membaca data mahasiswa dari file CSV.
    Format per baris: NIM,NAMA,NILAI
    Mengembalikan dictionary dengan struktur:
    {NIM: {"nama": NAMA, "nilai": NILAI}, ...}
    """
    data_dict = {}
    
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    parts = line.split(",")
                    if len(parts) == 3:
                        nim, nama, nilai = parts
                        data_dict[nim] = {"nama": nama, "nilai": int(nilai)}
    except FileNotFoundError:
        print(f"File '{filepath}' tidak ditemukan. Memulai dengan data kosong.")
    except ValueError:
        print("Error: Format nilai tidak valid. Pastikan nilai berupa angka.")
    
    return data_dict

# ------------------------------- 
# 2) Tampilkan semua data 
# ------------------------------- 
def tampilkan_semua_mahasiswa(data_dict): 
    """ 
    Menampilkan semua data mahasiswa dalam format tabel. 
    """ 
    if len(data_dict) == 0: 
        print("Data mahasiswa kosong.") 
        return 
 
    print("\n=== DAFTAR MAHASISWA ===") 
    print(f"{'NIM':<10} | {'Nama':<12} | {'Nilai':>5}") 
    print("-" * 32) 

    for nim in sorted(data_dict.keys()): 
        nama = data_dict[nim]["nama"] 
        nilai = data_dict[nim]["nilai"] 
        print(f"{nim:<10} | {nama:<12} | {nilai:>5}") 


# ------------------------------- 
# 3) Cari mahasiswa berdasarkan NIM 
# ------------------------------- 
def cari_mahasiswa(data_dict): 
    """ 
    Mencari mahasiswa berdasarkan NIM (key dictionary). 
    """ 
    nim_cari = input("Masukkan NIM yang ingin dicari (contoh: J0403001): ").strip() 
 
    if nim_cari in data_dict: 
        nama = data_dict[nim_cari]["nama"] 
        nilai = data_dict[nim_cari]["nilai"] 
 
        print("\n=== Data Mahasiswa Ditemukan ===") 
        print(f"NIM   : {nim_cari}") 
        print(f"Nama  : {nama}") 
        print(f"Nilai : {nilai}") 
    else: 
        print("\nData tidak ditemukan. Pastikan NIM yang dimasukkan benar.") 
 
# ------------------------------- 
# 4) Update nilai mahasiswa 
# ------------------------------- 
def update_nilai_mahasiswa(data_dict): 
    """ 
    Mengubah nilai mahasiswa berdasarkan NIM. 
    Aturan: 
    - NIM harus ada 
  - Nilai baru harus 0–100 
    """ 
    nim = input("Masukkan NIM yang ingin diupdate nilainya: ").strip() 
 
    if nim not in data_dict: 
        print("NIM tidak ditemukan. Update dibatalkan.") 
        return 
 
    try: 
        nilai_baru = int(input("Masukkan nilai baru (0-100): ").strip()) 
    except ValueError: 
        print("Nilai harus berupa angka. Update dibatalkan.") 
        return 
 
    if nilai_baru < 0 or nilai_baru > 100: 
        print("Nilai harus antara 0 sampai 100. Update dibatalkan.") 
        return 
 
    nilai_lama = data_dict[nim]["nilai"] 
    data_dict[nim]["nilai"] = nilai_baru 
 
    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}.") 
 
 
# ------------------------------- 
# 5) Write: Simpan data ke file 
# ------------------------------- 
def simpan_data_mahasiswa(DATA_MAHASISWA, data_dict): 
    """ 
    Menyimpan data mahasiswa dari dictionary ke file. 
    Format per baris: NIM,NAMA,NILAI 
    """ 
    with open(DATA_MAHASISWA, "w", encoding="utf-8") as file: 
        for nim in sorted(data_dict.keys()): 
            nama = data_dict[nim]["nama"] 
            nilai = data_dict[nim]["nilai"] 
            file.write(f"{nim},{nama},{nilai}\n") 
 
 
# ========================================================== 
# Program Utama: Menu Interaktif 
# ========================================================== 
def main(): 
    # Load data saat program mulai 
    DATA_MAHASISWA = baca_data_mahasiswa(DATA_MAHASISWA) 
 
    while True: 
        print("\n=== MENU DATA MAHASISWA ===") 
        print("1. Tampilkan semua data") 
        print("2. Cari data berdasarkan NIM") 
        print("3. Update nilai mahasiswa") 
        print("4. Simpan data ke file") 
        print("0. Keluar") 
 
        pilihan = input("Pilih menu: ").strip() 
 
        if pilihan == "1": 
            tampilkan_semua_mahasiswa(DATA_MAHASISWA)
        elif pilihan == "2": 
            cari_mahasiswa(DATA_MAHASISWA) 
 
        elif pilihan == "3":
            update_nilai_mahasiswa(DATA_MAHASISWA) 
 
        elif pilihan == "4": 
            simpan_data_mahasiswa(DATA_MAHASISWA, DATA_MAHASISWA) 
            print("Data berhasil disimpan.") 
 
        elif pilihan == "0": 
            print("Program selesai.") 
            break 
 
        else: 
            print("Pilihan tidak valid. Silakan coba lagi.") 
 
 
if __name__ == "__main__": 
    main()