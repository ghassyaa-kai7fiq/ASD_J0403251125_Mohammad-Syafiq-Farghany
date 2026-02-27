# ========================================================== 
# Contoh Rekursi 3: Menjumlahkan Elemen List
# ========================================================== 
def jumlah_list(data, index=0): 
    # Base case: jika index sudah mencapai panjang list 
    if index == len(data): 
        return 0 # Kembalikan 0 sebagai base case.
    # Recursive case: elemen sekarang + jumlah elemen setelahnya 
    return data[index] + jumlah_list(data, index + 1)# Penjumlahan elemen rekursif.
print(jumlah_list([2, 4, 6, 8]))  # Output: 20

# ==========================================================
# Deskripsi Penjelasan:
# ==========================================================

# Pada contoh di atas, fungsi jumlah_list menggunakan rekursi untuk menghitung jumlah elemen dalam sebuah list.
# Fungsi jumlah_list menggunakan rekursi untuk menghitung jumlah elemen dalam sebuah list.
    # Base case terjadi ketika index sudah mencapai panjang list, dimana fungsi akan mengembalikan 0, menandakan bahwa tidak ada elemen yang tersisa untuk dijumlahkan.

# Untuk setiap elemen dalam list, fungsi menambahkan nilai elemen saat ini (data[index]) dengan hasil pemanggilan rekursif jumlah_list untuk elemen berikutnya (index + 1)
    # sehingga masalahnya diperkecil setiap kali fungsi dipanggil.

# Maka hasilnya adalah:
    # jumlah_list([2, 4, 6, 8]) = 2 + jumlah_list([4, 6, 8])
    # jumlah_list([4, 6, 8]) = 4 + jumlah_list([6, 8])
    # jumlah_list([6, 8]) = 6 + jumlah_list([8])
    # jumlah_list([8]) = 8 + jumlah_list([])
    # jumlah_list([]) = 0 (base case)

# Sehingga hasil akhirnya adalah:
    # jumlah_list([8]) = 8 + 0 = 8 
    # jumlah_list([6, 8]) = 6 + 8 = 14
    # jumlah_list([4, 6, 8]) = 4 + 14
    # jumlah_list([2, 4, 6, 8]) = 2 + 18 = 20

# Penjelasan ini menunjukkan
    # bagaimana fungsi jumlah_list bekerja dengan menggunakan rekursi,
    # dimana setiap kali fungsi dipanggil,
    # ia masuk ke dalam level rekursi yang lebih dalam hingga mencapai base case,
    # kemudian keluar dari level rekursi tersebut secara berurutan,
    # menghasilkan jumlah total dari elemen-elemen dalam list.
# Sehingga hasilnya adalah 20, yang merupakan jumlah dari elemen-elemen dalam list [2, 4, 6, 8].