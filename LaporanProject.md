# Laporan Proyek Machine Learning - Agus Irvan Maulana

## Domain Proyek

Masalah kesehatan, terutama penyakit kronis seperti diabetes, merupakan isu global yang membutuhkan perhatian serius. Diabetes adalah salah satu penyakit tidak menular yang jumlah kasusnya terus meningkat setiap tahun. Deteksi dini terhadap potensi diabetes menjadi langkah krusial untuk mencegah komplikasi yang lebih serius. Dengan memanfaatkan machine learning, saya  dapat membangun sistem prediksi diabetes berdasarkan data pasien.

## Business Understanding
Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Bagaimana memprediksi apakah seorang pasien mengidap diabetes berdasarkan fitur-fitur medis?
- Fitur apa saja yang paling berpengaruh terhadap prediksi diabetes?

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Membangun model klasifikasi untuk memprediksi status diabetes seseorang.
- Mengetahui kontribusi tiap fitur terhadap klasifikasi diabetes.


    ### Solution statements
    - Menggunakan beberapa algoritma klasifikasi seperti Logistic Regression, Random Forest, dan Neural Network
    - Metrik yang digunakan: accuracy, precision, recall, F1-score.

## Data Understanding
Dataset yang digunakan berasal dari Kaggle Diabetes Health Indicators Dataset. Dataset ini berisi informasi medis seperti umur, BMI, tingkat glukosa darah, riwayat merokok, dan sebagainya.


### Variabel-variabel pada   dataset adalah sebagai berikut:
- year: Tahun data dicatat atau dikumpulkan (misal: 2020, 2021, dll).
- gender: Jenis kelamin pasien (misalnya: "Male", "Female", "Other").
- age: Usia pasien
- location: Lokasi atau wilayah tempat pasien tinggal atau dirawat
- race:AfricanAmerican: 1 jika pasien beretnis Afrika-Amerika, 0 jika tidak.
- race:Asian: 1 jika pasien beretnis Asia, 0 jika tidak.
- race:Caucasian: 1 jika pasien beretnis Kaukasia, 0 jika tidak.
- race:Hispanic: 1 jika pasien beretnis Hispanik, 0 jika tidak.
- race:Other: 1 jika pasien berasal dari etnis lain yang tidak disebutkan, 0 jika tidak.
-  hypertension: 1 jika pasien memiliki riwayat tekanan darah tinggi, 0 jika tidak.
-  eart_disease: 1 jika pasien memiliki riwayat penyakit jantung, 0 jika tidak.
-  smoking_history: Riwayat merokok pasien
- bmi: Indeks Massa Tubuh pasien (Body Mass Index), ukuran berat badan relatif terhadap tinggi badan.
- hbA1c_level: Tingkat HbA1c (hemoglobin terglikasi), indikator kadar gula darah jangka panjang.
-  blood_glucose_level: Kadar gula darah saat ini pasien
- diabetes: 1 jika pasien terdiagnosis diabetes, 0 jika tidak.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.
- Menghapus kolom gender, smoking_history, dan location karena nilai tidak relevan atau terlalu bervariasi.
- Melakukan encoding terhadap variabel kategorikal menggunakan LabelEncoder dan OneHotEncoder.
- Menormalkan nilai numerik  PowerTransformer untuk fitur yang skewed seperti blood_glucose_level dan bmi.
- Membagi data menjadi data latih dan data uji (train-test split).


## Modeling
Model yang digunakan 
1. Logistic Regression
2. Random Forest Classifier
3. Neural Network
## Evaluation

Metrik evaluasi yang digunakan:
- Accuracy
- Recall
- Precision

Hasil Evaluasi :
1. Logistic Regression :91%
2. Random Forest Classifier : 97%
3. Neural Network : 96%
