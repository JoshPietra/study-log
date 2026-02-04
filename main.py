catatan = []
favorit = []

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

def menu_favorit():
    print("\n=== Menu Mapel Favorit ===")
    print("1. Tambah mapel favorit")
    print("2. Lihat mapel favorit")
    print("3. Kembali ke menu utama")

def tambah_favorit():
    mapel = input("Masukkan nama mapel yang ingin ditambahkan ke favorit: ")
    if mapel not in favorit:
        favorit.append(mapel)
        print(f"Mapel '{mapel}' berhasil ditambahkan ke favorit!")
    else:
        print(f"Mapel '{mapel}' sudah ada di favorit.")

def lihat_favorit():
    if not favorit:
        print("Belum ada mapel favorit.")
    else:
        print("\n=== Daftar Mapel Favorit ===")
        for i, mapel in enumerate(favorit, start=1):
            print(f"{i}. {mapel}")
        print()

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Mapel Favorit")
    print("5. Keluar")

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
        while True:
            menu_favorit()
            sub_pilihan = input("Pilih submenu: ")
            if sub_pilihan == "1":
                tambah_favorit()
            elif sub_pilihan == "2":
                lihat_favorit()
            elif sub_pilihan == "3":
                break
            else:
                print("Pilihan tidak valid")
    elif pilihan == "5":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")