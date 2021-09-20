# G2P0
# Graded Challenge 2

_Graded Challenge ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada Linear Algebra dan Calculus._

Pada graded challenge ini, anda diminta melakukan image processing menggunakan konsep linear algebra dan kalkulus.

---

## Dataset Description

Dataset yang digunakan adalah sebuah gambar yang dapat diunduh pada link berikut: https://cdn.cnn.com/cnnnext/dam/assets/201030094143-stock-rhodesian-ridgeback-exlarge-169.jpg

Sumber gambar: https://edition.cnn.com/2020/10/30/world/dog-dna-intl-scli-gbr-scn/index.html

## Assignment Instructions

*Graded Challenge 1* dikerjakan dalam format ***notebook*** dengen beberapa **kriteria wajib** di bawah ini:

1. Gunakan library **Numpy** untuk kebutuhan pengolahan tipe data array dan beberapa operasi matematika.
2. Jika diperlukan, silahkan menggunakan library **Scipy**, **Numpy**, **Sympy** atau lainnya untuk melakukan perhitungan matematika.
3. Gunakan library **PIL** untuk membaca dan pengolahan gambar
4. Untuk visualisasi, gunakan library **Matplotlib**
5. *Objektif* dari project ini adalah mendeteksi edge suatu gambar dan melakukan transformasi linear pada gambar. Sebagai clue, berikut langkah-langkah untuk mendeteksi edge:
    1. Hitung vektor gradien (turunan parsial) masing-masing pixel untuk masing-masing sumbu x dan y dengan rumus $\frac{\partial I}{\partial x}$ dan $\frac{\partial I}{\partial y}$
    2. Hitung gradient magnitude tiap pixel dengan rumus $mag=\sqrt{(\frac{\partial I}{\partial x})^2 + (\frac{\partial I}{\partial y})^2}$
    3. Jika nilai magnitude melebihi angka threshold, maka edge terdeteksi (Biasanya threshold ~ 30)
6. **Catatan**: Anda dapat menggunakan metode apapun, baik menggunakan library atau melakukan perhitungan dengan metode numerik.
7. *Project* dinyatakan selesai dan diterima untuk dinilai jika saat dilakukan `Run All` pada *notebook*, semua *cell* berhasil tereksekusi sampai akhir.
8. Isi *notebook* harus mengikuti *outline* di bawah ini:
   1. Perkenalan\
   Bab pengenalan harus diisi dengan identitas, *metode* yang ingin dilakukan guna mencapai tujuan, dan transformasi linear apa yang ingin diterapkan pada gambar.
   2. *Import* pustaka yang dibutuhkan\
   *Cell* pertama pada *notebook* **harus berisi dan hanya berisi** semua *library* yang digunakan dalam *project*.
   3. *Data Loading*\
   Bagian ini berisi proses *data loading* yang kemudian dilanjutkan dengan *explorasi data* secara sederhana.
   4. *Data Preprocessing*\
   Bagian ini berisi proses penyiapan data berupa preprocessing sebelum dilakukan *processing* lebih lanjut. Proses preprocessing dapat berupa filtering komponen warna ataupun ubah gambar warna menjadi grey, dan lain sebagainya.
   5. *Image Processing*\
   Bagian ini berisi kode-kode serta perhitungan-perhitungan untuk mencapai tujuan.
   6. Hasil dan Kesimpulan\
   Pada bab terakhir ini, **harus berisi** kesimpulan yang mencerminkan hasil yang didapat dengan membandingkan hasil untuk beberapa nilai threshold dan juga hasil transformasi linear yang telah dilakukan.
4. *Notebook* harus diupload dalam akun GitHub masing-masing siswa untuk selanjutnya dinilai.

## Assignment Submission

- Simpan assignment pada sesi ini dengan nama `h8dsft_P0W2`.
- Push Assigment yang telah kalian buat ke akun Github kalian masing-masing.

## Assignment Objectives

*Graded Challenge 2* ini dibuat guna mengevaluasi Linear Algebra dan Calculus sebagai berikut:

- Mampu memuat data gambar
- Mampu melakukan transformasi tipe data gambar ke data yang siap olah
- Mampu melakukan eksplorasi data gambar
- Mampu menerapkan konsep kalkulus pada pengolahan citra menggunakan library atau metode numerik from scratch
- Mampu menerapkan konsep linear algebra pada pengolahan citra menggunakan library atau metode numerik from scratch
- Mampu memvisualisasikan gambar menggunakan matplotlib

---

## Assignment Rubrics

### Code Review

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|Data Loading|Mampu memuat data gambar dengan library PIL| 2 pts |
|Data Transformation|Mampu mentransformasikan gambar ke array| 2 pts |
|Image Data Exploration|Mampu mengeksplorasi data gambar dan mengambil keputusan dalam menindaklanjut data| 3 pts |
|Calculus Implementation|Mampu menerapkan perhitungan turunan parsial/vector gradient dalam kode| 10 pts |
|Linear Algebra Implementation|Mampu menerapkan perhitungan transformasi linear dalam kode| 10 pts |
|Image Visualization|Mampu memvisualisasikan gambar dengan Matplotlib| 3 pts |

### Readability

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|Tertata Dengan Baik|Semua Cell Di Notebook Terdokumentasi Dengan Baik Dengan Markdown Pada Tiap Cell Untuk Penjelasan Kode.| 10 pts |

### Analysis

|Criteria|Meet Expectations|Points|
|--- |--- |--- |
|Overall Analysis|Menarik Informasi/Kesimpulan Dari Perbandingan Nilai Threshold min 3 nilai.| 10 pts |

---

```{admonition} Total Points
**50**
```

