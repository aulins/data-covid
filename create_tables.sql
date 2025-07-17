CREATE TABLE IF NOT EXISTS kasus_covid (
    id SERIAL PRIMARY KEY,
    wilayah VARCHAR(100),
    tanggal DATE,
    kasus_baru INTEGER,
    sembuh INTEGER,
    meninggal INTEGER
);
