#========================================================================================
#Nama    : Mohammad Syafiq Farghany
#NIM     : J0403251125
#Kelas   : Teknologi Rekayasa Perangkat Lunak A1
#========================================================================================


#========================================================================================
#Implementasi Dasar : Stack
#========================================================================================

class Node:
    #kontruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data #menyimpan data atau nilai pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)


#Stack ada operasi push(memasukkan head baru) dan pop(menghapus head)

class stack:
    def __init__(self):
        self.top = None #top menunjuk ke node paling atas (awalnya kosong / Nol)
        
    def push(self, data): #memasukkan data baru pada stack
        #1 membuat node baru 
        nodeBaru = Node(data) #instantiasi/memanggil konstruktor pada class Node
        
        #2 Node baru  menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top
        
        #3 geser top ke node baru (head yang lama -> head yang baru)
        self.top = nodeBaru
        
    def is_empty(self):
        return self.top is None #mengembalikan True jika stack kosong, False jika tidak
        
    def pop(self):  #mengambil / menghapus node paling atas (top/head)
        
        if self.top is None: #jika stack kosong
            print("Stack kosong, tidak bisa pop")
            return None #kembalikan None jika stack kosong
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel (peek)
        self.top = self.top.next #geser top ke node berikutnya
        return data_terhapus #kembalikan data yang terhapus
        #F --> None
        
    def peek(self):
        if self.is_empty(): #jika stack kosong
            return None #kembalikan None jika stack kosong
        return self.top.data #kembalikan data pada top tanpa menghapusnya
        
    def tampilkan(self):
        #Top --> F -> A
        current = self.top #current menunjuk ke top
        print("Top ->"  ,  end=" ") #cetak data pada node saat ini
        while current is not None: 
            print(current.data, end=" -> ") #cetak data pada node saat ini
            current = current.next #pindah ke node berikutnya   
        print("None") #akhir dari stack
        
#Instantiasi class Stack
s = stack()
s.push("F")
s.push("A")
s.tampilkan()
print("Peek (Lihat Top):", s.peek()) 
s.pop
s.tampilkan()#Lihat data pada top tanpa menghapusnya
