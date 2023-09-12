
-------------------------------------
TUGAS 2 PEMROGRAMAN BERBASIS PLATFORM 
-------------------------------------
Nama    : Sekar Gandes Dianti

NPM     : 2206082713

Kelas   : PBP D

Tautan aplikasi:
https://dapur-laekker.adaptable.app/main/

---
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
---
Checklist 1 - Membuat sebuah proyek Django baru.
Hal yang dilakukan:
- Membuat repositori GitHub dan menamakannya dengan nama proyek yang saya buat, yakni `dapur-laekker`
- Membuat direktori `dapur-laekker` dan melakukan konfigurasi repositori git terhadap folder tersebut.
- Mengaktifkan virtual environment.
- Membuat dependencies ke dalam file 'requirement.txt' dan menginstall dependencies tersebut
- Membuat proyek Django dengan perintah `django-admin startproject dapur_laekker .`
- Melakukan konfigurasi proyek, seperti menambah * ALLOWED_HOST di settings.py, dan kemudian menjalankan server.
- Menambahkan file `.gitignore` pada direktori yang sama.
- Melakukan add, commit, push semua file yang ada pada direktori dapur_laekker ke repositori GitHub
- Melakukan deployment di Adaptable.io.

Checklist 2 - Membuat aplikasi `main` pada proyek tersebut
Hal yang dilakukan:
- Membuat direktori dengan nama `main` di dalam `dapur_laekker`.
- Menjalankan `python manage.py startapp main` untuk membuat aplikasi baru.
- Memasukkan `main` ke dalam list `INSTALLED_APPS` di direktori `dapur_laekker`.

Checklist 3 - Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
Hal yang dilakukan: 
- Membuat file `ulrs.py` di direktori `main`.
- Mengimpor `path` dari `django.urls` utnuk mendefinisikan pola URL dan `show-main` dari `main.views` untuk menampilkan tampilan ketika URL diakses
- Membuat variabel `app_name` dan meng-assign `main` ke dalamnya, tujuannya adlaah untuk memberikan nama unik pada pola URL dalam aplikasi.

Checklist 4 - Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib seperti di soal.
Hal yang dilakukan: 
- Membuat kelas  `Inventory` pada file `models.py` dengan atribut `name`, `amount`, dan `description`.
- Melakukan migrasi model.

Checklist 5 - Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.
Hal yang dilakukan: 
- Membuat fungsi `show_main` yang mana nantinya fungsi tersebut akan mengembalikan data ke dalam template html yang menampilkan nama aplikasi, nama, dan kelas. 

Checklist 6 - Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
Hal yang dilakukan: 
- Membuat file `urls.py` di dalam direktori `dapur_laekker`, kemudian mengimpor fungsi `include` dari `django.urls` dan menambahkan rute URL untuk mengarahkan ke main di dalam variabel `urlpatterns`.
- Memcoba menjalankan proyek Django dan membuka http://localhost:8000/main/ di browser untuk melihat apakah tampilannya sudah sesuai.

Checklist 7 - Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Hal yang dilakukan: 
- Melakukan proses deploy di Adaptable.io dengan mengambil dari repositori `dapur-laekker`
- Setelah deploy berhasil, mencoba untuk mengakses[URL aplikasi]/main/ untuk mengecek apakah aplikasi main dapat berjalan dengan baik dan tampilan sudah sesuai.

Checklist 8 - Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan yang diberikan di soal.
Hal yang dilakukan: 
- Buat file `README.md` dan tambahkan tautan menuju aplikasi Adaptable yang sudah di-deploy.
- Jawab pertanyaan-pertanyaan yang diberikan di soal dalam README.md.
- Add, commit, dan push file `README.md` ke repositori GitHub.

---
Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
---
```
                                 urls.py
          (melakukan request)  ↗          ↘   (memilih view)           (query)           (transaksi data)
                        user                     views.py   <----------------->  models.py  <-------->  database
    (menampilkan halaman web)  ↖          ↙  (memilih template)   (respon data)
                                 templates 

```
Kaitan antara urls.py, views.py, models.py, dan berkas html adalah sebagai berikut.
1. `urls.py` : menerjemahkan pola URL untuk mengarahkan request ke view yang sesuai.
2. `views.py` : menampilkan data dari model dan menghubungkannya dengan template.
3. `models.py`: menyimpan data-data dan logika dari aplikasi web.
4. Berkas html (templates) : menentukan tampilan halaman web berdasarkan data dari model melalui view. 

---
Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
---
Dalam pembuatan proyek atau aplikasi Django, virtual environment berfungsi untuk mengisolasi dan mengelola dependencies dalam proyek tersebut. Virtual environment dapat menghindari konflik dependencies, seperti package/dependencies yang bertabrakan karena beda versi. 

Meskipun tanpa menggunakan virtual environment, proyek atau aplikasi Django masih dapat dibuat. Namun, kekurangannya adalah ada kemungkinan terjadinya konflik dependencies dalam proyek atau aplikasi tersebut yang sulit dihindari yang akhirnya membuat proyek atau aplikasi tersebut sulit untuk dikelola. 

---
Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
---
MVC, MVT, dan MVVM adalah arsitektur yang digunakan dalam pengembangan aplikasi. Komponen-komponen yang ada di masing-masing arsitektur adalah sebagai berikut. 

MVC (Model-View-Controller)
- Model: mengelola data aplikasi
- View: menampilkan data kepada user
- controller: menerima input dari user, mengelola interaksi user, dan mengarahkan request kepada model atau view yang sesuai 

MVT (Model-View-Template)
- Model: mengelola data aplikasi
- View: menampilkan data kepada user 
- Template: mengatur cara data ditampilkan pada view

MVVM adalah adalah singkatan dari Model-View-ViewModel
- Model: mengelola data aplikasi
- View: menampilkan data kepada user
- ViewModel: mengonversi data menjadi format yang dapat ditampilkan oleh View dan menangani interaksi user.

Perbedaan antara MVC, MVT, MVVM adalah sebagai berikut.
1. Penekanan
   - MVC: terpusat pada pengendalian aliran program
   - MVT: terpusat pada pemisahan tampilan dari logika aplikasi
   - MVVM: terpusat pada pemisahan logikan presentasi dari model
2. Digunakan dalam
   - MVC: pengembangan perangkat lunak
   - MVT: kerangka kerja Django untuk aplikasi web
   - MVVM: pengembangan aplikasi front-end yang kompleks, seperti Angular atau Vue.js
3. Hubungan antarkomponen
   - MVC: view berfungsi secara independen dan tidak memiliki informasi tentang controller
   - MVT: menyimpan pengetahuan prese
   - MVVM: view menyimpan referensi ke ViewModel
