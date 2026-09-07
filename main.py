import ganjilgenap as gg
import modul_matematika as mm
import modul_BangunRuang as Mb
import autentikasi as aut

while not aut.login():
    print('Login dulu Dek 😂😝')
    print(aut.main_menu())

print("\nPilih rumus matematika\n1. ganjil genap\n2. Bilangan prima\n3. tambah kali kurang bagi\n4. Keliling Persegi\n5. Luas Segitiga\n6. Keluar")

while True:
    maumana = input("mau yang mana: ")
    if maumana == '1':
        gj = print()
        gg.ganjil_genap(gj)
    elif maumana == '2':
        ya = int(input("masukkan angka: "))
        mm.bilangan_prima(ya)
    elif maumana == '3':
        tak = int(input('masukkan angka 1: '))
        kul = int(input('masukkan angka 2: '))
        mm.tamkuli(tak, kul)
    elif maumana == '4':
        s = int(input("Masukkan Angkah: "))
        Mb.keliling_persegi(s)
    elif maumana == '5':
        a = float(input('Masukkan Alas Segitiga: '))
        t = float(input('Masukkan Tinggi Segitiga: '))
        Mb.luas_segitiga(a, t)
    elif maumana == '6':
        print('Terima Kasih 💖')
        break