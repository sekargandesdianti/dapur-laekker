TUGAS 2 PEMROGRAMAN BERBASIS PLATFORM 
-------------------------------------
Nama    : Sekar Gandes Dianti

NPM     : 2206082713

Kelas   : PBP D

Tautan aplikasi:
https://sekar-gandes-dapurlaekker.pbp.cs.ui.ac.id


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

Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
---
Dalam pembuatan proyek atau aplikasi Django, virtual environment berfungsi untuk mengisolasi dan mengelola dependencies dalam proyek tersebut. Virtual environment dapat menghindari konflik dependencies, seperti package/dependencies yang bertabrakan karena beda versi. 

Meskipun tanpa menggunakan virtual environment, proyek atau aplikasi Django masih dapat dibuat. Namun, kekurangannya adalah ada kemungkinan terjadinya konflik dependencies dalam proyek atau aplikasi tersebut yang sulit dihindari yang akhirnya membuat proyek atau aplikasi tersebut sulit untuk dikelola. 

Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
---
MVC, MVT, dan MVVM adalah arsitektur yang digunakan dalam pengembangan aplikasi. Komponen-komponen yang ada di masing-masing arsitektur adalah sebagai berikut. 

MVC (Model-View-Controller)
- Model: mengelola data aplikasi
- ViewL menampilkan data kepada user
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

---

TUGAS 3 PEMROGRAMAN BERBASIS PLATFORM 
---
Nama	: Sekar Gandes Dianti

NPM	: 2206082713

Kelas	: PBP D

Apa perbedaan antara form POST dan form GET dalam Django?
----
- POST atau POST request: digunakan untuk mengirim data (file, form data, dsb) ke pada server.  POST mengembalikan kode status HTTP 201 jika berhasil. Data dikirim dalam request body dan tidak terlihat dalam URL.
- GET atau GET request: digunakan untuk membaca atau mengambil data dari web server. Get mengembalikan kode status HTTP 200 (OK) jika data berhasil diambil dari server. Data yang dikirimkan terlihat dalam URL sebagai parameter query string.

Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
---
Dalam konteks pengiriman data, perbedaan utama antara XML, JSON, dan HTML adalah XML dan JSON digunakan untuk tempat penyimpanan dan transmisi data. Perbedaan antara XML dan JSON adalah sebagai berikut.
<img width="749" alt="XML vs JSON" src="https://github.com/sekargandesdianti/coba-coba/assets/124732529/3b611634-1856-45d3-9ec1-80c121740caf">

Sedangkan, HTML tidak digunakan untuk pengiriman data melainkan untuk mendeskripsikan bagaimana data tersebut ditampilkan dalam web. 

Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
---
JSON sering digunakan dalam pertukaran data antara aplikasi web modern dikarenakan beberapa hal berikut ini.
- Mudah ditulis dan dimengerti karena menggunakan format key-value dan array yang dapat dibaca manusia.
- Tidak seperti XML, JSON tidak memerlukan tag, atribut, atau skema khusus apa pun. 
- JSON dapat mudah diurai oleh fungsi JavaScript karena sudah terintegrasi. 
- JSON dapat dikonversi ke dan dari objek JavaScript sehingga memudahkan web developer yang menggunakan JavaScript sebagai bahasa utama untuk aplikasi webnya. 

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
---
Checklist 1 - Membuat input form untuk menambahkan objek model pada app sebelumnya.
Hal yang dilakukan:
- Membuat file `forms.py` di dalam folder main dan mengisi file tersebut dengan kode berikut.
  ```
  from django.forms import ModelForm
  from main.models import Inventory
  
  class ProductForm(ModelForm):
      class Meta:
          model = Inventory
          fields = ["name", "amount", "description"]
  ```
- Membuat fungsi `create_product` pada file `views.py`. Fungsi tersebut digunakan untuk membuat form yang dapat menambahkan data invetori secara otomatis ketika data di-submit.
- Mengimpor fungsi `create_product` dan menambahkan path url ke `urls.py`
- Membuat file `create_product.html` di folder main/templates yang digunakan untuk menampilkan form.
- Menambahkan kode-kode pada `main.html` untuk menampilkan data inventori dalam bentuk tabel dan menambah tombol `Add New Product` yang akan redirect ke halaman form.
  
