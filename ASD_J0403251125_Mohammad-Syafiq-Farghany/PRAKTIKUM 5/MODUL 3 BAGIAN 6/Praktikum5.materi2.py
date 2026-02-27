# ========================================================== 
# Contoh Rekursi 2: Tracing Masuk/Keluar 
# ========================================================== 
def hitung(n): 
# Base case 
    if n == 0: 
        print("Selesai")# Base case: mencetak "Selesai" dan berhenti ketika n = 0
        return 
    print("Masuk:", n)# Mencetak "Masuk:" diikuti dengan nilai n sebelum memanggil fungsi hitung dengan argumen n-1
    hitung(n - 1)# Recursive case: memanggil dirinya sendiri dengan argumen n-1, sehingga masalahnya diperkecil setiap kali fungsi dipanggil
    print("Keluar:", n)# Mencetak "Keluar:" diikuti dengan nilai n setelah pemanggilan rekursif selesai, menunjukkan bahwa fungsi sedang keluar dari level rekursi tersebut
hitung(3)# Output: (Masuk: 3, Masuk: 2, Masuk: 1, Selesai, Keluar: 1, Keluar: 2, Keluar: 3) *maka ini adalah hasil dari pemanggilan fungsi berulang dgn nilai n yang besar semakin kecil

# ==========================================================
# Deskripsi Penjelasan:
# ==========================================================
# Pada perogram berikut ialah Fungsi hitung menggunakan rekursi untuk menghitung nilai n hingga mencapai 0.
# Base case terjadi ketika n = 0, dimana fungsi akan mencetak "Selesai" dan berhenti.

# Untuk nilai n yang lebih besar dari 0, fungsi mencetak "Masuk:" diikuti dengan nilai n, kemudian memanggil dirinya sendiri dengan argumen n-1, sehingga masalahnya diperkecil setiap kali fungsi dipanggil.
# Setelah pemanggilan rekursif selesai, fungsi mencetak "Keluar:" diikuti dengan nilai n, menunjukkan bahwa fungsi sedang keluar dari level rekursi tersebut.
# Sehingga hasilnya adalah:
        # Masuk: 3
        # Masuk: 2
        # Masuk: 1
    # Selesai
        # Keluar: 1
        # Keluar: 2
        # Keluar: 3
# Penjelasan ini menunjukkan bagaimana fungsi hitung bekerja dengan menggunakan rekursi, dimana setiap kali fungsi dipanggil, ia masuk ke dalam level rekursi yang lebih dalam hingga mencapai base case, kemudian keluar dari level rekursi tersebut secara berurutan.