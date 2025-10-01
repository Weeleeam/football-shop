link menuju web yang telah dibuat: https://william-jonnatan-elbolashop.pbp.cs.ui.ac.id/

TUGAS 3:
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Karena sebuah platform membutuhkan mekanisme pertukaran data agar data-data penting dalam platform tersebut tidak hilang ataupun tertukar. Mekanisme data delivery yang baik juga membuat data aman, konsisten, dan tidak hilang saat terjadi down pada server.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya pribadi JSON lebih baik karena lebih mudah untuk dibaca. Itu juga menjadi salah satu alasan mengapa JSON lebih populer dibandingkan XML. Selain itu, parser JSON umumnya lebih cepat dan hampir tersedia di semua bahasa. 

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method tersebut untuk memvalidasi data yang didapat dari form apakah sudah bener atau belum. Method tersebut dibutuhkan untuk memfilter data-data yang tidak diinginkan, mencegah error, dan masalah mengenai keamanan.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token dibutuhkan untuk melindungi aplikasi platform dari serangan Cross-Site Request Forgery. Jika kita tidak menambahkan csrf_token akan memberikan dampak negatif pada user dan platform. Penyerang dapat membuat halaman berbahaya yang mengirim request ke aplikasi seperti mengganti password dan server bisa mengganggap request tersebut berasal dari user. 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
a. Menambahkan fungsi" show baru pada file views.py agar dapat menampilkan data-data produk
b. Menambahkan beberapa url pattern yang sesuai agar fungsi" baru pada views dapat ditampilkan
c. Untuk membuat halaman yang dapat menambahkan produk baru dan melihat detailnya, saya memodifikasi file main.html pada subdirektori templates pada direktori main dengan kode yang sesuai, termasuk membuat button Detail
d. Halaman form dapat dibuat dengan membuat file html baru di tempat yang sama dengan main yang baru saja dimodifikasi. Dalam kasus saya, saya membuat file create_product yang akan memuat halaman yang meminta input detail-detail produk yang ingin ditambahkan
e. Sama seperti pembuatan halaman form, saya membuat file html baru yang bernama product_detail dan mengisinya deng kode yang akan menampilkan berbagai detail tentang produk sesuai dengan yang telah ditambahkan sebelumnya 

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan? tidak ada

link screenshot: https://drive.google.com/drive/folders/1r_XS3FNCj4Pq128NCe78zAFkNWsEUPgP?usp=sharing


TUGAS 4:
1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
Merupakan form bawaan dari Django yang akan memproses data login pengguna. Form ini akan mencocokan username dan password (2 field utama) yang dikirim dengan yang ada di database. Kelebihannya adalah dilengkapi fitur keamanan bawaan Django, mudah dan cepat digunakan, serta proses validasi yang standar. Kekurangannya adalah kostumisasi form yang terbatas dimana form ini hanya menyediakan 2 field utama yaitu username dan password.

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Secara garis besar, autentifikasi mengecek identitas yang sedang ingin login ke platfrom sedangkan otorisasi mengecek hal apa saja yang dapat dilakukan atau diakses oleh pengguna. Dalam autentifikasi, Django menyediakan model User yang sudah terdapat 2 field utama yaitu username dan password, selain itu Django juga menyediakan form dan views untuk proses login bawaan yang bisa dipakai. Dalam otorisasi, Django membuat model memiliki permission/izin dasar seperti add, change, delete, view, serta kita juga dapat kostum "izin" sendiri. Selain itu, pada tugas kali juga memakai decorators (contohnya @login_required) yang diimplementasikan pada method show_main dan create_product pada file views.py yang dimana hanya pengguna yang login saja yang dapat view tersebut.

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Session lebih aman daripada cookies karena data disimpan dalam server sehingga pengguna tidak bisa melihat atau memodifikasi data secara langsung, sedangkan cookies dapat dilihat dan dimodifikasi yang membuatnya kurang aman. Di sisi lain, cookies tidak membebani server karena datanya disimpan pada browser sedangkan session menyimpan data pada server yang menambah beban pada memori setiap sesi saat pengguna sedang aktif.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
secara default, cookies tidak aman karena menyimpan data pada browser yang bisa menyebabkan cookie theft dimana penyerang dapat mencuri cookie sesi pengguna dan mendapatkan hak akses akun. Namun, Django menangani hal ini dengan tidak menyimpan data sesi pada cookie melainkan menyimpan ID sesi yang dibuat secara acak yang membuatnya lebih aman karena data yang asli berada di server. 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
a. Mengimport library yang sesuai, membuat fungsi baru pada views.py yaitu register, dan membuat file html register untuk menampilkan dan menjalankan proses register akun
b. Membuat fungsi login pada views.py dan membuat file html login untuk menampilkan serta menjalankan proses login
c. Memodifikasi file main.html dnegan menambahkan button logout yang akan mengalihkan ke tampilan login
d. Menambahkan path yang sesuai untuk fungsi-fungsi yang telah dibuat seperti register, login, dan logout pada urls.py di urlpatterns
e. Mengimport decorator login_required dan menambahkannya pada beberapa fungsi yang membutuhkan akses untuk menampilkannya
f. Mendaftarkan cookie last_login pdad respone dan menambahkannya pada variabel context, kemudian mengubah fungsi logout agar bisa menghapus cookie last_login setelah logout
g. Menghubungkan model Product dengan user dengan cara menambahkan library yang sesuai dan menambahkan field user pada model Product agar setiap produk yang ditambahkan mempunyai hubungan atau terikat dengan user yang menambahkannya

