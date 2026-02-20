#========================================================================================
#Nama    : Mohammad Syafiq Farghany
#NIM     : J0403251125
#Kelas   : Teknologi Rekayasa Perangkat Lunak A1
#========================================================================================


#========================================================================================
#Implementasi Dasar : Node pada Linked List
#========================================================================================

class Node:
    #kontruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data #menyimpan data atau nilai pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)
        
#1) membuat node dengan instantiasi class Node
nodeA = Node("a") 
nodeB = Node("b")
nodeC = Node("c")

#2) Mendifinisikan head dan Menghubungkan node : A -> B -> C  None
head = nodeA #head menunjuk ke nodeA
nodeA.next = nodeB #nodeA menunjuk ke nodeB
nodeB.next = nodeC #nodeB menunjuk ke nodeC

#3) Traversal : Menelusuri node dari head sampai ke None
current = head #current menunjuk ke head
while current is not None: #selama current tidak menunjuk ke None
    print(current.data) #cetak data pada node saat ini
    current = current.next #pindah ke node berikutnya 
    


