#====================================================
# Nama    : Mohammad Syafiq Farghany
# NIM     : J0403251125
# Kelas  : Teknologi Rekayasa Perangkat Lunak A1/P1
#====================================================

#===================================================================================
# Praktikum 6 : Buble sort Descending
# Latihan Dasar : Membandingkan dan Menukar Nilai besar & kecil Secara (Menurun)
#===================================================================================

def bubbleSort(alist):
    exchanges = True

    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]<alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum-1


data = [54,26,93,17,77,31,44,55,20]
bubbleSort(data)
print(data)
# Output
# [93, 77, 55, 54, 44, 31, 26, 20, 17]