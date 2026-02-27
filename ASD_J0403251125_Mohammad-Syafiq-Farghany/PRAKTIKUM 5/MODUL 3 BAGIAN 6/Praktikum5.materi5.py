# ========================================================== 
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning) 
# ========================================================== 

def biner_batas(n, batas, hasil="", jumlah_1=0): #Definisi fungsi backtracking.
    # Pruning: jika jumlah_1 sudah melewati batas, berhenti 
    if jumlah_1 > batas: #Pruning batasi pencarian.
        return #Hentikan cabang ini

    # Base case 
    if len(hasil) == n: #Cek panjang terpenuhi
        print(hasil) # Cetak kombinasi valid
        return #Kembali ke pemanggil.

    # Pilih '0' 
    biner_batas(n, batas, hasil + "0", jumlah_1) #Panggil rekursi dengan 0
    # Pilih '1' 
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1) #Panggil rekursi tambah 1.
biner_batas(4, 2) #jalankan Input menjadi Output.