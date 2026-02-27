# ========================================================== 
# Contoh Backtracking 1: Kombinasi Biner (n) 
# ========================================================== 
def biner(n, hasil=""): 
    # Base case: jika panjang string sudah n, cetak hasil 
    if len(hasil) == n: 
        print(hasil) # Cetak saat lengkap, backtrack
        return # Kembali untuk mencoba kombinasi lain
    # Choose + Explore: tambah '0' 
    biner(n, hasil + "0") # Tambah '0', panggil rekursi

    # Choose + Explore: tambah '1' 
    biner(n, hasil + "1") # Tambah '1', panggil rekursi

biner(3) 

# ==========================================================
# Deskripsi Penjelasan:
# ==========================================================

# Pada contoh di atas, fungsi biner menggunakan backtracking untuk menghasilkan semua kombinasi biner dari panjang n.
# Fungsi biner memiliki dua langkah utama: "Choose + Explore" dan "Backtrack".
    # "Choose + Explore" terjadi ketika fungsi menambahkan '0' atau '1'
    # ke string hasil dan memanggil dirinya sendiri untuk melanjutkan proses hingga mencapai base case.
    # Base case terjadi ketika panjang string hasil sudah mencapai n, dimana fungsi akan mencetak hasil
    # dan kembali (backtrack) untuk mencoba kombinasi lainnya.
# Sehingga hasilnya adalah semua kombinasi biner dari panjang 3, yaitu:
    # 000
    # 001
    # 010
    # 011
    # 100
    # 101
    # 110
    # 111
# Dari hal tersebut backtracking hasilkan semua kombinasi biner.
# Sehingga hasilnya adalah semua kombinasi biner dari panjang 3, yaitu 000, 001, 010, 011, 100, 101, 110, dan 111.
# maka kesimpulannya ialah dengan menggunakan backtracking, Kita dapat menghasilkan semua kombinasi.