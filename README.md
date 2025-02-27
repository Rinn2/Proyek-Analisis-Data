# 🚴 Analisis Peminjaman Sepeda dengan Streamlit

## 📌 Deskripsi Proyek
Aplikasi ini dibuat menggunakan **Streamlit** untuk menganalisis data peminjaman sepeda berdasarkan berbagai faktor seperti cuaca, suhu, kecepatan angin, dan hari kerja/libur. Dengan bantuan **Random Forest Regressor**, aplikasi ini juga menentukan faktor paling berpengaruh terhadap jumlah peminjaman sepeda.

## 📂 Dataset
Dataset yang digunakan berisi informasi mengenai peminjaman sepeda dengan kolom seperti:
- `mnth`: Bulan peminjaman
- `cnt`: Jumlah total peminjaman
- `weathersit`: Kondisi cuaca
- `temp`: Suhu
- `hum`: Kelembaban udara
- `windspeed`: Kecepatan angin
- `holiday`: Apakah hari tersebut hari libur
- `workingday`: Apakah hari tersebut hari kerja

## ⚙️ Instalasi dan Menjalankan Aplikasi
1. **Clone repository ini**:
   ```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name
   ```

2. **Buat virtual environment (opsional tetapi direkomendasikan)**:
   ```bash
   python -m venv env
   source env/bin/activate  # Untuk macOS/Linux
   env\Scripts\activate  # Untuk Windows
   ```

3. **Install dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi Streamlit**:
   ```bash
   streamlit run dashboard.py
   ```

## 📊 Fitur Utama
✅ **Visualisasi Tren Peminjaman Sepeda**
   - Grafik tren peminjaman sepeda per bulan
   - Identifikasi bulan dengan penurunan peminjaman terbesar

✅ **Analisis Faktor Peminjaman Sepeda**
   - Model **Random Forest Regressor** untuk menentukan faktor paling berpengaruh
   - Visualisasi **Feature Importance**

## 📌 Hasil Analisis
Dari hasil analisis, faktor yang paling berpengaruh terhadap peminjaman sepeda adalah:
1. **Kecepatan Angin (windspeed)**
2. **Suhu Udara (temp)**
3. **Kelembaban (hum)**

Bulan dengan penurunan peminjaman terbesar juga diidentifikasi melalui grafik tren peminjaman.

## 🛠 Teknologi yang Digunakan
- **Python**
- **Streamlit**
- **Pandas**
- **Matplotlib & Seaborn**
- **Scikit-learn**

## 💡 Pengembangan Selanjutnya
- Menambahkan fitur **prediksi peminjaman sepeda** berdasarkan cuaca
- Menganalisis **pola peminjaman sepeda pada hari kerja vs hari libur**

📩 **Kontribusi**: Jika tertarik untuk berkontribusi, silakan lakukan pull request atau hubungi saya!

🚀 **Selamat mencoba!**

