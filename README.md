# GameHunt

## Nama Anggota
- Oscar Ryanda Putra - 2306217765
- Aliefa Alsyafiandra Setiawati Mahdi - 2306221056	
- Priscilla Natanael Surjanto - 2306152153	
- Vincent Davis Leonard Tjoeng - 2306275014	
- Utandra Nur Ahmad Jais - 2306152443	
- Rahma Dwi Maghfira - 2306245794	

## Deskripsi
Temukan kaset game PS4 favoritmu dengan mudah di Jakarta melalui GameHunt, web app pencarian kaset game paling lengkap yang siap membawamu ke dunia gaming tanpa batas! Tak perlu lagi berkeliling kota untuk mencari toko yang menyediakan game impianmu—cukup buka GameHunt, dan biarkan kami membantu kamu menemukan toko terdekat yang menjual game PS4 terbaru maupun game klasik yang langka.

Dengan antarmuka yang sederhana dan cepat, GameHunt memudahkan pencarian berdasarkan lokasi, harga, dan stok yang tersedia. Aplikasi ini juga dilengkapi fitur ulasan dari pengguna lain serta informasi tentang promosi atau diskon di berbagai toko di Jakarta, sehingga kamu bisa mendapatkan kaset game terbaik dengan harga yang paling terjangkau.

Nikmati pengalaman berbelanja game PS4 tanpa repot, langsung dari genggamanmu! Dengan GameHunt, misi mencari game PS4 favoritmu jadi lebih seru dan praktis!

Jadi, tunggu apa lagi? Jelajahi dunia game PS4 dengan mudah dan cepat bersama GameHunt!

## Modules

### 1. Order
Modul ini menangani seluruh proses pembelian game oleh pengguna. Setiap kali pengguna membeli game dari toko tertentu, data transaksi akan dicatat dalam model `Order`, yang mencakup informasi seperti game yang dibeli, toko asal, harga, dan status pesanan. Modul ini juga memungkinkan pengguna untuk melihat riwayat pembelian mereka, melakukan pembayaran, dan mendapatkan konfirmasi setelah transaksi berhasil. Dengan ini, pengguna dapat membeli game dari berbagai toko dengan harga yang bervariasi, dan sistem akan mencatat detail transaksi secara akurat.

### 2. Review
Modul ini mengatur proses ulasan terhadap pesanan yang telah diselesaikan. Pengguna dapat memberikan ulasan dan peringkat untuk setiap order setelah pembelian. Model `Review` akan menyimpan data ulasan terkait pesanan tertentu, termasuk komentar pengguna dan rating. Modul ini memungkinkan pengguna lain untuk membaca pengalaman orang lain sebelum memutuskan membeli game yang sama. Dengan adanya ulasan terkait kualitas produk dan layanan toko, calon pembeli dapat memperoleh pandangan yang lebih baik sebelum melakukan pembelian.


### 3. Search and Price Sorting Module
Modul ini memfasilitasi pencarian game dan pengurutan daftar toko berdasarkan harga. Saat pengguna mencari game tertentu, modul ini menampilkan hasil pencarian yang sesuai dan menyediakan fitur untuk mengurutkan daftar toko yang menjual game tersebut berdasarkan harga, dari harga terendah hingga tertinggi atau sebaliknya. Dengan ini, pengguna dapat menemukan toko yang menawarkan harga terbaik secara efisien.

### 4. Stock Management
Modul ini memungkinkan setiap toko untuk mengelola ketersediaan stok game yang mereka jual. Model `Stock` menyimpan informasi mengenai jumlah stok untuk setiap game di toko tertentu. Toko dapat memperbarui stok melalui dashboard mereka, dan pengguna dapat melihat status stok secara *real-time* ketika memilih game dari berbagai toko. 

### 5. User Authentication Module
Modul ini memastikan bahwa semua pengguna harus terautentikasi sebelum mengakses fitur-fitur yang memerlukan identitas pengguna. Ini mencakup proses login, logout, dan registrasi, serta pengaturan ulang kata sandi. 

## Sumber initial dataset kategori utama produk

Dapat dilihat di link <a href ="https://docs.google.com/spreadsheets/d/1K3VhjmiJ9hOLFPaEudecgRv3C4AyJoByI_fX6XXbYR0/edit?pli=1&gid=0#gid=0"> ini </a>

## Role atau Peran Pengguna

Terdapat beberapa peran atau role pengguna yang dapat diakses dengan fitur-fitur yang berbeda

1. Admin

Admin adalah pengguna dengan akses penuh untuk mengelola seluruh konten dan pengguna dalam aplikasi. Mereka memiliki wewenang untuk menjaga kualitas data, ulasan, dan informasi yang ada di platform.

Fitur yang bisa diakses :

  * Mengelola informasi game yang dijual.
  * Mengelola informasi toko 
  * Menghapus ulasan atau komentar yang tidak sesuai dengan kebijakan aplikasi.

2. Registered User

Pengguna terdaftar adalah pengguna yang telah membuat akun di GameHunt dan dapat menikmati semua fitur dasar seperti mencari game, memberikan ulasan, dan membeli game.

Fitur yang Bisa Diakses:

  * Mencari game berdasarkan judul.
  * Melihat daftar toko yang menjual game tertentu dan membandingkan harga.
  * Melihat detail game dan ulasan dari pengguna lain.
  * Memberikan rating dan ulasan setelah membeli game.