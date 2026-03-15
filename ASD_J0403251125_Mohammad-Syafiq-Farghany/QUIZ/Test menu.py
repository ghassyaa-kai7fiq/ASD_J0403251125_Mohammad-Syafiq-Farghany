
import json

BOOK_FILE = "books.json"

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head
        if not current:
            print("Tidak ada promosi.")
            return
        while current:
            print(current.data)
            current = current.next

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            print("Antrean kosong.")
            return
        for item in self.items:
            print(item)

books = {}
promotions = LinkedList()
queue = Queue()
sales = []  # List of transactions: {'customer': str, 'books': list, 'total': int}

def load_books():
    try:
        with open(BOOK_FILE, 'r') as f:
            global books
            books = json.load(f)
    except FileNotFoundError:
        books = {}

def save_books():
    with open(BOOK_FILE, 'w') as f:
        json.dump(books, f)

def display_menu():
    print("""--- SISTEM MANAJEMEN TOKO BUKU ---
1. Lihat Katalog Buku (Dictionary/File)
2. Kelola Daftar Promosi (Linked List)
3. Kelola Antrean Kasir (Queue)
4. Lihat Laporan Penjualan Terurut (Sorting)
5. Keluar""")

def display_catalog():
    if not books:
        print("Katalog kosong.")
        return
    for title, info in books.items():
        print(f"{title}: {info['author']} - Rp{info['price']}")

def manage_promotions():
    while True:
        print("\n--- Kelola Daftar Promosi ---")
        print("1. Tambah Promosi")
        print("2. Hapus Promosi")
        print("3. Lihat Promosi")
        print("4. Kembali")
        choice = input("Pilih: ").strip()
        if choice == '1':
            promo = input("Masukkan promosi: ")
            promotions.add(promo)
            print("Promosi ditambahkan.")
        elif choice == '2':
            promo = input("Masukkan promosi untuk dihapus: ")
            promotions.remove(promo)
            print("Promosi dihapus.")
        elif choice == '3':
            promotions.display()
        elif choice == '4':
            break
        else:
            print("Pilihan tidak valid.")

def manage_queue():
    while True:
        print("\n--- Kelola Antrean Kasir ---")
        print("1. Tambah Pelanggan ke Antrean")
        print("2. Proses Antrean (Transaksi)")
        print("3. Lihat Antrean")
        print("4. Kembali")
        choice = input("Pilih: ").strip()
        if choice == '1':
            customer = input("Nama pelanggan: ")
            queue.enqueue(customer)
            print(f"{customer} ditambahkan ke antrean.")
        elif choice == '2':
            if queue.is_empty():
                print("Antrean kosong.")
            else:
                customer = queue.dequeue()
                print(f"Memproses transaksi untuk {customer}")
                bought_books = []
                total = 0
                while True:
                    display_catalog()
                    book = input("Pilih buku (atau 'selesai'): ").strip()
                    if book.lower() == 'selesai':
                        break
                    if book in books:
                        bought_books.append(book)
                        total += books[book]['price']
                        print(f"{book} ditambahkan. Subtotal: Rp{total}")
                    else:
                        print("Buku tidak ditemukan.")
                sales.append({'customer': customer, 'books': bought_books, 'total': total})
                print(f"Transaksi selesai. Total: Rp{total}")
        elif choice == '3':
            queue.display()
        elif choice == '4':
            break
        else:
            print("Pilihan tidak valid.")

def view_sales_report():
    if not sales:
        print("Tidak ada penjualan.")
        return
    sorted_sales = sorted(sales, key=lambda x: x['total'], reverse=True)
    print("\n--- Laporan Penjualan Terurut ---")
    for sale in sorted_sales:
        print(f"Pelanggan: {sale['customer']}, Buku: {', '.join(sale['books'])}, Total: Rp{sale['total']}")

def main():
    load_books()
    while True:
        display_menu()
        choice = input("Pilih menu (1-5): ").strip()
        if choice == '1':
            display_catalog()
        elif choice == '2':
            manage_promotions()
        elif choice == '3':
            manage_queue()
        elif choice == '4':
            view_sales_report()
        elif choice == '5':
            print("Terima kasih telah menggunakan sistem.")
            save_books()
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1-5.")

if __name__ == "__main__":
    main()



