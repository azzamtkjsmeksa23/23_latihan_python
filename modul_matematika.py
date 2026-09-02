def ganjil_genap(ti):
    if ti % 2 == 0:
        print("Angka Genap")
    else:
        print("Angka Ganjil")

def bilangan_prima(ya):
    if ya < 2:
        print(ya, "Bukan Prima")
        return False
    for i in range(2, int(ya**0.5) + 1):
        if ya % i == 0:
            print(ya, "bukan bilangan prima")
            return False
    print(ya, "adalah bilangan prima")
    return True

def tamkuli(tak, kul):
    tambah = tak + kul
    kurang = tak - kul
    kali = tak * kul
    bagi = tak / kul

    print("tambah: ", tambah)
    print("kurang: ", kurang)
    print("kali: ", kali)
    print("bagi: ", bagi)