Checklist 2 - Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
Hal yang dilakukan: Membuat fungsi-fungsi baru pada `views.py` di folder `main` yang isinya sebagai berikut.
```
def show_xml(request):
    data = Inventory.objects.all()
    return HttpResponse(serializers.serialize('xml', data), 
                        content_type= 'application/xml')

def show_json(request):
    data = Inventory.objects.all()
    return HttpResponse(serializers.serialize('json', data),
                        content_type='application/json')

def show_xml_by_id(request, id):
    data = Inventory.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml', data), 
                        content_type= 'application/xml')

def show_json_by_id(request, id):
    data = Inventory.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', data),
                        content_type='application/json')
```

Checklist 3 - Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
Hal yang dilakukan: Menambah impor fungsi-fungsi tersebut dan menambahkan pathnya ke `urls.py` dengan kode berikut. 
```
path('xml/', show_xml, name= 'show_xml'),
path('json/', show_json, name='show_json'),
path('xml/<int:id>/', show_json_by_id, name='show_xml_by_id'),
path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
```

Checklist 4 -  Menjawab beberapa pertanyaan berikut pada README.md pada root folder.
Hal yang dilakukan: menjawab pertanyaan-pertanyaan tersebut dengan mencari referensi dari materi PPT di Scele dan internet.

Checklist 5 - Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
1. URL: http://127.0.0.1:8000/
   <img width="958" alt="tampilan html" src="https://github.com/sekargandesdianti/coba-coba/assets/124732529/e346d6ca-95d8-4371-b93a-50882249b256">

2. URL: http://127.0.0.1:8000/xml/
   <img width="960" alt="tampilan xml" src="https://github.com/sekargandesdianti/coba-coba/assets/124732529/badb5abf-a359-4176-99b3-ca56113f9b2d">

3. URL: http://127.0.0.1:8000/json/
   <img width="960" alt="tampilan json" src="https://github.com/sekargandesdianti/coba-coba/assets/124732529/c5ba34e6-2119-4e57-b704-a8924a3cfc80">

4. URL: http://127.0.0.1:8000/xml/2/
   <img width="960" alt="tampilan xml by id" src="https://github.com/sekargandesdianti/coba-coba/assets/124732529/e5adc9e2-5638-4c38-9582-e86e92fae03f">

5. URL: http://127.0.0.1:8000/json/3/
   <img width="960" alt="tampilan json by id" src="https://github.com/sekargandesdianti/coba-coba/assets/124732529/6d71b379-5af1-4811-ae03-647cff5e1b04">

Referensi Tugas 3
---
PPT Data Delivery (Markup Language & JSON) 

Tutorial 2 PBP Ganjil 23/24

Lane, R. (2023, May 16). What’s the relationship between XML, JSON, HTML and the internet? DeltaXML. https://www.deltaxml.com/blog/xml/whats-the-relationship-between-xml-json-html-and-the-internet/#:~:text=The%20differences%20between%20XML%2C%20JSON,how%20that%20data%20is%20displayed. 

House, E. (2021, April 7). XML vs JSON, what’s the difference? Medium. https://evanahouse.medium.com/xml-vs-json-whats-the-difference-4eac57818b30 

Berga, M. (2023, September 14). JSON vs XML: Which One is faster and more efficient?. Imaginary Cloud. https://www.imaginarycloud.com/blog/json-vs-xml/ 

AI and LinkedIn Community. (2023, August 25). What are the benefits and drawbacks of using JSON as a data format for web applications?. JSON for Web Applications: Benefits and Drawbacks. https://www.linkedin.com/advice/3/what-benefits-drawbacks-using-json-data#:~:text=One%20of%20the%20main%20benefits,data%20format%20for%20web%20applications. 

---

TUGAS 4 PEMROGRAMAN BERBASIS PLATFORM
---
Nama	: Sekar Gandes Dianti

NPM	: 2206082713

