"""Tugas Struktur Data Python: string, list, set, tuple, dictionary."""
import os
import re


# ---------------------------------------------------------------- SOAL 1
def soal1():
    print("\n=== SOAL 1: Analisis Kalimat ===")
    kalimat = input("Masukkan sebuah kalimat: ").strip()
    kata_list = kalimat.split()

    if not kata_list:
        print("Kalimat kosong.")
        return

    # (a) jumlah kata
    print(f"(a) Jumlah kata            : {len(kata_list)}")

    # (b) jumlah karakter
    print(f"(b) Jumlah karakter        : {len(kalimat)} (dengan spasi), "
          f"{len(kalimat.replace(' ', ''))} (tanpa spasi)")

    # (c) kata terpanjang (tanda baca diabaikan)
    bersih = [k.strip(".,!?;:\"'()[]{}") for k in kata_list]
    terpanjang = max(bersih, key=len)
    print(f"(c) Kata terpanjang        : {terpanjang} ({len(terpanjang)} huruf)")

    # (d) title case
    title = " ".join(k.capitalize() for k in kata_list)
    print(f"(d) Title case             : {title}")


# ---------------------------------------------------------------- SOAL 2
def kategori_nilai(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 55:
        return "C"
    elif nilai >= 40:
        return "D"
    return "E"


def soal2():
    print("\n=== SOAL 2: Analisis Nilai Mahasiswa ===")
    teks = input("Masukkan nilai (pisahkan dengan spasi): ").split()
    try:
        nilai = [float(n) for n in teks]
    except ValueError:
        print("Input tidak valid, hanya angka yang diperbolehkan.")
        return
    if not nilai:
        print("Tidak ada nilai yang dimasukkan.")
        return

    # (a) rata-rata
    print(f"(a) Rata-rata              : {sum(nilai) / len(nilai):.2f}")

    # (b) tertinggi & terendah
    print(f"(b) Nilai tertinggi        : {max(nilai)}")
    print(f"    Nilai terendah         : {min(nilai)}")

    # (c) pengelompokan kategori
    kategori = [(n, kategori_nilai(n)) for n in nilai]
    print("(c) Kategori tiap nilai    :")
    for n, k in kategori:
        print(f"      {n:>6} -> {k}")

    # (d) frekuensi kategori (dictionary)
    frekuensi = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    for _, k in kategori:
        frekuensi[k] += 1
    print(f"(d) Frekuensi kategori     : {frekuensi}")


# ---------------------------------------------------------------- SOAL 3
def soal3():
    print("\n=== SOAL 3: Operasi Set Beasiswa ===")
    beasiswa_a = [101, 102, 103, 104, 105, 106]
    beasiswa_b = [104, 105, 106, 107, 108, 109, 105]  # ada duplikat sengaja

    a, b = set(beasiswa_a), set(beasiswa_b)
    print(f"Penerima beasiswa A: {sorted(a)}")
    print(f"Penerima beasiswa B: {sorted(b)}")

    print(f"(a) Menerima keduanya      : {sorted(a & b)}")   # intersection
    print(f"(b) Hanya beasiswa A       : {sorted(a - b)}")   # difference
    print(f"(c) Beasiswa B tapi bukan A: {sorted(b - a)}")   # difference
    print(f"(d) Semua mahasiswa unik   : {sorted(a | b)}")   # union


# ---------------------------------------------------------------- SOAL 4
inventaris = {
    "Pensil": (2500, 100),
    "Buku Tulis": (7000, 50),
    "Penghapus": (1500, 80),
}


def tambah_barang(nama, harga, stok):
    """(a) Menambah barang baru."""
    if nama in inventaris:
        print(f"'{nama}' sudah ada. Gunakan update_stok().")
        return
    inventaris[nama] = (harga, stok)
    print(f"Barang '{nama}' ditambahkan.")


def update_stok(nama, stok_baru):
    """(b) Mengupdate stok barang (tuple immutable, jadi dibuat ulang)."""
    if nama not in inventaris:
        print(f"'{nama}' tidak ditemukan.")
        return
    harga, _ = inventaris[nama]
    inventaris[nama] = (harga, stok_baru)
    print(f"Stok '{nama}' diubah menjadi {stok_baru}.")


def cari_harga(harga_min, harga_maks):
    """(c) Mencari barang dengan harga dalam rentang tertentu."""
    return {nama: (h, s) for nama, (h, s) in inventaris.items()
            if harga_min <= h <= harga_maks}


def total_nilai():
    """(d) Total nilai inventaris = jumlah(harga x stok)."""
    return sum(h * s for h, s in inventaris.values())


def soal4():
    print("\n=== SOAL 4: Inventaris Toko ===")
    print("Inventaris awal:", inventaris)

    tambah_barang("Penggaris", 3000, 40)
    update_stok("Pensil", 120)

    hasil = cari_harga(2000, 5000)
    print("Barang harga Rp2.000 - Rp5.000:", hasil)

    print(f"Total nilai inventaris: Rp{total_nilai():,}".replace(",", "."))


# ---------------------------------------------------------------- SOAL 5
CONTOH_TEKS = (
    "Belajar python itu menyenangkan. Python adalah bahasa yang mudah dipelajari. "
    "Dengan python kita dapat membuat program yang berguna dan program yang menarik."
)


def soal5():
    print("\n=== SOAL 5: Analisis Teks dari File ===")
    path = input("Nama file teks (Enter untuk 'teks.txt'): ").strip() or "teks.txt"

    if not os.path.exists(path):
        print(f"File '{path}' tidak ditemukan, membuat file contoh...")
        with open(path, "w", encoding="utf-8") as f:
            f.write(CONTOH_TEKS)

    with open(path, "r", encoding="utf-8") as f:
        teks = f.read().lower()                       # string

    kata_list = re.findall(r"[a-zA-Z']+", teks)       # list
    if not kata_list:
        print("File tidak berisi kata.")
        return

    # (a) frekuensi kata (dictionary)
    frekuensi = {}
    for kata in kata_list:
        frekuensi[kata] = frekuensi.get(kata, 0) + 1
    print(f"(a) Frekuensi kata         : {frekuensi}")

    # (b) 10 kata paling sering (urut frekuensi turun, lalu alfabet)
    top10 = sorted(frekuensi.items(), key=lambda x: (-x[1], x[0]))[:10]
    print("(b) 10 kata terbanyak      :")
    for i, (kata, f) in enumerate(top10, 1):
        print(f"      {i:>2}. {kata:<15} {f}")

    # (c) hapax legomena (set)
    hapax = {kata for kata, f in frekuensi.items() if f == 1}
    print(f"(c) Hapax legomena ({len(hapax)})  : {sorted(hapax)}")

    # (d) type-token ratio
    ttr = len(set(kata_list)) / len(kata_list)
    print(f"(d) Type-token ratio       : {len(set(kata_list))}/{len(kata_list)} = {ttr:.4f}")


# ---------------------------------------------------------------- MENU
def main():
    menu = {"1": soal1, "2": soal2, "3": soal3, "4": soal4, "5": soal5}
    while True:
        print("\n===== MENU =====")
        print("1. Analisis kalimat")
        print("2. Analisis nilai mahasiswa")
        print("3. Operasi set beasiswa")
        print("4. Inventaris toko")
        print("5. Analisis teks dari file")
        print("0. Keluar")
        pilihan = input("Pilih soal: ").strip()
        if pilihan == "0":
            break
        menu.get(pilihan, lambda: print("Pilihan tidak valid."))()


if __name__ == "__main__":
    main()
