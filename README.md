# Data COVID Project (PostgreSQL)

Project ini digunakan untuk simulasi transformasi dan query data COVID-19 berbasis SQL.

## Struktur Tabel

Tabel utama: `kasus_covid`

| Kolom      | Tipe         | Keterangan        |
| ---------- | ------------ | ----------------- |
| id         | SERIAL       | Primary key       |
| wilayah    | VARCHAR(100) | Nama kota/daerah  |
| tanggal    | DATE         | Tanggal laporan   |
| kasus_baru | INTEGER      | Kasus baru harian |
| sembuh     | INTEGER      | Jumlah sembuh     |
| meninggal  | INTEGER      | Jumlah meninggal  |

## Cara Pakai

1. Jalankan `utils/drop_all_tables.sql` untuk reset.
2. Jalankan `create_tables.sql` untuk membuat struktur tabel.
3. Jalankan `insert_data.sql` untuk mengisi data dummy.
4. Jalankan file di folder `queries/` untuk eksplorasi data.

Pastikan sudah terkoneksi ke database PostgreSQL dengan nama `covid_data`.