Kelas	: PBP D

Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
---
UserCreationFrom adalah bentuk dari Django forms yang berfungsi untuk membuat dan mendaftarkan user baru dalam aplikasi web yang dibuat.

Kelebihan:
- Mengurangi kompleksitas pengembangan aplikasi web dan mempercepat proses pembuatan formulir registrasi karena developer tidak harus menuliskan kodenya dari awal.
- Dilengkapi validasi bawaan untuk memastikan user memasukkan data yang benar dan sesuai.
- Terintegrasi dengan sistem autentikasi dari Django

Kekurangan: 
- Dirancang hanya untuk keperluan umum. Jika developer ingin menerapkan persyaratan pendaftaran user yang spesifik, maka harus dikustomisasi sendiri.
- Validasi tidak untuk semua kasus sehingga untuk keamanan yang lebih tinggi, maka developer harus menambahkannya sendiri.

Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
---
Autentikasi adalah proses memverifikasi bahwa pengguna adalah siapa yang mereka klaim. Sedangkan, otorisasi adalah proses menentukan apa yang boleh dilakukan oleh pengguna yang diautentikasi. Keduanya penting karena hal-hal berikut ini.

1. Memverifikasi identitas pengguna untuk mencegah akses yang tidak sah ke akun dan data pribadi.
2. Memungkinkan pendaftaran, masuk, dan manajemen akun pengguna di aplikasi.
3. Menyediakan mekanisme untuk membedakan pengguna yang berbeda dan mengaitkan aktivitas dengan pengguna tertentu.
4. Menentukan siapa yang dapat mengakses bagian-bagian tertentu dari aplikasi dan apa yang dapat mereka lakukan setelah diotentikasi.
5. Melindungi data sensitif dan fungsi aplikasi dari akses yang tidak sah atau perubahan yang tidak sah.

Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
---
Cookies adalah file yang disimpan pada komputer pengguna saat mereka berinteraksi dengan aplikasi web. Cookies digunakan untuk menyimpan informasi yang dapat digunakan oleh server web untuk mengidentifikasi pengguna dan menyimpan data sesi pengguna. 

Django akan membaca session ID dari cookie, mengidentifikasi sesi yang sesuai, dan mengambil data sesi yang terkait dengan pengguna tersebut. Ini memungkinkan aplikasi untuk menampilkan informasi yang sesuai untuk setiap pengguna. Ketika pengguna logout, Django akan menghapus data sesi dan session ID-nya. 
 
Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
---
Penggunaan cookies dapat aman, tetapi ada risiko potensial yang harus diperhatikan:
1. Cookies yang mengandung informasi sensitif bisa bocor jika tidak diatur dengan baik.
2. Cookies rentan terhadap serangan MITM jika tidak dienkripsi dengan benar.
3. Penyerang dapat mencuri cookies dari perangkat pengguna yang terinfeksi malware.
4. Serangan XSS dapat mencuri cookies atau menjalankan tindakan berbahaya atas nama pengguna.
5. Penyerang yang berhasil mencuri cookies dapat mengambil alih sesi pengguna.
6. Cookies dapat digunakan untuk melacak aktivitas pengguna di berbagai situs web, menimbulkan masalah privasi.
 
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
--- 
Checklist 1 - Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar. 
Hal yang dilakukan:
1. Membuat fungsi `register`, `login_user`, dan `logout_user` pada `views.py`. 
- Fungsi `register` digunakan untuk menampilkan formulir registrasi akun dan membuat akun user ketika datanya di-submit. Fungsi tersebut menggunakan formulir bawaan dari Django dengan mengimpor `UserCreationForm`. 
- Fungsi`login_user` digunakan untuk mengautentikasi user yang ingin login. Pada fungsi ini, kita mengimpor fungsi `authenticate` dan `login` bawaan dari Django. 
- Fungsi `logout_user` berfungsi untuk melakukan mekanismen logout dan me-redirect ke halaman login setelah user logout dari aplikasi. Pada fungsi ini, kita mengimport fungsi `logout` bawaan dari Django.
2. Membuat file `register.html`dan `login.html` pada `main/templates`. Kode pada file tersebut berfungsi untuk menentukan bagaimana tampilan registrasi akun dan login. Untuk logout, kita menambahkan hyperlink tag untuk tombol logout di `main.html`
3. Mengimpor ketiga fungsi yang sudah dibuat ke `url.py` yang ada di `main` dan menambahkan path urlnya ke `urlpatterns`.
4. Membuat restriksi akses halaman main dengan mengimpor `login_required` pada `views.py` dan menambahkannya di atas fungsi `show_main`. `login_required` ini berfungsi untuk mengharuskan user login terlebih dahulu sebelum mereka mengakses halaman web.

