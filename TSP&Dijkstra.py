import networkx as nx
import time

#Program TSP
def tsp(graph, mulai):
    def node_to_int(node):
        return ord(node) - ord('A')

    def int_to_node(num):
        return chr(num + ord('A'))

    n = graph.number_of_nodes()
    visited = [False] * n
    jalur = []
    jalur.append(mulai)
    visited[node_to_int(mulai)] = True
    total_bobot = 0
    waktu_mulai = time.time()

    def tsp_util(curr):
        nonlocal total_bobot
        bobot_minimal = float('inf')
        next_node = None
        for neighbor in graph.neighbors(int_to_node(curr)):
            bobot = graph[int_to_node(curr)][neighbor]['weight']
            if not visited[node_to_int(neighbor)] and bobot < bobot_minimal:
                bobot_minimal = bobot
                next_node = neighbor
        if next_node is not None:
            jalur.append(next_node)
            visited[node_to_int(next_node)] = True
            total_bobot += bobot_minimal
            tsp_util(node_to_int(next_node))

    tsp_util(node_to_int(mulai))
    waktu_akhir = time.time()
    waktu_eksekusi = waktu_akhir - waktu_mulai
    return jalur, total_bobot, waktu_eksekusi

#Program Dijkstra
def dijkstra(graph, mulai, akhir):
    dist = {}
    prev = {}
    unvisited = set(graph.nodes())
    waktu_mulai = time.time()

    def node_to_int(node):
        return ord(node) - ord('A')

    def int_to_node(num):
        return chr(num + ord('A'))

    for node in graph.nodes():
        dist[node] = float('inf')
    dist[mulai] = 0

    while unvisited:
        min_dist = float('inf')
        curr = None
        for node in unvisited:
            if dist[node] < min_dist:
                min_dist = dist[node]
                curr = node
        unvisited.remove(curr)

        for neighbor in graph.neighbors(curr):
            bobot = graph[curr][neighbor]['weight']
            alt = dist[curr] + bobot
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = curr

    waktu_akhir = time.time()
    waktu_eksekusi = waktu_akhir - waktu_mulai
    jalur = []
    curr = akhir
    while curr != mulai:
        jalur.append(curr)
        curr = prev[curr]
    jalur.append(mulai)
    jalur.reverse()
    return jalur, dist[akhir], waktu_eksekusi

def iterasi(jalur):
    print("\nIterasi :")
    for i, node in enumerate(jalur):
        print(f"Iterasi ke-{i+1}: {node}")
    print()

def waktu_komputasi(waktu):
    print(f"Waktu Perhitungan : {waktu:.6f} detik")

def jalur_terpendek(jalur, bobot):
    print("Jalur Terpendek :")
    print(" -> ".join(jalur))
    print(f"Total Bobot : {bobot}")

def main():
    graph = nx.Graph()
    graph.add_edge('A', 'B', weight=12)
    graph.add_edge('A', 'C', weight=10)
    graph.add_edge('A', 'G', weight=12)
    graph.add_edge('B', 'A', weight=12)
    graph.add_edge('B', 'C', weight=8)
    graph.add_edge('B', 'D', weight=12)
    graph.add_edge('C', 'A', weight=10)
    graph.add_edge('C', 'B', weight=8)
    graph.add_edge('C', 'D', weight=11)
    graph.add_edge('C', 'E', weight=3)
    graph.add_edge('C', 'G', weight=9)
    graph.add_edge('D', 'C', weight=11)
    graph.add_edge('D', 'E', weight=11)
    graph.add_edge('D', 'F', weight=10)
    graph.add_edge('E', 'C', weight=3)
    graph.add_edge('E', 'D', weight=11)
    graph.add_edge('E', 'F', weight=6)
    graph.add_edge('E', 'G', weight=7)
    graph.add_edge('F', 'D', weight=10)
    graph.add_edge('F', 'E', weight=6)
    graph.add_edge('F', 'G', weight=9)
    graph.add_edge('G', 'A', weight=12)
    graph.add_edge('G', 'C', weight=9)
    graph.add_edge('G', 'E', weight=7)
    graph.add_edge('G', 'F', weight=9)

    print("===============================================================")
    print("    PROGRAM MENGHITUNG JALUR TERPENDEK DALAM SUATU GRAPH"
          "\n         MENGGUNAKAN ALGORITMA TSP ATAU DIJKSTRA")
    print("===============================================================")
    print("Jenis Algoritma Yang Tersedia : ")
    print("1. Algoritma TSP (Traveling Salesman Problem)")
    print("2. Algoritma Dijkstra")
    print("===============================================================")
    pilihan = int(input("Pilih perhitungan yang ingin dilakukan (1/2) : "))
    print("===============================================================")

    if pilihan == 1:
        node_awal = input("Pilih node Awal (Huruf pada Graph) : ")
        tsp_jalur, tsp_bobot, tsp_waktu = tsp(graph, node_awal)
        iterasi(tsp_jalur)
        waktu_komputasi(tsp_waktu)
        jalur_terpendek(tsp_jalur, tsp_bobot)
    elif pilihan == 2:
        node_awal = input("Pilih node Awal (Huruf pada Graph) : ")
        node_akhir = input("Pilih node Akhir (Huruf pada Graph) : ")
        dijkstra_jalur, dijkstra_bobot, dijkstra_waktu = dijkstra(graph, node_awal, node_akhir)
        iterasi(dijkstra_jalur)
        waktu_komputasi(dijkstra_waktu)
        jalur_terpendek(dijkstra_jalur, dijkstra_bobot)
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

    print("===============================================================")
    lanjut = input("Apakah Anda ingin melanjutkan perhitungan? (ya/tidak) : ")
    print("===============================================================")

    while lanjut.lower() == "ya":
        print("\nJenis Algoritma Yang Tersedia : ")
        print("1. Algoritma TSP (Traveling Salesman Problem)")
        print("2. Algoritma Dijkstra")
        print("===============================================================")
        pilihan = int(input("Pilih perhitungan yang ingin dilakukan (1/2) : "))

        if pilihan == 1:
            node_awal = input("Pilih node Awal (Huruf pada Graph) : ")
            tsp_jalur, tsp_bobot, tsp_waktu = tsp(graph, node_awal)
            iterasi(tsp_jalur)
            waktu_komputasi(tsp_waktu)
            jalur_terpendek(tsp_jalur, tsp_bobot)
        elif pilihan == 2:
            node_awal = input("Pilih node Awal (Huruf pada Graph) : ")
            node_akhir = input("Pilih node Akhir (Huruf pada Graph) : ")
            dijkstra_jalur, dijkstra_bobot, dijkstra_waktu = dijkstra(graph, node_awal, node_akhir)
            iterasi(dijkstra_jalur)
            waktu_komputasi(dijkstra_waktu)
            jalur_terpendek(dijkstra_jalur, dijkstra_bobot)
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

        print("===============================================================")
        lanjut = input("Apakah Anda ingin melanjutkan perhitungan? (ya/tidak) : ")
        print("===============================================================")

if __name__ == '__main__':
    main()