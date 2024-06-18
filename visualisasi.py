import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Data Tabel Produk
data_produk = {
    'Produk_ID': range(1, 16),
    'Nama_Produk': ['Produk_A', 'Produk_B', 'Produk_C', 'Produk_D', 'Produk_E', 'Produk_F', 'Produk_G', 'Produk_H', 'Produk_I', 'Produk_J', 'Produk_K', 'Produk_L', 'Produk_M', 'Produk_N', 'Produk_O'],
    'Harga_Satuan': [20000, 15000, 10000, 25000, 22000, 17000, 12000, 27000, 21000, 16000, 11000, 26000, 23000, 18000, 13000],
    'Kategori': ['Elektronik', 'Fashion', 'Gadget', 'Makanan', 'Elektronik', 'Fashion', 'Gadget', 'Makanan', 'Elektronik', 'Fashion', 'Gadget', 'Makanan', 'Elektronik', 'Fashion', 'Gadget']
}
df_produk = pd.DataFrame(data_produk)

# Data Tabel Transaksi
data_transaksi = {
    'Transaksi_ID': range(101, 116),
    'Tanggal': pd.date_range(start='2023-01-01', periods=15, freq='D'),
    'Pelanggan_ID': range(1001, 1016),
    'Total_Harga': [500000, 300000, 700000, 200000, 100000, 600000, 400000, 500000, 300000, 700000, 200000, 100000, 600000, 400000, 500000]
}
df_transaksi = pd.DataFrame(data_transaksi)

# Data Tabel Detail Transaksi
data_detail_transaksi = {
    'Detail_ID': range(1, 16),
    'Transaksi_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],
    'Produk_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    'Jumlah_Terjual': [10, 5, 20, 10, 25, 15, 8, 5, 10, 4, 6, 3, 9, 7, 12]
}
df_detail_transaksi = pd.DataFrame(data_detail_transaksi)

# Data Tabel Biaya Marketing
data_biaya_marketing = {
    'Marketing_ID': range(201, 216),
    'Tanggal': pd.date_range(start='2023-01-01', periods=15, freq='D'),
    'Kampanye': ['Kampanye_A', 'Kampanye_B', 'Kampanye_C', 'Kampanye_D', 'Kampanye_E', 'Kampanye_F', 'Kampanye_G', 'Kampanye_H', 'Kampanye_I', 'Kampanye_J', 'Kampanye_K', 'Kampanye_L', 'Kampanye_M', 'Kampanye_N', 'Kampanye_O'],
    'Biaya': [50000, 40000, 60000, 30000, 20000, 70000, 50000, 40000, 60000, 30000, 20000, 70000, 50000, 40000, 60000]
}
df_biaya_marketing = pd.DataFrame(data_biaya_marketing)

# Menggabungkan Tabel Transaksi dengan Detail Transaksi
df_transaksi_detail = pd.merge(df_detail_transaksi, df_transaksi, on='Transaksi_ID')

# Menggabungkan dengan Tabel Produk
df_merged = pd.merge(df_transaksi_detail, df_produk, on='Produk_ID')

# Menggabungkan dengan Tabel Biaya Marketing
df_final = pd.merge(df_merged, df_biaya_marketing, on='Tanggal')

# Menampilkan DataFrame Gabungan
print("DataFrame Gabungan:")
print(df_final)

# Visualisasi Total Penjualan per Produk (Histogram)
plt.figure(figsize=(10, 6))
df_final['Harga_Satuan'].plot(kind='hist', bins=15, color='skyblue', edgecolor='black')
plt.title('Distribusi Harga Satuan')
plt.xlabel('Harga Satuan (Rp)')
plt.ylabel('Frekuensi')
plt.grid(True)
plt.show()

# Visualisasi Jumlah Terjual vs. Total Harga (Scatter Plot)
plt.figure(figsize=(10, 6))
plt.scatter(df_final['Jumlah_Terjual'], df_final['Total_Harga'], color='purple')
plt.title('Scatter Plot Jumlah Terjual vs. Total Harga')
plt.xlabel('Jumlah Terjual')
plt.ylabel('Total Harga (Rp)')
plt.grid(True)
plt.show()

# Visualisasi Total Penjualan per Produk (Grafik Batang)
total_penjualan_per_produk = df_final.groupby('Nama_Produk')['Total_Harga'].sum()
plt.figure(figsize=(10, 6))
total_penjualan_per_produk.plot(kind='bar', color='orange')
plt.title('Total Penjualan per Produk')
plt.xlabel('Produk')
plt.ylabel('Total Penjualan (Rp)')
plt.grid(True)
plt.show()

# Visualisasi Pendapatan Harian (Grafik Garis)
pendapatan_harian = df_final.groupby('Tanggal')['Total_Harga'].sum()
plt.figure(figsize=(10, 6))
pendapatan_harian.plot(kind='line', color='green', marker='o')
plt.title('Pendapatan Harian')
plt.xlabel('Tanggal')
plt.ylabel('Total Pendapatan (Rp)')
plt.grid(True)
plt.show()

# Visualisasi Diagram Venn
set_a = set(df_final['Produk_ID'].unique())
set_b = set(df_final['Pelanggan_ID'].unique())
plt.figure(figsize=(10, 6))
venn2([set_a, set_b], ('Produk ID', 'Pelanggan ID'))
plt.title('Diagram Venn Produk ID dan Pelanggan ID')
plt.show()