Checklist 2 - Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
Hal yang dilakukan:
1. Membuat dua akun melalui web dan kemudian menambahkan tiga item di akun tersebut.

Checklist 3 -  Menghubungkan model Item dengan User.
Hal yang dilakukan:
1. Menambahkan field user untuk class Inventory dan menambahkan relasi antara model `Inventory` dan `User` menggunakan ForeignKey.
2. Di file `views.py`, dalam fungsi `create_product`, gunakan commit=False saat menyimpan objek Product dari form. Setel objek user pada produk sebagai pengguna yang sedang login (request.user).
3. Di file `views.py`, dalam fungsi `show_main`, ambil produk yang terkait dengan pengguna yang sedang login (request.user).
4. Melakukan migrasi model.

Checklist 4 - Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
Hal yang dilakukan: 
1. Di file `views.py`, impor modul datetime, HttpResponseRedirect, dan reverse pada bagian atas file.
2. Dalam fungsi `login_user`, tambahkan kode untuk melakukan login pengguna. Set cookie `last_login` dengan timestamp waktu saat ini.
3. Dalam fungsi `show_main`, tambahkan kode untuk mengambil nilai cookie `last_login` dan menyertakannya dalam konteks.
4. Dalam fungsi `logout_user`, tambahkan kode untuk menghapus cookie `last_login` saat pengguna logout.
5. Di berkas `main.html`, tambahkan kode HTML untuk menampilkan data last login di halaman utama.

Referensi Tugas 4
---
Slide 05: Form, Authentication, Session, and Cookie

https://docs.djangoproject.com/en/4.2/

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Sessions 

https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-3
---

TUGAS 4 PEMROGRAMAN BERBASIS PLATFORM
---
Nama	: Sekar Gandes Dianti

NPM	: 2206082713

Kelas	: PBP D

Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya
---
1. Selector Elemen
   - Manfaat:
   - Tepat digunakan untuk mengaplikasikan gaya atau operasi pada semua elemen dari satu jenis. 
   
   Contoh:
   ```
   p {
    color: blue;
   }
   ```
2. Selector ID
   - Manfaat:
   -  Tepat digunakan untuk mengaplikasikan gaya atau operasi pada elemen dengan ID tertentu.
   
   Contoh:
   ```
   #header {
    background-color: gray;
   }
   ```
3. Selector Kelas
   - Manfaat: memilih elemen berdasarkan kelas yang mereka miliki.
   - Tepat digunakan untuk mengaplikasikan gaya atau operasi pada sekelompok elemen yang karakteristik atau tampilannya sama.
   
   Contoh:
   ```
   .highlight {
    font-weight: bold;
   }
   ```

Jelaskan HTML5 Tag yang kamu ketahui.
---
Penjelasan tentang HTML5 tag yang saya gunakan pada tugas ini adalah sebagai berikut.
- `<div>`: menentukan bagian dalam dokumen
- `<tbody>`: mengelompokkan elemen-elemen `<tr>`
- `<tr>`: mewakili satu baris dalam table
- `<th>`: mendefinisikan table header
- `<title>`: memberikan judul
- `<p>`: menandakan sebuah paragraf atau blok teks
- `<h1>` s.d. `<h6>`: menentukan header 1 sampai header 6
- `<comment>`: memberikan komentar pada dokumen HTML
- `<br>`: membuat baris baru
- `<form>`: menentukan formulir
- `<a>`: mendefinisika hyperlink
- `<label>`: menetapkan label untuk elemen form
- `<input>`: menentukan kontrol input dalam formulir
- `<nav>`:  menandai bagian navigasi pada dokumen HTML
- `<ul>`: membuat list yang tidak terutur
- `<li>`: menandai list item
- `<span>`: menentukan bagian dalam dokumen

