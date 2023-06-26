# AFIFA WULANDARI_F55121057_UAS_PAA2

Pada Algoritma TSP:
1. Worst Case: Dalam kasus terburuk, algoritma TSP akan mengunjungi setiap simpul dalam graf. Oleh karena itu, kompleksitas waktu algoritma TSP dalam kasus terburuk adalah O(n!), di mana n adalah jumlah simpul dalam graf. Ini karena setiap simpul memiliki n-1 kemungkinan simpul berikutnya yang belum dikunjungi.
2. Best Case: Dalam kasus terbaik, algoritma TSP akan menemukan jalur terpendek pada iterasi pertama tanpa harus mencoba semua kemungkinan. Namun, dalam implementasi yang diberikan, tidak ada optimasi khusus yang dilakukan untuk menangani kasus terbaik. Oleh karena itu, kompleksitas waktu algoritma TSP dalam kasus terbaik juga O(n!).
3. Average Case: Analisis rata-rata kompleksitas waktu algoritma TSP dapat rumit karena melibatkan distribusi kemungkinan yang berbeda untuk graf yang berbeda. Secara umum, algoritma TSP memiliki kompleksitas eksponensial, tetapi implementasi heuristik atau optimasi khusus dapat membantu mengurangi jumlah percobaan yang dilakukan dan meningkatkan kinerja dalam kasus-kasus umum.

Pada Algoritma Dijkstra:
1. Worst Case: Dalam kasus terburuk, algoritma Dijkstra akan memeriksa setiap simpul dalam graf dan setiap sisi yang terhubung. Oleh karena itu, kompleksitas waktu algoritma Dijkstra dalam kasus terburuk adalah O(V^2), di mana V adalah jumlah simpul dalam graf.
2. Best Case: Dalam kasus terbaik, algoritma Dijkstra akan menemukan jalur terpendek pada iterasi pertama tanpa harus memeriksa semua simpul. Jika node awal secara langsung terhubung dengan node akhir, algoritma dapat berhenti setelah satu iterasi. Dalam implementasi yang diberikan, kasus terbaik akan terjadi jika simpul awal langsung terhubung dengan simpul akhir. Oleh karena itu, kompleksitas waktu algoritma Dijkstra dalam kasus terbaik adalah O(1).
3. Average Case: Secara umum, kompleksitas waktu rata-rata algoritma Dijkstra adalah O(V^2), tetapi dapat dikurangi menjadi O((V + E) log V) dengan menggunakan implementasi menggunakan struktur data antrian prioritas, seperti heap biner atau Fibonacci heap, di mana E adalah jumlah sisi dalam graf.

Pada Algoritma Bubble Sort:
1. Worst Case: Pada kasus terburuk, algoritma Bubble Sort akan memeriksa setiap elemen dalam data pada setiap iterasi. Jumlah iterasi yang dibutuhkan adalah (n-1), di mana n adalah jumlah elemen dalam data. Kompleksitas waktu Bubble Sort dalam kasus terburuk adalah O(n^2).
2. Best Case: Pada kasus terbaik, jika data sudah dalam keadaan terurut, maka algoritma Bubble Sort akan mengidentifikasi ini pada iterasi pertama dan berhenti. Kompleksitas waktu Bubble Sort dalam kasus terbaik adalah O(n), karena hanya satu iterasi yang dilakukan.
3. Average Case: Pada kasus rata-rata, tidak ada asumsi khusus tentang data yang diurutkan atau tidak diurutkan. Oleh karena itu, kompleksitas waktu Bubble Sort dalam kasus rata-rata juga O(n^2).

Pada Algoritma Insertion Sort:
1. Worst Case: Pada kasus terburuk, setiap elemen akan memerlukan pemindahan ke posisi awal dalam setiap iterasi, karena elemen tersebut merupakan elemen terkecil dalam data yang belum diurutkan. Jumlah iterasi yang dibutuhkan adalah (n-1), di mana n adalah jumlah elemen dalam data. Kompleksitas waktu Insertion Sort dalam kasus terburuk adalah O(n^2).
2. Best Case: Pada kasus terbaik, jika data sudah dalam keadaan terurut, maka setiap iterasi hanya memerlukan satu perbandingan. Kompleksitas waktu Insertion Sort dalam kasus terbaik adalah O(n), karena hanya satu iterasi yang dilakukan.
3. Average Case: Pada kasus rata-rata, tidak ada asumsi khusus tentang data yang diurutkan atau tidak diurutkan. Oleh karena itu, kompleksitas waktu Insertion Sort dalam kasus rata-rata juga O(n^2).
