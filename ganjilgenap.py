def ganjil_genap(x):
    while True:
        x = int(input("Masukkan angkah: "))
        if x % 2 == 0:
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