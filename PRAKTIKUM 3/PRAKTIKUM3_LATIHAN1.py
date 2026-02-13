class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def delete_node(self, key):
        temp = self.head
        
        if temp is None:
            print("Linked list kosong. Tidak ada node yang dihapus.")
            return
        
        if temp.data == key:
            self.head = temp.next
            if self.head is None:
                self.tail = None
            elif temp == self.tail:
                self.tail = self.head
            print("Node dengan nilai", key, "berhasil dihapus (node pertama)")
            temp = None
            return
        
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        
        if temp is None:
            print("Node dengan nilai", key, "tidak ditemukan")
            return
        
        if temp == self.tail:
            prev.next = None
            self.tail = prev
            print("Node dengan nilai", key, "berhasil dihapus (node terakhir)")
        else:
            prev.next = temp.next
            print("Node dengan nilai", key, "berhasil dihapus (node di tengah)")
        
        temp = None
    
    def display(self):
        if not self.head:
            print("Linked list kosong")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

def praktikum3_latihan1():
    print("LATIHAN 1: MENGHAPUS NODE DENGAN NILAI TERTENTU")
    print("=" * 50)
    
    ll = LinkedList()
    ll.insert_at_end(3)
    ll.insert_at_end(5)
    ll.insert_at_end(13)
    ll.insert_at_end(2)
    ll.insert_at_end(7)
    ll.insert_at_end(9)
    
    print("\nLinked List awal:")
    ll.display()
    
    print("\nMenghapus node dengan nilai 13:")
    ll.delete_node(13)
    ll.display()
    
    print("\nMenghapus node dengan nilai 3 (node pertama):")
    ll.delete_node(3)
    ll.display()
    
    print("\nMenghapus node dengan nilai 9 (node terakhir):")
    ll.delete_node(9)
    ll.display()
    
    print("\nMenghapus node dengan nilai 100 (tidak ada):")
    ll.delete_node(100)
    ll.display()
    
    print("\nMenghapus semua node:")
    ll.delete_node(5)
    ll.delete_node(2)
    ll.delete_node(7)
    ll.display()
    
    print("\nMenghapus dari linked list kosong:")
    ll.delete_node(10)

praktikum3_latihan1()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert_after(self, prev_node_data, data):
        temp = self.head
        while temp and temp.data != prev_node_data:
            temp = temp.next
        if not temp:
            print("Node sebelumnya tidak ditemukan")
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        if temp == self.tail:
            self.tail = new_node
    
    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            if self.head is None:
                self.tail = None
            temp = None
            print("Node dengan nilai", key, "telah dihapus")
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            print("Node dengan nilai", key, "tidak ditemukan")
            return
        prev.next = temp.next
        if temp == self.tail:
            self.tail = prev
        temp = None
        print("Node dengan nilai", key, "telah dihapus")
    
    def delete_first(self):
        if self.head:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            print("Node pertama telah dihapus")
    
    def delete_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            self.tail = None
            print("Node terakhir telah dihapus")
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        self.tail = temp
        print("Node terakhir telah dihapus")
    
    def search(self, key):
        temp = self.head
        position = 1
        while temp:
            if temp.data == key:
                print("Elemen", key, "ditemukan pada posisi", position)
                return True
            temp = temp.next
            position += 1
        print("Elemen", key, "tidak ditemukan")
        return False
    
    def display(self):
        if not self.head:
            print("Linked List kosong")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

def main():
    print("=" * 60)
    print("LATIHAN 1: IMPLEMENTASI DELETE NODE PADA SINGLE LINKED LIST")
    print("=" * 60)
    
    ll = LinkedList()
    
    while True:
        print("\n--- MENU LINKED LIST ---")
        print("1. Tambah data di akhir")
        print("2. Tambah data di awal")
        print("3. Tambah data setelah node tertentu")
        print("4. Hapus node berdasarkan nilai")
        print("5. Hapus node pertama")
        print("6. Hapus node terakhir")
        print("7. Cari data")
        print("8. Tampilkan linked list")
        print("9. Keluar")
        
        pilihan = input("Pilih menu (1-9): ")
        
        if pilihan == '1':
            data = int(input("Masukkan data: "))
            ll.insert_at_end(data)
            print("Data", data, "ditambahkan di akhir")
            ll.display()
        
        elif pilihan == '2':
            data = int(input("Masukkan data: "))
            ll.insert_at_beginning(data)
            print("Data", data, "ditambahkan di awal")
            ll.display()
        
        elif pilihan == '3':
            prev = int(input("Masukkan data node sebelumnya: "))
            data = int(input("Masukkan data baru: "))
            ll.insert_after(prev, data)
            ll.display()
        
        elif pilihan == '4':
            key = int(input("Masukkan nilai node yang akan dihapus: "))
            ll.delete_node(key)
            ll.display()
        
        elif pilihan == '5':
            ll.delete_first()
            ll.display()
        
        elif pilihan == '6':
            ll.delete_last()
            ll.display()
        
        elif pilihan == '7':
            key = int(input("Masukkan data yang dicari: "))
            ll.search(key)
        
        elif pilihan == '8':
            print("\nISI LINKED LIST SAAT INI:")
            ll.display()
        
        elif pilihan == '9':
            print("Program selesai")
            break
        
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()