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
    filtered_df = filtered_df[filtered_df['season_x'] == season_filter]

# Menampilkan beberapa baris pertama dataset yang telah difilter
st.subheader("📌 Data Peminjaman Sepeda")
st.dataframe(filtered_df.head())

# --- Analisis Tren Bulanan ---
st.subheader(f"📊 Tren Peminjaman Sepeda per Bulan {'(Musim ' + {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}.get(season_filter, '') + ')' if season_filter != 'Tampilkan Semua' else ''}")

# Mengelompokkan data berdasarkan bulan
monthly_trend = filtered_df.groupby('mnth_x')['cnt_x'].sum().reset_index()
monthly_trend['change'] = monthly_trend['cnt_x'].diff()

# Hapus baris dengan nilai NaN di kolom 'change'
monthly_trend = monthly_trend.dropna(subset=['change'])

# Cek apakah ada data yang tersisa setelah menghapus NaN
if not monthly_trend.empty:
    month_with_biggest_drop = monthly_trend.loc[monthly_trend['change'].idxmin(), 'mnth_x']
else:
    month_with_biggest_drop = "Tidak ada data yang tersedia"

# Membuat plot tren peminjaman
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=monthly_trend, x='mnth_x', y='cnt_x', marker='o', linewidth=2.5, label='Total Peminjaman', ax=ax, color='royalblue')

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

# --- Perbandingan Penyewa Sepeda antara Hari Kerja dan Hari Libur ---
st.subheader("📊 Perbandingan Penyewa Sepeda: Hari Kerja vs Hari Libur")

# Menghitung rata-rata jumlah peminjaman sepeda berdasarkan hari kerja/libur
avg_rentals = filtered_df.groupby("workingday_x")["cnt_x"].mean().reset_index()

# Membuat plot lebih menarik
fig, ax = plt.subplots(figsize=(7, 5))
colors = sns.color_palette("coolwarm", n_colors=2)

sns.barplot(x="workingday_x", y="cnt_x", data=avg_rentals, palette=colors, ax=ax)

# Menambahkan label pada batang
for p in ax.patches:
    ax.annotate(f'{p.get_height():.0f}', 
                (p.get_x() + p.get_width() / 2, p.get_height()), 
                ha='center', va='bottom', fontsize=12, fontweight='bold')

# Mengatur sumbu dan judul
ax.set_xticks([0, 1])
ax.set_xticklabels(["Hari Libur", "Hari Kerja"], fontsize=12)
ax.set_xlabel("Hari", fontsize=13, fontweight="bold")
ax.set_ylabel("Rata-rata Jumlah Penyewa Sepeda", fontsize=13, fontweight="bold")
ax.set_title("Perbandingan Penyewa Sepeda antara Hari Kerja dan Hari Libur", fontsize=14, fontweight="bold")

st.pyplot(fig)
