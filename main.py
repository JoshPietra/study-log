catatan = []

def tambah_catatan():
    mapel = input("Masukkan nama mapel: ")
    topik = input("Masukkan topik yang dipelajari: ")
    durasi = int(input("Masukkan durasi belajar (dalam menit): "))
    
    # Membuat dictionary untuk catatan baru
    catatan_baru = {
        'mapel': mapel,
        'topik': topik,
        'durasi': durasi
    }
    
    # Menambahkan ke list catatan
    catatan.append(catatan_baru)
    print("Catatan berhasil ditambahkan!")

def lihat_catatan():
    if not catatan:
        print("Belum ada catatan belajar.")
    else:
        print("\n=== Daftar Catatan Belajar ===")
        for i, item in enumerate(catatan, start=1):
            print(f"{i}. Mapel: {item['mapel']}, Topik: {item['topik']}, Durasi: {item['durasi']} menit")
        print()

def total_waktu():
    total = sum(item['durasi'] for item in catatan)
    print(f"Total waktu belajar: {total} menit")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")