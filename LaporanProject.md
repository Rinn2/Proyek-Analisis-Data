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

### URL Dataset 
Link Dataset : https://www.kaggle.com/datasets/priyamchoksi/100000-diabetes-clinical-dataset
### Jumlah Baris dan Kolom
Dataset ini memiliki 16 kolom dengan total 100.000 baris data, yang terdiri dari 10 kolom dengan tipe data integer, 3 kolom dengan tipe data string, dan 3 kolom dengan tipe data float
### Kondisi
Kondisi dataset tidak  ada missing value pada seluruh kolom dalam dataset. Selain itu, ditemukan 14 data duplikat dalam dataset.Lalu pada  dataset ini memiliki data outlier pada kolom blood_glucose_level,hbA1c_level, dan bmi

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
- Menghapus duplikat data yang ada didalam dataset
- Melakukan encoding terhadap variabel kategorikal menggunakan LabelEncoder dan OneHotEncoder.
- Menormalkan nilai numerik  untuk fitur yang skewed seperti blood_glucose_level dan bmi.
- Membagi data menjadi data latih dan data uji (train-test split).

## Modeling
Model yang digunakan 
1. Logistic Regression Logistic Regression adalah metode klasifikasi yang digunakan untuk memprediksi output biner.Menggunakan fungsi logistik (sigmoid) untuk mengubah output menjadi nilai probabilitas antara 0 dan 1
### Cara Kerja 
Fungsi Logistik (Sigmoid): Logistic regression menggunakan fungsi logistik (sigmoid) untuk memetakan hasil regresi linear ke dalam rentang probabilitas antara 0 dan 1.Selanjutnya proses training melibatkan pencarian bobot (weights) dan bias yang meminimalkan fungsi kerugian (loss function), yang biasanya menggunakan binary cross-entropy loss atau log-loss.

