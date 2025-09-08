# import json

# def analisis_per_kategori(produk):
#     kategori = {}
#     for item in produk:
#         cat = item['category']
#         kategori[cat] = kategori.get(cat, 0) + 1
#     return kategori

# def total_nilai_inventaris(produk):
#     total = sum(item['price'] for item in produk)
#     return total

# def produk_ekstrim_per_kategori(produk):
#     ekstrim = {}
#     for item in produk:
#         cat = item['category']
#         if cat not in ekstrim:
#             ekstrim[cat] = {
#                 'termurah': item,
#                 'termahal': item
#             }
#         else:
#             if item['price'] < ekstrim[cat]['termurah']['price']:
#                 ekstrim[cat]['termurah'] = item
#             if item['price'] > ekstrim[cat]['termahal']['price']:
#                 ekstrim[cat]['termahal'] = item
#     return ekstrim

# def tampilkan_analisis(produk):
#     print(f"Jumlah total produk: {len(produk)}")

#     print("\n📊 Jumlah produk per kategori:")
#     per_kat = analisis_per_kategori(produk)
#     for k, v in per_kat.items():
#         print(f"- {k}: {v} produk")

#     total = total_nilai_inventaris(produk)
#     print(f"\n💰 Total nilai inventaris: ${total:,.2f}")

#     ekstrim = produk_ekstrim_per_kategori(produk)
#     print("\n📉📈 Produk termurah & termahal per kategori:")
#     for k, data in ekstrim.items():
#         print(f"\n📂 Kategori: {k}")
#         print(f"  ▸ Termurah:  {data['termurah']['title']} (${data['termurah']['price']})")
#         print(f"  ▸ Termahal:  {data['termahal']['title']} (${data['termahal']['price']})")

# def analisis_dari_file(filepath):
#     try:
#         with open(filepath, "r") as f:
#             produk = json.load(f)

#         tampilkan_analisis(produk)

#     except FileNotFoundError:
#         print("❌ File tidak ditemukan. Pastikan 'data/produk.json' ada.")
#     except json.JSONDecodeError:
#         print("❌ Gagal membaca file JSON. Formatnya mungkin salah.")

# if __name__ == "__main__":
#     analisis_dari_file("data/produk.json")
