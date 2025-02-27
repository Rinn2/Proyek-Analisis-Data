import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor

# Konfigurasi gaya Seaborn
sns.set_style("whitegrid")

# --- Tampilan Sidebar ---
st.sidebar.title("Agus Irvan Maulana")
st.sidebar.write("agusirvan2708@gmail.com")
st.sidebar.write("MC381D5Y1073")

# --- Judul Aplikasi ---
st.title("🚴 Analisis Peminjaman Sepeda")
st.markdown("---")

# --- Memuat Dataset ---
df = pd.read_csv("dashboard/main-data.csv")

# --- Filtering Data ---
st.sidebar.subheader("Filter Data")

# Dropdown filter untuk Season
season_filter = st.sidebar.selectbox(
    "Pilih Season:",
    ["Tampilkan Semua", 1, 2, 3, 4],
    format_func=lambda x: "Tampilkan Semua" if x == "Tampilkan Semua" else {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}[x]
)

# Filter dataset
filtered_df = df.copy()
if season_filter != "Tampilkan Semua":
    filtered_df = filtered_df[filtered_df['season'] == season_filter]

# Menampilkan beberapa baris pertama dataset yang telah difilter
st.subheader("📌 Data Peminjaman Sepeda")
st.dataframe(filtered_df.head())

# --- Analisis Tren Bulanan ---
st.subheader(f"📊 Tren Peminjaman Sepeda per Bulan {'(Musim ' + {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}.get(season_filter, '') + ')' if season_filter != 'Tampilkan Semua' else ''}")

# Mengelompokkan data berdasarkan bulan
monthly_trend = filtered_df.groupby('mnth')['cnt'].sum().reset_index()
monthly_trend['change'] = monthly_trend['cnt'].diff()

# Hapus baris dengan nilai NaN di kolom 'change'
monthly_trend = monthly_trend.dropna(subset=['change'])

# Cek apakah ada data yang tersisa setelah menghapus NaN
if not monthly_trend.empty:
    month_with_biggest_drop = monthly_trend.loc[monthly_trend['change'].idxmin(), 'mnth']
else:
    month_with_biggest_drop = "Tidak ada data yang tersedia"

# Membuat plot tren peminjaman
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=monthly_trend, x='mnth', y='cnt', marker='o', linewidth=2.5, label='Total Peminjaman', ax=ax, color='royalblue')

# Tambahkan garis vertikal hanya jika ada data yang tersedia
if not monthly_trend.empty:
    ax.axvline(
        x=month_with_biggest_drop,
        color='red',
        linestyle='--',
        label=f'Penurunan Terbesar (Bulan {month_with_biggest_drop})'
    )

ax.set_xticks(range(1, 13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'])
ax.set_xlabel('Bulan')
ax.set_ylabel('Total Peminjaman')
ax.set_title('📉 Tren Peminjaman Sepeda per Bulan', fontsize=14)
ax.legend()
ax.grid(alpha=0.3)
st.pyplot(fig)

# --- Analisis Feature Importance ---
st.subheader("🔍 Faktor yang Mempengaruhi Peminjaman")

# Memilih fitur yang relevan
features = ['weathersit', 'temp', 'hum', 'windspeed', 'holiday', 'workingday']
X = filtered_df[features]
y = filtered_df['cnt']

# Melatih model RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)
feature_importance = model.feature_importances_

# Membuat DataFrame untuk menampilkan hasil
importance_df = pd.DataFrame({'Feature': features, 'Importance': feature_importance})
importance_df = importance_df.sort_values(by='Importance', ascending=False)

# Membuat plot feature importance
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=importance_df, x='Importance', y='Feature', palette='Blues_r', ax=ax)
for index, value in enumerate(importance_df['Importance']):
    ax.text(value - 0.02, index, f'{value:.3f}', va='center', fontsize=10, fontweight='bold')
ax.set_xlabel('Tingkat Pengaruh')
ax.set_ylabel('Faktor')
ax.set_title('📊 Feature Importance - Faktor yang Mempengaruhi Peminjaman')
ax.grid(axis='x', linestyle='--', alpha=0.5)
st.pyplot(fig)

# --- Kesimpulan ---
st.markdown("---")
st.subheader("📌 Kesimpulan")
st.info(
    "- Bulan dengan penurunan peminjaman terbesar: **{}**.\n"
    "- Faktor paling berpengaruh terhadap jumlah peminjaman: **{}**."
    .format(month_with_biggest_drop, importance_df.iloc[0, 0])
)

st.markdown("---")
st.write("🚀 Dibuat dengan Streamlit | Data: Bike Sharing Dataset")
