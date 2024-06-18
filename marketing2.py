import pandas as pd
import matplotlib.pyplot as plt

# Data input for marketing
marketing_data = {
    "Marketing_ID": [201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215],
    "Tanggal": ["01/01/2023", "02/01/2023", "03/01/2023", "04/01/2023", "05/01/2023", "06/01/2023", "07/01/2023", "08/01/2023", "09/01/2023", "10/01/2023", "11/01/2023", "12/01/2023", "13/01/2023", "14/01/2023", "15/01/2023"],
    "Kampanye": ["Kampanye_A", "Kampanye_B", "Kampanye_C", "Kampanye_D", "Kampanye_E", "Kampanye_F", "Kampanye_G", "Kampanye_H", "Kampanye_I", "Kampanye_J", "Kampanye_K", "Kampanye_L", "Kampanye_M", "Kampanye_N", "Kampanye_O"],
    "Biaya": [50000, 40000, 60000, 30000, 20000, 70000, 50000, 40000, 60000, 30000, 20000, 70000, 50000, 40000, 60000]
}

# Data input for sales
sales_data = {
    "Detail_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    "Transaksi_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],
    "Produk_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    "Jumlah_Terjual": [10, 5, 20, 10, 25, 15, 8, 5, 10, 4, 6, 3, 9, 7, 12]
}

# Create DataFrame
df_marketing = pd.DataFrame(marketing_data)
df_sales = pd.DataFrame(sales_data)

# Convert 'Tanggal' to datetime format in marketing data
df_marketing['Tanggal'] = pd.to_datetime(df_marketing['Tanggal'], format='%d/%m/%Y')

# Sum up sales grouped by day (assuming each Detail_ID corresponds to a date in marketing data)
# For simplicity, let's assume the Tanggal matches with the Transaksi_ID sequence directly
df_sales['Tanggal'] = df_marketing['Tanggal']

# Group sales by date and sum up the Jumlah_Terjual
df_sales_grouped = df_sales.groupby('Tanggal')['Jumlah_Terjual'].sum().reset_index()

# Merge marketing and sales data on 'Tanggal'
df_merged = pd.merge(df_marketing, df_sales_grouped, on='Tanggal')

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 6))

color = 'tab:blue'
ax1.set_xlabel('Tanggal')
ax1.set_ylabel('Biaya Marketing', color=color)
ax1.plot(df_merged['Tanggal'], df_merged['Biaya'], marker='o', linestyle='-', color=color, label='Biaya Marketing')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:green'
ax2.set_ylabel('Jumlah Terjual', color=color)
ax2.plot(df_merged['Tanggal'], df_merged['Jumlah_Terjual'], marker='o', linestyle='--', color=color, label='Jumlah Terjual')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title('Pengaruh Biaya Marketing terhadap Penjualan Produk')
plt.show()
