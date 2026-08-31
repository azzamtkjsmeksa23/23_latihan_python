gj = print()
def ganjil_genap(gj):
    while True:
        gj = int(input("Masukkan Angkah: "))
        if gj % 2 == 0:
            print("itu adalah angka genap")
        else:
            print("itu adalah angka ganjil")

        jalan = str(input('masih lanjyut? (y/n): '))
        if jalan == "y":
            continue
        elif jalan == "n":
            print("Terima Kasih💖!!")
            break
        else:
            print("kemu dek")
            continue

if __name__ == "__main__":
    ganjil_genap(gj)