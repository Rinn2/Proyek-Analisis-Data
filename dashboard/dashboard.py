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
st.sidebar.write("agusirvan2708@gmail.com.")
st.sidebar.write("MC381D5Y1073.")

# --- Judul Aplikasi ---
st.title("🚴 Analisis Peminjaman Sepeda")
st.markdown("---")

# --- Memuat Dataset ---
df = pd.read_csv("dashboard/main-data.csv")

# --- Filter berdasarkan Musim ---
st.sidebar.subheader("Filter Data")
season_mapping = {1: "Musim Semi", 2: "Musim Panas", 3: "Musim Gugur", 4: "Musim Dingin"}
selected_season = st.sidebar.selectbox("Pilih Musim", list(season_mapping.values()))

# Mapping pilihan musim ke angka yang sesuai
df_filtered = df[df['season'] == list(season_mapping.keys())[list(season_mapping.values()).index(selected_season)]]

# Menampilkan beberapa baris pertama dataset
st.subheader("📌 Data Peminjaman Sepeda ({}).".format(selected_season))
st.dataframe(df_filtered.head())

# --- Analisis Tren Bulanan ---
st.subheader("📊 Tren Peminjaman Sepeda per Bulan ({})".format(selected_season))

# Mengelompokkan data berdasarkan bulan
monthly_trend = df_filtered.groupby('mnth')['cnt'].sum().reset_index()
monthly_trend['change'] = monthly_trend['cnt'].diff()
month_with_biggest_drop = monthly_trend.loc[monthly_trend['change'].idxmin(), 'mnth']

# Membuat plot tren peminjaman
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=monthly_trend, x='mnth', y='cnt', marker='o', linewidth=2.5, label='Total Peminjaman', ax=ax, color='royalblue')
ax.axvline(x=month_with_biggest_drop, color='red', linestyle='--', label=f'Penurunan Terbesar (Bulan {month_with_biggest_drop})')
ax.set_xticks(range(1, 13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'])
ax.set_xlabel('Bulan')
ax.set_ylabel('Total Peminjaman')
ax.set_title(f'📉 Tren Peminjaman Sepeda per Bulan ({selected_season})', fontsize=14)
ax.legend()
ax.grid(alpha=0.3)
st.pyplot(fig)

# --- Analisis Feature Importance ---
st.subheader("🔍 Faktor yang Mempengaruhi Peminjaman ({})".format(selected_season))

# Memilih fitur yang relevan
features = ['weathersit', 'temp', 'hum', 'windspeed', 'holiday', 'workingday']
X = df_filtered[features]
y = df_filtered['cnt']

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
ax.set_title(f'📊 Feature Importance - Faktor yang Mempengaruhi Peminjaman ({selected_season})')
ax.grid(axis='x', linestyle='--', alpha=0.5)
st.pyplot(fig)

# --- Kesimpulan ---
st.markdown("---")
st.subheader("📌 Kesimpulan ({})".format(selected_season))
st.info(
    "- Bulan dengan penurunan peminjaman terbesar: **Bulan {}**.\n"
    "- Faktor paling berpengaruh terhadap jumlah peminjaman: **{}**."
    .format(month_with_biggest_drop, importance_df.iloc[0, 0])
)

st.markdown("---")
st.write("🚀 Dibuat dengan Streamlit | Data: Bike Sharing Dataset")
