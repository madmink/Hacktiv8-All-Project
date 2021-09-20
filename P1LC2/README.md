# Live Code 2


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
14. **DISARANKAN MENGERJAKAN DI GOOGLE COLAB**
15. **Simpan Notebook dengan nama file: h8_p1lc2_NAMA.ipynb, push ke branch masing-masing**

---

## Problems

1. Menggunakan dataset https://www.kaggle.com/nareshbhat/health-care-data-set-on-heart-attack-possibility, buatlah model machine learning untuk mengklasifikasikan kemungkinan orang terkena serangan jantung. Bandingkan antara model Decision Tree dan Random Forest. Mana yang lebih baik untuk data ini?

---

## Assignment Rubrics

### Code Review

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|Preprocessing|Mampu Melakukan Preproses Dataset Sebelum Melakukan Proses Modeling (split data, normalisasi,standardisasi, encoding, dll) | 20 pts |
|Decision Tree|Mampu melakukan training data dengan model decision tree serta melakukan hyperparameter tunning dengan **maksimal 2 hyperparameter dan 2 set values masing-masing hyperparameter (4 kombinasi)**| 25 pts |
|Ensemble Learning|Mampu melakukan training data dengan model Random Forest serta melakukan hyperparameter tunning dengan **maksimal 2 hyperparameter dan 2 set values masing-masing hyperparameter (4 kombinasi)**| 25 pts |
|Model Evaluation|Mampu melakukan evaluasi model DT dan RF yang telah dibuat| 20 pts each model (40 max)|
|Model Inference | Mampu Mencoba model yang telah dibuat dengan random data dari masing-masing student|10 pts each model (20 max)|
|Apakah Kode Berjalan Tanpa Ada Error?|Kode Berjalan Tanpa Ada Error. Seluruh Kode Berfungsi Dan Dibuat Dengan Benar.|10 pts|

### Readability

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|Tertata Dengan Baik|Semua Cell Di Notebook Terdokumentasi Dengan Baik Dengan Markdown Pada Tiap Cell Untuk Penjelasan Kode.| 10 pts|
|Informasi dan Analisa|Terdapat penjelasan/informasi tiap EDA dan informasi setiap keputusan yang diambil pada data terutama di bagian Preprocessing dan penentuan set hyperparameter| 10 pts|

### Analysis

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|EDA Analysis|Menarik Informasi/Kesimpulan Dari Eksplorasi Data yang Dilakukan.| 40 pts |
|Model Analysis|Menganalisa informasi dari model yang telah dibuat|30 pts|

---

```{admonition} Total Points
**230**
```
