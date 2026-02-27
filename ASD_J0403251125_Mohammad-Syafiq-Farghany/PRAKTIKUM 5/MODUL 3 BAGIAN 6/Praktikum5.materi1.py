# ========================================================== 
# Contoh Rekursi 1: Faktorial 
# ========================================================== 

def faktorial(n): 
    # Base case: berhenti ketika n = 0 
    if n == 0: 
        return 1 # Faktorial dari 0 adalah 1
    # Recursive case: masalah diperkecil menjadi faktorial(n-1) 
    return n * faktorial(n - 1) # Balik ke n lagi dikalikan dengan Menarik fungsi faktorial dengan argumen n-1
print(faktorial(5))  # Output: 120 

# ==========================================================
# Deskripsi Penjelasan:
# ==========================================================
# Fungsi faktorial atau yang biasa dipanggil dengan "n!" adalah hasil perkalian semua bilangan bulat positif dari 1 hingga n.
# Dalam contoh di atas, fungsi faktorial menggunakan rekursi untuk menghitung nilai faktorial dari sebuah bilangan n.

# Base case terjadi ketika n = 0, dimana faktorial(0) didefinisikan sebagai 
    # 1. Untuk nilai n yang lebih besar dari 0, fungsi memanggil dirinya sendiri dengan argumen n-1, sehingga masalahnya diperkecil setiap kali fungsi dipanggil.
# maka faktorial(5) akan dihitung sebagai berikut:
    # faktorial(5) = 5 * faktorial(4)
    # faktorial(4) = 4 * faktorial(3)
    # faktorial(3) = 3 * faktorial(2)
    # faktorial(2) = 2 * faktorial(1)
    # faktorial(1) = 1 * faktorial(0)
    # faktorial(0) = 1 (base case)
# Sehingga hasilnya adalah:
    # faktorial(1) = 1 * 1 = 1
