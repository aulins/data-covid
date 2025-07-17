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

# Data COVID Project (PostgreSQL + Python)

Project ini digunakan untuk simulasi alur kerja seorang Data Engineer dalam melakukan ekstraksi, transformasi, dan pemuatan (ETL) data COVID-19 ke PostgreSQL, serta membangun REST API menggunakan FastAPI.

---

## 📁 Struktur Folder

data-covid/
├── api/ # API menggunakan FastAPI
│ └── main.py
├── etl/ # Skrip ETL: Load data ke database
│ └── load.py
├── data/
│ └── cleaned/
│ └── covid_cleaned.csv
├── queries/ # Kumpulan kueri SQL eksploratif
├── utils/ # Kode bantu SQL
│ └── drop_all_tables.sql
├── create_tables.sql
├── insert_data.sql
├── .env # Info koneksi database (disembunyikan)
├── .gitignore
├── requirements.txt
└── README.md

---

## 🧰 Tools yang Digunakan

-   **PostgreSQL 17**: Database relasional
-   **SQLAlchemy**: ORM untuk koneksi DB
-   **Pandas**: Transformasi data
-   **FastAPI**: Pembuatan API
-   **python-dotenv**: Membaca file `.env`
-   **psycopg2**: Driver PostgreSQL untuk Python

---

## 🛠️ Instalasi & Setup

1. **Clone repo & buat virtual environment**

```bash
git clone https://github.com/namauser/data-covid.git
cd data-covid
python -m venv venv
venv\Scripts\activate  # Windows
```

2. **Install dependencies**
   pip install -r requirements.txt

3. **Buat file .env**
   Isi dengan URL koneksi database:

```bash
DATABASE_URL=postgresql://postgres:password@localhost:5432/covid_data
```

4. **Jalankan ETL untuk load data ke DB**

```bash
python etl/load.py
```

5. **Menjalankan API**

```bash
uvicorn api.main:app --reload
```

Akses dokumentasi API di:
👉 http://localhost:8000/docs

# Contoh Endpoint API

GET /covid: Menampilkan seluruh data
GET /covid/{country}: Filter data berdasarkan negara

# Tujuan Project

Menunjukkan skill:

-   Transformasi data (ETL)
-   Integrasi ke PostgreSQL
-   Pembuatan API sederhana untuk Data Scientist
-   Struktur file modular untuk proyek data
