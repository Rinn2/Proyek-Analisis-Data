Ringkasan Notebook
Identitas
Nama: Agus Irvan Maulana

Cohort ID: MC381D5Y1073

Kelas: MC-48

 1. Import Library
    - Notebook ini memuat library penting untuk:

    - Visualisasi data: matplotlib, seaborn

    - Manipulasi data: pandas, os, glob

Deep Learning: tensorflow.keras

 2. Persiapan Data Gambar
   -Menggunakan dataset gambar dengan struktur folder: seg_train, seg_test, seg_pred.
   -Menghitung jumlah gambar di setiap folder.
   -Menampilkan beberapa sampel gambar dari tiap kelas.

 3. Split Data
 Data dibagi menjadi 3 bagian:
 Train: seg_train
 Validation: seg_pred
 Test: seg_test
Menggunakan ImageDataGenerator untuk preprocessing dan augmentasi gambar

 4. Membuat Model
 5. Membuat Plot Akurasi dan Loss Model
 6. Export Model

