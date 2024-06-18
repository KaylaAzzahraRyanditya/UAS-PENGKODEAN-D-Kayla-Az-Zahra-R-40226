import pandas as pd
import matplotlib.pyplot as plt

# Data input
data = {
    "Marketing_ID": [201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215],
    "Tanggal": ["01/01/2023", "02/01/2023", "03/01/2023", "04/01/2023", "05/01/2023", "06/01/2023", "07/01/2023", "08/01/2023", "09/01/2023", "10/01/2023", "11/01/2023", "12/01/2023", "13/01/2023", "14/01/2023", "15/01/2023"],
    "Kampanye": ["Kampanye_A", "Kampanye_B", "Kampanye_C", "Kampanye_D", "Kampanye_E", "Kampanye_F", "Kampanye_G", "Kampanye_H", "Kampanye_I", "Kampanye_J", "Kampanye_K", "Kampanye_L", "Kampanye_M", "Kampanye_N", "Kampanye_O"],
    "Biaya": [50000, 40000, 60000, 30000, 20000, 70000, 50000, 40000, 60000, 30000, 20000, 70000, 50000, 40000, 60000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(12, 8))
plt.bar(df['Kampanye'], df['Biaya'], color='b')
plt.title('Biaya Marketing per Kampanye')
plt.xlabel('Kampanye')
plt.ylabel('Biaya')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
