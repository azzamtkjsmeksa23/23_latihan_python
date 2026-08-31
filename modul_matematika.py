def ganjil_genap(ti):
    if ti % 2 == 0:
        print("Angka Genap")
    else:
        print("Angka Ganjil")

def bilangan_prima(ya):
    if ya < 2:
        print("Bukan Prima")
    else:
        print("Prima")

def tamkuli(tak, kul):
    tambah = tak + kul
    kurang = tak - kul
    kali = tak * kul
    bagi = tak / kul

    print("tambah: ", tambah)
    print("kurang: ", kurang)
    print("kali: ", kali)
    print("bagi: ", bagi)