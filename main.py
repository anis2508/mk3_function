print("Selamat Datang Ke Zoo Putra")
print("Sistem pembelian tiket Zoo Putra")

print("Tiket Kanak-Kanak(12 tahun kebawah) - Rm 7")
print("Tiket Dewasa(12 tahun ke atas)      - Rm 14")
print("Tiket Wargaemas(60tahun keatas)     - Rm 10")

print()

print("Sila masukkan bilangan tiket mengikut kategori yang disediakan")
dewasa = int(input("Bilangan dewasa      : "))
kanakkanak = int(input("Bilangan kanak-kanak : "))
wargaemas = int(input("Bilangan Warga emas  : "))

bayaran = int(input("Masukkan nilai bayaran tiket RM"))

def hargakk(hrgkanakk):
    total1 = hrgkanakk * 7
    return total1

def hargad(hrgdewasa):
    total2 = hrgdewasa * 14
    return total2

def hargaw(hrgwargaemas):
    total3 = hrgwargaemas * 10
    return total3

print()

hKanak = hargakk(kanakkanak)

hDewasa = hargad(dewasa)

hWargaemas = hargaw(wargaemas)

def total(pkanak, pdewasa, pwargaemas):
    jumlah = pkanak + pdewasa + pwargaemas
    return jumlah

totalAll = total(hKanak, hDewasa, hWargaemas)
print("Jumlah kesemua tiket adalah RM ", totalAll)

baki = bayaran - totalAll
print("Baki duit anda adalah RM", baki)