TUGAS 5:
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Browser akan menentukan pengambilan CSS selector berdasarkan urutan prioritas yang disebut spesifisitas, dimana CSS selector dengan skor spesifisitas tertinggi akan diambil dahulu. Urutannya adalah:
a. Inline styles
b. ID Selector
c. Class, Attribute, dan Pseudo-class Selectors
d. Element dan Pseudo-element Selectors
terdapat 1 lagi yaitu important yang memiliki prioritas paling tinggi namun penggunaannya harus dihindari

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
User experience dan penjangkauan audines menjadi alasan mengapa responsive design sangat penting. Pengalaman pengguna yang sering berganti perangkat dalam mengakses situs akan membuat situs yang tidak responsif sulit digunakan. Selain itu responsive design memungkinkan kita menjangkau audiens atau pengguna dengan perangkat apapun. Contoh aplikasi yang sudah menerapkan responsive design adalah Tokopedia dan yang belum adalah SIAK-NG. Jika kita mmengakses tokopedia dari berbagai perangkat, tampilan yang ada sudah disesuaikan dengan perangkat yang kita pakai. Sedangkan SIAK-NG jika kita mengaksesnya melalui perangkat mobile seperti handphone, tampilan yang ditunjukkan tidak sesuai jadi kita perlu menzoom untuk menekan beberapa button yang ukurannya kecil.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin berfungsi untuk mengatur jarak antara elemen/konten di luar border.
Border berfungsi sebagai garis batas visual dari suatu elemen.
Padding berfungsi untuk mengatur jarak antara elemen/konten dengan garis batasnya.
Contoh Implementasi:
padding: 20px ---> memberikan ruang untuk konten sebesar 20px
border: 1px ---> menambahkan garis batas 1px
margin: 30px ---> memberikan jarak antara konten dengan konten yang lainnya sebesar 30px

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya
flex box drancang untuk menata, meratakan, dan mendistribusikan ruang di antara item-item dalam sebuah kontainer, baik secara horizontal maupun vertikal, tetapi tidak keduanya sekaligus. Kegunaannya untuk mengatur antar (baris atau kolom) komponen yang digunakan.
grid layout dirancang untuk mengatur tata letak halaman yang lebih kompleks. Kegunaannya untuk mengatur konten-konten yang berada pada halaman.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
a. Membuat fungsi baru pada views.py yaitu edit_product dan delete_product untuk mnegedit dan menghapus product yang dibuat
b. Membuat file html baru yaitu edit_product.html dan mengisinya dengan kode yang sesuai untuk mengatur tampilan saat edit produk, lalu menambahkan path yang sesuai pada urls.py untuk fungsi edit dan delete
c. Memodifikasi fungsi main.html pada bagian loop list product dengan menambahkan button edit dan delete.
d. Menambahkan script cdn tailwind di bagian head pada base.html
e. Membuat navigation bar dengan membuat file html baru pada direktori yang sama dengan base.html dan menambahkan navbar pada main.html
f. Menambahkan middleware WhiteNoise dan mengkonfigurasikan variabel STATIC_ROOT, STATICFILES_DIRS, dan STATIC_URL pada settings.py
g. Membuat file baru yaitu global.css pada direktori static/css/ dan folder baru yaitu image pada direktori static/.
h. Mengkonfigurasikan global.css agar tampilan form yang memiliki class form-style dan membuat semua input memiliki lebar penuh, padding, border abu-abu, dan sudut melengkung.
i. Melalukan styling pada halaman home dan membuat file html baru pada direktori templates yang akan menampilkan card product sekaligus menstylingnya
j. Melakukan styling pada halaman login, register, create_product, edit_product, dan detail_product
