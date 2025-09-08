import os
import json
from api_client import get_all_products
from utils.writer import save_to_json

def analisis_per_kategori(produk):
    kategori = {}
    for item in produk:
        cat = item['category']
        kategori[cat] = kategori.get(cat, 0) + 1
    return kategori

def total_nilai_inventaris(produk):
    return sum(item['price'] for item in produk)

def produk_ekstrim_per_kategori(produk):
    ekstrim = {}
    for item in produk:
        cat = item['category']
        if cat not in ekstrim:
            ekstrim[cat] = {'termurah': item, 'termahal': item}
        else:
            if item['price'] < ekstrim[cat]['termurah']['price']:
                ekstrim[cat]['termurah'] = item
            if item['price'] > ekstrim[cat]['termahal']['price']:
                ekstrim[cat]['termahal'] = item
    return ekstrim

def tampilkan_analisis(produk):
    print(f"\nJumlah total produk: {len(produk)}")

    print("\n📊 Jumlah produk per kategori:")
    per_kat = analisis_per_kategori(produk)
    for k, v in per_kat.items():
        print(f"- {k}: {v} produk")

    total = total_nilai_inventaris(produk)
    print(f"\n💰 Total nilai inventaris: ${total:,.2f}")

    ekstrim = produk_ekstrim_per_kategori(produk)
    print("\n📉📈 Produk termurah & termahal per kategori:")
    for k, data in ekstrim.items():
        print(f"\n📂 Kategori: {k}")
        print(f"  ▸ Termurah:  {data['termurah']['title']} (${data['termurah']['price']})")
        print(f"  ▸ Termahal:  {data['termahal']['title']} (${data['termahal']['price']})")

def load_from_file(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Gagal membaca file: {e}")
        return []

if __name__ == "__main__":
    print("Pilih sumber data:")
    print("1. Ambil dari API")
    print("2. Baca dari file data/produk.json")
    mode = input("Ketik 1 atau 2: ")

    produk = []

    if mode == "1":
        print("\n🔄 Mengambil data dari API...")
        produk = get_all_products()
        if produk:
            save_to_json(produk, "produk.json")
    elif mode == "2":
        print("\n📂 Membaca data dari file...")
        produk = load_from_file("data/produk.json")
    else:
        print("❌ Pilihan tidak valid. Program dihentikan.")
        exit()

    if produk:
        tampilkan_analisis(produk)
    else:
        print("❌ Tidak ada data untuk dianalisis.")
