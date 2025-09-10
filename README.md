link menuju web yang telah dibuat: https://william-jonnatan-elbolashop.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
a. Membuat virtual environtment terlebih dahulu, menyiapkan dependencies pada berkas requirements.txt, lalu membuat proyek django baru bernama football_shop. Mengkonfigurasikan variabel environtment dengan proyek seperti membuat file .env, .env.prod, dan menambahkan daftar host untuk mengakses web. Mencoba menjalankan server untuk menguji coba
b. Membuat aplikasi baru bernama main dan menambahkannya pada file settings.py yang berada di direktori utama
c. Mengisi pada file models.py dengan mendeklarasikan model Product dan membuat field" yang akan menyimpan isi dari atribut-atribuat yang disebutkan
d. Membuat fungsi show_main yang kan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai dengan context (dictionary yang telah dibuat). Membuat file html pada direktori templates dan mengisinya dengan kode yang akan menampilkan nama aplikasi, nama, kelas
e. Melalukan routing dengan menambahkan fungsi include pada file urls.py di direktori football-shop dan menggunakannya dengan menambahkan rute url menuju main di url_patterns
f. Melakukan deployment melalui PWS

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

3. Jelaskan peran settings.py dalam proyek Django!
file tersebut berisi berbagai pengaturan-pengaturan yanv krusial untuk menjalankan aplikasi yang dibuat. Contohnya terdapat daftar domain/IP yang diperbolehkan mengakses web, menyimpan daftar aplikasi yang digunakan, dan mengatur koneksi dengan database

4. Bagaimana cara kerja migrasi database di Django?
Django akan membandingkan model saat ini dengan struktur database yang digunakan sebelumnya dan mencatat perubahan yang terjadi dengan membuat folder baru bernama migrations. Kemudian Django akan melakukan migrasi ke database dalam bentuk SQL

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, Django memudahkan pemula untuk memahami alur pengembangan perangkat lunak. Hal tersebut dikarenakan komponen inti dalam pengembangan perangkat lunak yang disediakan Django lengkap, seperti tools bawaan, template, dll

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Tidak ada
