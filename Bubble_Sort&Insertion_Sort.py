import time

def bubble_sort(data):
    n = len(data)
    waktu_mulai = time.time()

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

        if i < 5 or i >= n - 6:
            print(f"Iterasi ke-{i + 1} : {data}")

    waktu_akhir = time.time()
    waktu_eksekusi = waktu_akhir - waktu_mulai

    return data, waktu_eksekusi

def insertion_sort(data):
    n = len(data)
    waktu_mulai = time.time()

    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

        if i < 6 or i >= n - 5:
            print(f"Iterasi ke-{i}: {data}")

    waktu_akhir = time.time()
    waktu_eksekusi = waktu_akhir - waktu_mulai

    return data, waktu_eksekusi

def main():
    data = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7, 26, 85, 46, 39, 40, 9,
           36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32,
           31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]

    print("===============================================================")
    print("     PROGRAM PENGURUTAN DATA ANGKA MENGGUNAKAN ALGORITMA"
          "\n            BUBBLE SORT ATAU INSERTION SORT")
    print("===============================================================")

    while True:
        print("Jenis Algoritma Yang Tersedia : ")
        print("1. Algoritma Bubble Sort")
        print("2. Algoritma Insertion Sort")
        print("===============================================================")
        pilihan = input("Pilih Jenis Algoritma Yang Diinginkan (1/2) : ")
        print("===============================================================")
        if pilihan.lower() == "1":
            print("\nData Sebelum Pengurutan :")
            print(data)
            print("\nIterasi yang Terjadi ")
            sorted_arr, waktu_eksekusi = bubble_sort(data.copy())
            break
        elif pilihan.lower() == "2":
            print("\nData Sebelum Pengurutan :")
            print(data)
            print("\nIterasi yang Terjadi ")
            sorted_arr, waktu_eksekusi = insertion_sort(data.copy())
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

    print("\nData Setelah Pengurutan:")
    print(sorted_arr)
    print("\nWaktu Komputasi Pengurutan:", waktu_eksekusi, "detik")
    print("===============================================================")
    lanjut = input("Apakah Anda ingin melanjutkan perhitungan? (ya/tidak) : ")
    print("===============================================================")

    while lanjut.lower() == "ya":
        print("\nJenis Algoritma Yang Tersedia : ")
        print("1. Algoritma Bubble Sort")
        print("2. Algoritma Insertion Sort")
        print("===============================================================")
        pilihan = input("Pilih Jenis Algoritma Yang Diinginkan (1/2) : ")
        print("===============================================================")
        if pilihan.lower() == "1":
            print("\nData Sebelum Pengurutan :")
            print(data)
            print("\nIterasi yang Terjadi ")
            sorted_arr, waktu_eksekusi = bubble_sort(data.copy())
            break
        elif pilihan.lower() == "2":
            sorted_arr, waktu_eksekusi = insertion_sort(data.copy())
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

    print("\nData Setelah Pengurutan:")
    print(sorted_arr)
    print("\nWaktu Komputasi Pengurutan:", waktu_eksekusi, "detik")
    print("===============================================================")
    lanjut = input("Apakah Anda ingin melanjutkan perhitungan? (ya/tidak) : ")
    print("===============================================================")

if __name__ == '__main__':
    main()