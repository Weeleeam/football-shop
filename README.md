link menuju web yang telah dibuat: https://william-jonnatan-elbolashop.pbp.cs.ui.ac.id/

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
