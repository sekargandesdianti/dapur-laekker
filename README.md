TUGAS 2 PEMROGRAMAN BERBASIS PLATFORM 
-------------------------------------
Nama    : Sekar Gandes Dianti

NPM     : 2206082713

Kelas   : PBP D

Tautan aplikasi:
https://dapur-laekker.adaptable.app/main/


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
