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
    
    def insert_multiple(self, data_list):
        for data in data_list:
            self.insert_at_end(data)
    
    def reverse(self):
        if not self.head:
            print("Linked List kosong")
            return
        if not self.head.next:
            print("Linked List hanya memiliki 1 node")
            return
        old_head = self.head
        prev = None
        current = self.head
        next_node = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        self.tail = old_head
        self.tail.next = None
        print("Linked List telah dibalik")
    
    def display(self):
        if not self.head:
            print("Linked List kosong")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
    
    def clear(self):
        self.head = None
        self.tail = None
        print("Linked List dikosongkan")

def main():
    print("=" * 60)
    print("LATIHAN 5: MEMBALIK (REVERSE) SINGLE LINKED LIST")
    print("=" * 60)
    
    ll = LinkedList()
    
    while True:
        print("\n--- MENU SINGLE LINKED LIST ---")
        print("1. Tambah data di akhir")
        print("2. Tambah banyak data (pisahkan dengan spasi)")
        print("3. Tampilkan linked list")
        print("4. Balik linked list (reverse)")
        print("5. Kosongkan linked list")
        print("6. Keluar")
        
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1':
            data = int(input("Masukkan data: "))
            ll.insert_at_end(data)
            print("Data", data, "ditambahkan")
            ll.display()
        
        elif pilihan == '2':
            data_input = input("Masukkan data (pisahkan dengan spasi): ")
            data_list = [int(x) for x in data_input.split()]
            ll.insert_multiple(data_list)
            print("Data", data_list, "ditambahkan")
            ll.display()
        
        elif pilihan == '3':
            print("\nISI LINKED LIST SAAT INI:")
            ll.display()
        
        elif pilihan == '4':
            print("\nSEBELUM REVERSE:")
            ll.display()
            ll.reverse()
            print("SETELAH REVERSE:")
            ll.display()
        
        elif pilihan == '5':
            ll.clear()
            ll.display()
        
        elif pilihan == '6':
            print("Program selesai")
            break
        
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()