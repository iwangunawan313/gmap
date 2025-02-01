  <div align="center" style="margin-top: 0;">
  <h1>🤖 Google Maps Scraper 🤖</h1>
  </div>

<p align="center">
Google Maps Scraper adalah alat otomatisasi berbasis Python yang dirancang untuk mengambil data dari Google Maps, seperti tautan lokasi, informasi bisnis, dan nomor kontak. Proyek ini cocok untuk kebutuhan pengumpulan data lokasi secara efisien.
</p>

<p align="center">
  <a href="https://gitpod.io/#https://github.com/iwangunawan313/gmap">
    <img alt="Run in Gitpod" src="https://gitpod.io/button/open-in-gitpod.svg" />
  </a>
</p>

## 🎯 Fitur Utama

- **Scrape Lokasi Bisnis**: Mengambil tautan lokasi dari hasil pencarian Google Maps.
- **Filter Data**: Hanya mengambil data yang relevan berdasarkan kata kunci.
- **Retry Mechanism**: Mencoba kembali scraping untuk data yang gagal hingga 3 kali.
- **Blokir Gambar & CSS**: Mengoptimalkan scraping dengan menonaktifkan gambar dan CSS.
- **Ekspor Data ke Excel**: Menyimpan hasil scraping dalam file `.xlsx` dengan nama file sesuai query pencarian.
- **Kompatibel dengan Proxy**: Mendukung penggunaan proxy untuk menghindari deteksi bot.

## 🛠️ Persyaratan

- **Python 3.10+**
- **Google Chrome** dan **ChromeDriver** yang sesuai
- Pustaka Python:
  - `selenium`
  - `openpyxl`
  - `random`
  - `time`

## 🚀 Cara Menggunakan

1. **Kloning Repository**
   ```bash
   git clone https://github.com/iwangunawan313/gmap.git
   cd gmap


2. **Install Dependencis**
   ```bash
   pip install -r requirements.txt
   
3. **Jalankan Scraper**
   ```bash
   python main.py

Hasil Scraping Data akan diekspor ke folder output dengan format query.xlsx. Contoh: warung bakso cirebon.xlsx.

⚙️ Konfigurasi Opsional
Blokir Gambar & CSS Anda dapat mengaktifkan fitur blokir gambar dan CSS untuk mempercepat scraping. Pastikan opsi ini sudah diatur dalam main.py.

4. **Menggunakan Proxy Tambahkan proxy pada chrome_options:**
   ```bash
   chrome_options.add_argument("--proxy-server=http://your-proxy-address:port")
  
📌 Catatan Penting
Gunakan scraping secara bertanggung jawab dan patuhi kebijakan Google.
Jangan lakukan scraping secara agresif untuk menghindari pemblokiran.

🤝 Kontribusi
Kontribusi sangat diterima! Silakan ajukan pull request atau buka issue untuk ide pengembangan lebih lanjut.

📜 Lisensi
Proyek ini dilisensikan di bawah MIT License.
