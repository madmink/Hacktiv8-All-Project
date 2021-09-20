# Live Code 3

```{attention}
This page is still on development.
```


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
14. **DISARANKAN MENGERJAKAN DI GOOGLE COLAB JIKA LOCAL BERMASALAH**
---

## Problems

Menggunakan dataset https://www.kaggle.com/amansaxena/lifeexpectancy, buatlah model machine learning unsupervised menggunakan KMeans untuk mendeteksi kelompok negara dan jawab beberapa pertanyaan di bawah sebagai acuan analisa/cerita:

1. Pada bagian eksplorasi data, apa insight menarik yang bisa kamu ceritakan?
2. Berapa cluster yang berhasil kamu peroleh dari dataset tersebut? apakah sudah optimal? Visualisasikan hasil clustering yang kamu peroleh dengan plot 2 dimensi dimana 2 dimensi tersebut merupakan dimensi yang diperoleh dari hasil reduksi dimensi.
3. Bagaimana karakteristik dari masing-masing cluster? Bisakah kamu visualisasikan dan ceritakan?
4. Apa insight menarik yang kamu peroleh dari jawaban/analisa nomor 3?
5. Dibandingkan dengan EDA, apakah ada kesamaan dari hasil clustering yang kamu peroleh? coba ceritakan analisamu!

---

## Assignment Rubrics

### Code Review

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|Data Loading|Mampu memuat data dengan Pandas| 5 pts  |
|Data Processing and Cleaning|Mampu melakukan pengolahan data dan data cleaning | 15 pts |
|Feature Engineering|Mampu menyeleksi dan menyesuaikan feature yang akan ditrain oleh model| 15 pts|
|Unsupervised Model Implementation|Mampu melakukan training data dengan model KMeans| 20 pts |
|Model Evaluation|Mampu melakukan evaluasi model untuk menentukan nilai K/jumlah grup| 15 pts |
|PCA|Mampu melakukan reduksi dimensi dengan menggunakan PCA| 15 pts |

### Readability

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|Tertata Dengan Baik|Semua Cell Di Notebook Terdokumentasi Dengan Baik Dengan Markdown Pada Tiap Cell Untuk Penjelasan Kode.| 10 pts|

### Analysis

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|Overall Analysis|Menarik Informasi/Kesimpulan Dari Analisa.| 40 pts |

---

```{admonition} Total Points
**135**
```
