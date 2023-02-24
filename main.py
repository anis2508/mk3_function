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

if kanakkanak > 1:
    hKanak = hargakk(kanakkanak)
    print(f"Jumlah harga untuk {kanakkanak} tiket kanak-kanak adalah RM{hKanak}")
else:
    hKanak = 7
    print(f"Jumlah harga untuk {kanakkanak} tiket kanak-kanak adalah RM{hKanak}")

if dewasa > 1:
    hDewasa = hargad(dewasa)
    print(f"Jumlah harga untuk {dewasa} tiket dewasa adalah RM{hDewasa}")
else:
    hDewasa = 14
    print(f"Jumlah harga untuk {dewasa} tiket dewasa adalah RM{hDewasa}")

if wargaemas > 1:
    hWargaemas = hargaw(wargaemas)
    print(f"Jumlah harga untuk {wargaemas} tiket dewasa adalah RM{hWargaemas}")
else:
    hWargaemas = 10
    print(f"Jumlah harga untuk {wargaemas} tiket dewasa adalah RM{hWargaemas}")

def total(pkanak, pdewasa, pwargaemas):
    jumlah = pkanak + pdewasa + pwargaemas
    return jumlah

totalAll = total(hKanak, hDewasa, hWargaemas)
print("Jumlah kesemua tiket adalah RM ", totalAll)

print()

i = 2

while i > 1:
    bayaran = int(input("Masukkan nilai bayaran tiket RM"))
    if bayaran < totalAll:
        print("Bayaran tiket anda tidak mencukupi dengan harga tiket yang anda beli")
        continue
    else:
        baki = bayaran - totalAll
        print("Anda sudah membuat pembayaran")
        print("Baki duit anda adalah RM", baki)
        break