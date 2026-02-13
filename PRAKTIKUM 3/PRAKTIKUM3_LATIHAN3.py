class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
            new_node.prev = self.tail
            self.tail = new_node
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
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
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node
        if temp == self.tail:
            self.tail = new_node
    
    def delete_node(self, key):
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        if not temp:
            print("Node dengan nilai", key, "tidak ditemukan")
            return
        if temp == self.head:
            self.head = temp.next
            if self.head:
                self.head.prev = None
        else:
            temp.prev.next = temp.next
        if temp == self.tail:
            self.tail = temp.prev
            if self.tail:
                self.tail.next = None
        else:
            if temp.next:
                temp.next.prev = temp.prev
        print("Node dengan nilai", key, "telah dihapus")
    
    def search_forward(self, key):
        position = 1
        temp = self.head
        while temp:
            if temp.data == key:
                print("Elemen", key, "ditemukan pada posisi", position, "(pencarian dari head)")
                return True, position
            temp = temp.next
            position += 1
        print("Elemen", key, "tidak ditemukan (pencarian dari head)")
        return False, -1
    
    def search_backward(self, key):
        position_from_tail = 1
        temp = self.tail
        while temp:
            if temp.data == key:
                total_nodes = self.count_nodes()
                position_from_head = total_nodes - position_from_tail + 1
                print("Elemen", key, "ditemukan pada posisi", position_from_head, "(pencarian dari tail)")
                return True, position_from_head
            temp = temp.prev
            position_from_tail += 1
        print("Elemen", key, "tidak ditemukan (pencarian dari tail)")
        return False, -1
    
    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def display_forward(self):
        if not self.head:
            print("Doubly Linked List kosong")
            return
        print("Traversing forward:")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
    
    def display_backward(self):
        if not self.tail:
            print("Doubly Linked List kosong")
            return
        print("Traversing backward:")
        temp = self.tail
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("null")
    
    def display_details(self):
        if not self.head:
            print("Doubly Linked List kosong")
            return
        print("\n=== DETAIL DOUBLY LINKED LIST ===")
        print("Head:", self.head.data if self.head else "None")
        print("Tail:", self.tail.data if self.tail else "None")
        print("Jumlah node:", self.count_nodes())
        self.display_forward()
        self.display_backward()

def main():
    print("=" * 60)
    print("LATIHAN 3: PENCARIAN PADA DOUBLY LINKED LIST")
    print("=" * 60)
    
    dll = DoublyLinkedList()
    
    while True:
        print("\n--- MENU DOUBLY LINKED LIST ---")
        print("1. Tambah data di akhir")
        print("2. Tambah data di awal")
        print("3. Tambah data setelah node tertentu")
        print("4. Hapus node berdasarkan nilai")
        print("5. Cari data (dari head)")
        print("6. Cari data (dari tail)")
        print("7. Tampilkan DLL (maju)")
        print("8. Tampilkan DLL (mundur)")
        print("9. Tampilkan detail DLL")
        print("10. Keluar")
        
        pilihan = input("Pilih menu (1-10): ")
        
        if pilihan == '1':
            data = int(input("Masukkan data: "))
            dll.insert_at_end(data)
            print("Data", data, "ditambahkan di akhir")
            dll.display_forward()
        
        elif pilihan == '2':
            data = int(input("Masukkan data: "))
            dll.insert_at_beginning(data)
            print("Data", data, "ditambahkan di awal")
            dll.display_forward()
        
        elif pilihan == '3':
            prev = int(input("Masukkan data node sebelumnya: "))
            data = int(input("Masukkan data baru: "))
            dll.insert_after(prev, data)
            dll.display_forward()
        
        elif pilihan == '4':
            key = int(input("Masukkan nilai node yang akan dihapus: "))
            dll.delete_node(key)
            dll.display_forward()
        
        elif pilihan == '5':
            key = int(input("Masukkan data yang dicari: "))
            dll.search_forward(key)
        
        elif pilihan == '6':
            key = int(input("Masukkan data yang dicari: "))
            dll.search_backward(key)
        
        elif pilihan == '7':
            dll.display_forward()
        
        elif pilihan == '8':
            dll.display_backward()
        
        elif pilihan == '9':
            dll.display_details()
        
        elif pilihan == '10':
            print("Program selesai")
            break
        
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()