Jelaskan perbedaan antara margin dan padding
---
- Margin adalah ruang di sekitar suatu elemen. Margin digunakan untuk memindahkan elemen ke atas atau ke bawah pada halaman serta ke kiri atau ke kanan. Margin tidak memiliki warna background (transparan).
- Padding adalah ruang antara elemen dan konten terkait di dalamnya. Padding menentukan bagaimana elemen terlihat dan ditempatkan di dalam wadah. Padding dapat dipengaruhi oleh warna background.

Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
---
1. Bootstrap
   - Menawarkan desain bawaan
   - Developer hanya tinggal menggunakan komponen-komponen yang sudah ada dengan menambahkan kelas-kelas HTML khusus
   - Ukuran file lebih besar karena fitur bawaan yang disediakan
   - Memiliki sistem grid bawaan
   - Cocok untuk proyek yang kebutuhan desainnya standar
2. Tailwind 
   - Tidak ada desain bawaan, tetapi memberikan kelas-kelas utilitas yang fleksibel. 
   - Penentuan desain (gaya dan tata letak) langsung di dalam HTML
   - Ukuran file lebih kecil dan memberikan kustomisasi yang tinggi
   - Tidak memiliki sistem grid bawaan
   - Cocok untuk developer yang ingin tingkat kostumisasinya tinggi dan desain yang lebih unik.

Dari perbedaan tersebut, kita dapat
- Menggunakan Bootstrap Ketika:
   - Proyek memerlukan implementasi cepat dengan sedikit konfigurasi
   - Tim pengembangan tidak memiliki banyak pengalaman dalam desain antarmuka.
   - Butuh banyak komponen UI yang sudah jadi.
- Menggunakan Tailwind Ketika:
   - Ingin kebebasan desain yang lebih besar.
   - Lebih memilih pendekatan "utility-first" dan ingin kontrol yang lebih detail.
   - Proyek memerlukan performa yang optimal dengan file CSS yang lebih kecil.

Referensi Tugas 5:
Slides Web Design Using HTML5 and CSS3

https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-4 

https://www.digitalocean.com/community/tutorials/how-to-select-html-elements-using-id-class-and-attribute-selectors-in-css

https://www.tutorialspoint.com/html5/html5_tags.htm 

https://www.geeksforgeeks.org/css-padding-vs-margin/ 

---
TUGAS 6 PEMROGRAMAN BERBASIS PLATFORM
---

Nama	: Sekar Gandes Dianti

NPM	: 2206082713

Kelas	: PBP D

Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
---
Asynchronous programming adalah teknik pemrograman yang memungkinkan eksekusi beberapa task tanpa harus menunggu suatu task selesai dilakukan untuk melanjutkan task yang lain. 

Synchronous programming adalah teknik pemrograman di mana ketika suatu task sedang dieksekusi, program harus menunggu task tersebut selesai untuk melanjutkan eksekusi task berikutnya.

Ilustrasi dari asynchronous dan synchronous programming adalah sebagai berikut.
![Alt text](image-1.png)
Sumber gambar: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.scaler.com%2Ftopics%2Fsynchronous-and-asynchronous-javascript%2F&psig=AOvVaw1zlMlsNEfYAug8DX0Vg-nQ&ust=1697236068930000&source=images&cd=vfe&opi=89978449&ved=0CBMQjhxqFwoTCJiA2ZnH8YEDFQAAAAAdAAAAABBW

Perbedaan antara asynchronous dan synchronous programming adalah sebagai berikut. 
![Alt text](image.png)

Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
---
Event-driven programming adalah paradigma pemrograman di mana alur programnya ditentukan oleh events seperti interaksi dari user, sensor output, atau pesan dari program lain atau threads. Pada Event-driven programming, umumnya terdapat main loop yang mendengarkan sebuah event lalu memicu fungsi callback ketika event tersebut terdeteksi.

