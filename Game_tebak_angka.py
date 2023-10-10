import random

def main():
    print("Selamat datang di Permainan Tebak Angka!")
    print("Saya akan memilih sebuah angka acak antara 1 dan 15.")
    target = random.randint(1, 100)
    
    tebakan = None
    jumlah_tebakan = 0

    while tebakan != target:
        try:
            tebakan = int(input("Tebak angka (1-15): "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        jumlah_tebakan += 1

        if tebakan < target:
            print("Tebakan terlalu rendah. Coba lagi.")
        elif tebakan > target:
            print("Tebakan terlalu tinggi. Coba lagi.")
        else:
            print(f"Selamat! Anda berhasil menebak angka {target} dalam {jumlah_tebakan} tebakan.")

    if jumlah_tebakan == 1:
        print("Anda adalah seorang jenius! Anda menebak angka dengan satu tebakan.")
    else:
        print("Terima kasih telah bermain!")

if __name__ == "__main__":
    main()