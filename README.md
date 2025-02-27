# 🚴 Analisis Peminjaman Sepeda dengan Streamlit

## 📌 Deskripsi Proyek
Aplikasi ini dibuat menggunakan **Streamlit** untuk menganalisis data peminjaman sepeda berdasarkan berbagai faktor seperti cuaca, suhu, kecepatan angin, dan hari kerja/libur. Dengan bantuan **Random Forest Regressor**, aplikasi ini juga menentukan faktor paling berpengaruh terhadap jumlah peminjaman sepeda.

## 📂 Dataset
Dataset yang digunakan berisi informasi mengenai peminjaman sepeda dengan kolom seperti:
🕒 Waktu & Indeks
instant: Indeks record
dteday: Tanggal peminjaman
season: Musim (1: Spring, 2: Summer, 3: Fall, 4: Winter)
yr: Tahun (0: 2011, 1: 2012)
mnth: Bulan (1 hingga 12)
hr: Jam dalam format 24 jam (0 hingga 23)
🚴‍♂️ Hari Kerja & Hari Libur
holiday: Apakah hari tersebut libur (1: Ya, 0: Tidak)
weekday: Hari dalam seminggu (0: Minggu, 1: Senin, ..., 6: Sabtu)
workingday: Apakah hari tersebut merupakan hari kerja (1: Ya, 0: Tidak)
🌦 Kondisi Cuaca
weathersit:
1: Cerah, Sedikit Berawan, Berawan Parsial
2: Kabut + Berawan, Kabut + Mendung, Kabut + Sedikit Berawan
3: Hujan Ringan, Salju Ringan, Petir + Awan Tersebar
4: Hujan Lebat + Badai Petir, Salju + Kabut
temp: Suhu normalisasi dalam Celsius (dibagi 41 sebagai nilai maksimum)
atemp: Suhu terasa dalam Celsius (dibagi 50 sebagai nilai maksimum)
hum: Kelembaban normalisasi (dibagi 100 sebagai nilai maksimum)
windspeed: Kecepatan angin normalisasi (dibagi 67 sebagai nilai maksimum)
📈 Data Peminjaman Sepeda
casual: Jumlah pengguna sepeda non-terdaftar
registered: Jumlah pengguna sepeda terdaftar
cnt: Jumlah total peminjaman sepeda (casual + registered)

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

