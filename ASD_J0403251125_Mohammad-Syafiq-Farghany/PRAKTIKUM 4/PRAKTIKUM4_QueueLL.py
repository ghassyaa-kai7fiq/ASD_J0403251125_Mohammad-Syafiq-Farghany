#========================================================================================
#Nama    : Mohammad Syafiq Farghany
#NIM     : J0403251125
#Kelas   : Teknologi Rekayasa Perangkat Lunak A1
#========================================================================================


#========================================================================================
#Implementasi Dasar : Queue
#========================================================================================

class Node:
    #kontruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data #menyimpan data atau nilai pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)
        
class Queue:
    #buat konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang
    
    def is_empty(self):
        return self.front is None #mengembalikan True jika queue kosong, False jika tidak
    
    #membuat fungsi untuk menambahkan data baru pada bagian paling belakang
    def enqueue(self, data):
        nodeBaru = Node(data)
        
        #Jika queue kosong, maka front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        #jika queue tidak kosong, maka Letakkan data baru ke setelah rear, dan jadikan data baru sebagai rear
        self.rear.next = nodeBaru #Letakkan data baru pada setelahnya rear
        self.rear = nodeBaru #Jadikan data baru sebagai rear
        
        
    def dequeue(self):
        #menghapus data dari depan (front)
        data_terhapus = self.front.data #simpan data yang akan dihapus
        
        #geser front ke node berikutnya
        self.front = self.front.next
        
        #Jika setelah geser front menjadi None, maka queue menjadi kosong, sehingga rear juga harus diatur ke None
        if self.front is None:
            self.rear = None
        return data_terhapus #kembalikan data yang dihapus
        
    def tampilkan(self):
        current = self.front #current menunjuk ke front
        print("Front ->"  ,  end=" ") #cetak data pada node saat ini
        while current is not None: 
            print(current.data, end=" -> ") #cetak data pada node saat ini
            current = current.next #pindah ke node berikutnya   
        print("Rear") #akhir dari queue
        
#Instantiasi class Queue
q = Queue()
q.enqueue("F")
q.enqueue("A")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()