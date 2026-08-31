import ganjilgenap as gg
import modul_matematika as mm

print("1. ganjil genap\n2. Bilangan prima\n3. tambah kali kurang bagi")

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