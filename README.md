# Google Maps Scraper

Google Maps Scraper adalah alat otomatisasi berbasis Python yang dirancang untuk mengambil data dari Google Maps, seperti tautan lokasi, informasi bisnis, dan nomor kontak. Proyek ini cocok untuk kebutuhan pengumpulan data lokasi secara efisien.

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
