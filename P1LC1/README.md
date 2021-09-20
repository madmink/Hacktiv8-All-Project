# Live Code 1

## Instruction

Live Code ini dikerjakan dalam format ***notebook*** isi *notebook* harus mengikuti *outline* di bawah ini:
1. Perkenalan\
   Bab pengenalan harus diisi dengan identitas
2. **Judul/Penanda Soal**\
    Sediakan *Cell* Markdown sebelum cell import pustaka yang berisi nomor soal dan judul problem yang dikerjakan di tiap soalnya. Tiap soal mengikuti format nomor 2-13.
3. *Import* pustaka yang dibutuhkan\
   *Cell* pertama pada *notebook* **harus berisi dan hanya berisi** semua *library* yang digunakan dalam *project*.
4. *Data Loading*\
   Bagian ini berisi proses *data loading* yang kemudian dilanjutkan dengan *explorasi data* secara sederhana.
5. *Data Cleaning*\
   Bagian ini berisi proses penyiapan data berupa data cleaning sebelum dilakukan *explorasi data* lebih lanjut. Proses cleaning dapat berupa memberi nama baru untuk setiap kolom, mengisi missing values, menghapus kolom yang tidak dipakai, dan lain sebagainya.
6. *Explorasi Data*\
   Bagian ini berisi explorasi data pada dataset diatas dengan menggunakan query, grouping, visualisasi sederhana, dan lain sebagainya.
7. *Data Preprocessing*\
   Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti pembagian data menjadi train-dev-test, transformasi data (normalisasi, encoding, dll.), dan proses-proses lain yang dibutuhkan.
8. *Pendefinisian Model*\
   Bagian ini berisi cell untuk mendefinisikan model sampai kompilasi model. Akan lebih bagus jika didahului dengan penjelasan mengapa memilih arsitektur atau jenis model tertentu, alasan memilih nilai hyperparameter, dan hal lain yang berkaitan.
9. *Pelatihan Model*\
   Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan.
10. *Evaluasi Model*\
   Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model.
11. *Model Inference*\
   Bagian ini diisi dengan model inference, di mana model yang sudah kita latih akan dicoba pada data selain data yang sudah tersedia. Data yang dimaksud bisa berupa data buatan oleh student, ataupun data yang ada pada internet.
12. *Pengambilan Kesimpulan*\
   Pada bab terakhir ini, **harus berisi** kesimpulan yang mencerminkan hasil yang didapat dengan dibandingkan dengan *objective* yang sudah ditulis di bagian pengenalan.
13. *Notebook* harus diupload dalam akun GitHub masing-masing siswa untuk selanjutnya dinilai.

---

## Problems
1. Buatlah model linear regression untuk memprediksi biaya asuransi menggunakan dataset yang dapat diunduh [disini](https://www.kaggle.com/mirichoi0218/insurance?select=insurance.csv).
2. Buatlah model SVM untuk mengklasifikasikan tipe galaksi menggunakan dataset yang dapat diunduh [disini](https://github.com/fahmimnalfrzki/Dataset/raw/main/GalaxyMorphology.csv). (*link data original [disini](https://www.kaggle.com/saurabhshahane/galaxy-classification)*).

   **NOTE NOMOR 2**
   - Hanya ambil kolom C,A,S,G2,dan H untuk dijadikan feature
   - Tidak perlu mengerti arti dari kolom-kolom tersebut
   - Tidak perlu mengecek teori-teori atau referensi yang tidak ada kaitannya dengan data science
   - 0: galaksi elips, 1: galaksi spiral

---

## Assignment Rubrics

### Code Review

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|Preprocessing|Mampu Melakukan Preproses Dataset Sebelum Melakukan Proses Modeling (split data, normalisasi, encoding, dll) | 20 pts each number (40 max) |
|Linear Regression| Mengimplementasikan Linear Regression dan Menentukan Hyperparameter yang Tepat dengan Scikit-Learn | 10 pts |
|SVM| Mengimplementasikan SVM dan Menentukan Parameter yang Tepat dengan Scikit-Learn | 10 pts |
|Model Evaluation|Mampu melakukan evaluasi terhadap LR dan SVM Model yang telah dibuat | 20 pts each (40 max) |
|Model Inference| Mencoba model yang telah dibuat dengan random data dari masing-masing student | 10 pts each number (20 max) |
|Apakah Kode Berjalan Tanpa Ada Error?|Kode Berjalan Tanpa Ada Error. Seluruh Kode Berfungsi Dan Dibuat Dengan Benar.| 10 pts |

### Readability

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|Tertata Dengan Baik|Semua baris kode terdokumentasi Dengan Baik Dengan Markdown Untuk Penjelasan Kode.| 10 pts |

### Analysis

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|Model Analysis| Menganalisa informasi dari model yang telah dibuat| 20 pts each number (40 max) |
|EDA Analysis|Menarik Informasi/Kesimpulan Dari Eksplorasi Data yang Dilakukan.| 5 pts each number (10 max) |


---

```{admonition} Total Points
**190**
```