Dalam tugas ini, event-driven programming diimplementasikan dengan menambahkan tombol "Add New Product" yang memiliki event listener. Ketika tombol diklik, event listener memicu fungsi yang berisi logika untuk menampilkan modal dengan formulir untuk menambahkan item.


Jelaskan penerapan asynchronous programming pada AJAX.
---
Asynchronous programming di AJAX membolehkan pembaruan halaman web tanpa membuat pengguna harus menunggu server merespons. AJAX menggunakan objek XMLHttpRequest untuk mengirim request ke server dan tanggapi responsnya secara asynchronous. Ini berarti skrip JavaScript bisa terus berjalan tanpa terhenti oleh proses komunikasi dengan server. Cara kerja asynchronous ini melibatkan penggunaan fungsi callback yang dijalankan setelah request selesai. Contohnya, fungsi `success` menangani respons yang berhasil, sementara `error` menanggapi kesalahan. Event handling juga digunakan untuk memantau perubahan status request, seperti event `onreadystatechange`, yang memungkinkan developer untuk merespon status permintaan secara dinamis. Dalam pengembangan web dengan jQuery, penggunaan fungsi `$.ajax()` memudahkan penggunaan asynchronous AJAX dengan menyediakan opsi yang dapat diatur, seperti URL, jenis request, dan fungsi callback. Ini memudahkan kita untuk membuat aplikasi web yang responsif dan efisien.

Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
---
Perbandingan antara Fetch API dan library jQuery adalah sebagai berikut.

![Alt text](image-3.png)

Berdasarkan perbandingan tersebut, menurut saya Fetch API lebih baik digunakan dibandingkan jQuery karena lebih ringan, terintegrasi langsung dengan JavaScript modern, dan menggunakan konsep Promise untuk menyederhanakan penanganan asynchronous. Fokus Fetch API pada HTTP request membuatnya lebih sederhana dan tidak memberikan overhead fungsi tambahan yang tidak diperlukan. Selain itu, Fetch API memiliki dukungan browser yang lebih baik karena tersedia di semua browser modern. 

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
---
1. Membuat fungsi `get_product_json` pada `views.py` yang mana fungsi tersebut berfungsi untuk menampilkan data produk pada HTML dengan menggunkan `fetch`
2. Membuat fungsi `add_product_ajax` pada `views.py` yang mana fungsi tersebut berfungsi untuk menambahkan produk baru ke database dengan AJAX
3. Mengimpor kedua fungsi tersebut ke `urls.py` dan menambahkan routing untuk kedua fungsi tersebut.
4. Memperbarui `main.html` untuk mendukung AJAX GET dengam menambahkan blok skrip pada `main.html` dengan fungsi `refreshProducts`. Fungsi ini melakukan permintaan GET asynchronous ke URL yang ditentukan oleh `{% url 'main:get_product_json' %}`. Kemudian, hasil respons JSON diproses dan memperbarui konten HTML untuk menampilkan produk.
5. Menambahkan kode untuk mengimplementasikan modal untuk formulir menambahkan item baru di `main.hmtl`.
6. Menambahkan button "Add New Product by AJAX" untuk menampilkan modal dengan cara berikut ini `<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Add New Product</button>`
7. Menambahkan fungsi `addProduct` pada bagian skirp di `main.html` yang mana fungsi tersebut berfungsi untuk menambahkan data produk ke basis data secara AJAX dan menambahkan fungsi `onclick` pada button "Add New Product" untuk menjalankan fungsi `addProduct`.
8. Menjalankan `python manage.py collectstatic` di terminal

Referensi Tugas 6:
---

https://reintech.io/blog/what-is-event-driven-programming-in-javascript

https://4geeks.com/lesson/event-driven-programming 

https://stackoverflow.com/questions/54229132/can-i-use-fetch-api-in-jquery-datatables

https://www.digitalocean.com/community/tutorials/how-to-use-the-javascript-fetch-api-to-get-data

https://www.geeksforgeeks.org/how-to-use-the-javascript-fetch-api-to-get-data/

https://www.geeksforgeeks.org/how-to-fetch-data-from-json-file-and-display-in-html-table-using-jquery/