![image](https://github.com/user-attachments/assets/56ba19b9-8a0e-4403-8195-efcae3976e06)

### Parameter 
- Koefisien (weights) Parameter yang menentukan seberapa besar pengaruh setiap fitur input terhadap prediksi output.

- Bias (intercept) Parameter tambahan yang memungkinkan model untuk memprediksi nilai bahkan ketika semua input adalah 0.

- Learning Rate digunakan dalam optimisasi (misalnya menggunakan gradient descent) untuk menentukan seberapa besar langkah yang diambil untuk memperbarui parameter model selama pelatihan.
### Kelebihan 
- Logistic Regression mudah dipahami dan diimplementasikan
- Sangat baik untuk masalah klasifikasi yang memiliki hubungan linear antara fitur dan kelas target
- Model ini dapat dengan mudah dijelaskan karena parameter (koefisien) menunjukkan kontribusi setiap fitur terhadap hasil akhir
  
### Kekurangan
- Logistic Regression tidak bekerja dengan baik pada masalah yang memiliki hubungan non-linear antar fitur
- Model ini mudah dipengaruhi oleh outlier
  
2. Random Forest adalah algoritma ensemble learning yang membangun banyak pohon keputusan (decision trees) dan menggabungkan hasilnya untuk membuat prediksi yang lebih akurat dan stabil.
### Cara Kerja 
- Bootstrap Aggregating (Bagging)  menggunakan teknik bagging yang melibatkan pengambilan sampel data secara acak dengan pengulangan (bootstrap) untuk melatih setiap pohon keputusan
- Pembangunan Pohon Keputusan artnya setiap pohon keputusan di Random Forest dibangun dengan memilih subset acak dari fitur pada setiap pembelahan (split), yang membedakan Random Forest dari pohon keputusan biasa yang mempertimbangkan semua fitu
- Voting/Averaging setelah pohon-pohon keputusan selesai dilatih, Random Forest menggabungkan hasil prediksi dari seluruh poho

### Parameter 
- n_estimators yaitu jumlah pohon keputusan yang akan dibangun. Semakin banyak pohon, semakin stabil hasilnya, meskipun juga meningkatkan waktu komputasi.
- max_features yaitu jumlah maksimum fitur yang akan dipertimbangkan untuk setiap pembelahan pohon.
- max_depth yaitu  kedalaman maksimum pohon. Ini membatasi jumlah pembelahan yang dapat dilakukan pada setiap pohon, yang membantu mengontrol overfitting.
- min_samples_spli yaitu jumlah minimum sampel yang diperlukan untuk membagi node. Ini juga dapat membantu dalam mengontrol overfitting.
- min_samples_leaf yaitu jumlah minimum sampel yang diperlukan untuk menjadi daun (leaf) pada pohon keputusan.

### Kelebihan 
- Dengan menggabungkan banyak pohon keputusan, Random Forest menghasilkan prediksi yang lebih stabil dan akurat, mengurangi overfittin
- Tidak Rentan Terhadap Overfitting
- Cocok untuk Data Tidak Terstruktu

### Kekurangan 
- Kurang Efektif pada Data yang Sangat Keci
- Proses pelatihan dapat memakan waktu
- Random Forest dapat menghasilkan model yang sangat besar dan sulit untuk diinterpretasikan karena banyaknya pohon yang terlibat
  
3. Neural Network  (Jaringan Saraf Tiruan) adalah model pembelajaran mesin yang terinspirasi oleh cara kerja otak manusia. Model ini terdiri dari beberapa lapisan (layers) yang saling terhubung, di mana setiap lapisan terdiri dari neuron-neuron yang menghitung hasil berdasarkan input yang diberikan
### Cara Kerja 
- Input Layer yaitu lapisan pertama yang menerima data. Setiap node di lapisan ini mewakili fitur input.
- Hidden Layers yaitu lapisan tersembunyi yang terdiri dari neuron-neuron yang menghitung hasil berdasarkan input yang diterima dari lapisan sebelumnya. Hasil perhitungan dihasilkan melalui fungsi aktivasi seperti ReLU atau sigmoid
- Output Layer yaitu lapisan terakhir yang menghasilkan output dari jaringan saraf
- Compile yaitu setelah model dibangun, langkah selanjutnya adalah mengompilasi model. Proses ini melibatkan pengaturan algoritma optimisasi, fungsi kerugian (loss function), dan metrik yang ingin digunakan selama pelatihan
- model.fit  fungsi utama untuk melatih (training) model dalam Keras (TensorFlow)

### Parameter 
- Layer yaitu lapisan jaringan saraf yang dapat berupa lapisan input, tersembunyi (hidden), atau outpu
- Units (Neurons) yaitu jumlah neuron dalam setiap lapisan
- Activation Functions yaitu ungsi aktivasi yang digunakan untuk mengubah output dari neuron
- Learning Rate yaitu kecepatan pembaruan bobot selama pelatihan
- Batch Size yaitu jumlah sampel data yang digunakan untuk memperbarui bobot pada setiap iterasi.
- Epochs yaitu jumlah iterasi di mana seluruh dataset digunakan untuk melatih model.

### Kelebihan 
- Kemampuan untuk Menangani Data Kompleks
- Kemampuan untuk Belajar dari Data yang Kompleks
- Ekosistem yang Kuat (Keras dan TensorFlow)
### Kekurangan 
- Kebutuhan Sumber Daya yang Besar
- Waktu Pelatihan yang Lama
- Interpretabilitas yang Rendah
  
## Evaluation

Metrik evaluasi yang digunakan:
Dalam proses evaluasi model, tiga metrik utama yang digunakan adalah
- Accuracy (Akurasi) mengukur proporsi prediksi yang benar dibandingkan dengan keseluruhan jumlah data. Metrik ini berguna ketika distribusi kelas seimbang.
Rumus
![image](https://github.com/user-attachments/assets/5ef19c84-9572-49e2-8cd0-ca75c87f8043)
Penjelasan :
TP = True Positive
TN = True Negative
FP = False Positive
FN = False Negative

- Precision  (Presisi) mengukur seberapa banyak prediksi positif yang benar-benar relevan (benar). Metrik ini penting ketika biaya dari kesalahan positif (false positive) cukup tinggi.
Rumus
![image](https://github.com/user-attachments/assets/653b4ff5-a035-4e9e-b1ca-108ac7a36c02)


- Recall (Sensitivitas)  mengukur seberapa banyak dari total data positif yang berhasil dikenali oleh model. Metrik ini berguna ketika sangat penting untuk menangkap sebanyak mungkin data positif
Rumus
![image](https://github.com/user-attachments/assets/5ea139a1-7898-4c94-a3c0-d53c0ebdf82e)

- F1-Score merupakan harmonisasi antara precision dan recall. Metrik ini sangat berguna ketika kita menginginkan keseimbangan antara precision dan recall.
Rumus
![image](https://github.com/user-attachments/assets/837a601d-6180-4592-9e7c-fe00f413f3e2)


Hasil Metrik Evaluasi :
1. Logistic Regression :95% masih mampu memberikan hasil yang sangat kompetitif dengan akurasi 95%. 
2. Random Forest  : 97%  menunjukkan performa terbaik di antara ketiga model dengan akurasi tertinggi (97%) serta precision dan recall yang tinggi.
3. Neural Network : 96% memiliki akurasi yang sedikit lebih rendah dari Random Forest, namun tetap menunjukkan performa yang baik

Evaluasi Dengan Data Baru
1.Logistic Regression
![image](https://github.com/user-attachments/assets/fb1bb9bb-357b-4fcf-8731-ce7bb334c0c2)
Berdasarkan evaluasi dengan data baru pada menggunakan Logistic Regression menghasilkan Output diabetes pada 2 data barunya

2.Random Forest 
![image](https://github.com/user-attachments/assets/b15e254e-be62-4c97-8065-3af9a1688d17)
Berdasarkan evaluasi dengan data baru pada menggunakan Random  Forest menghasilkan Output diabetes pada 2 data barunya

3.Neural Network
![image](https://github.com/user-attachments/assets/4258fe90-93cb-4d83-81cf-951d1f4a3449)
Berdasarkan evaluasi dengan data baru pada menggunakan Neural Network   menghasilkan Output diabetes pada 2 data barunya

# Kesimpulan 
Ketiga model yang diuji Random Forest, Logistic Regression, dan Neural Network menunjukkan hasil yang konsisten saat dievaluasi dengan data baru yang sama. Ketiga model memprediksi bahwa kedua individu dalam data baru memiliki risiko Diabetes
