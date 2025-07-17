-- Ganti 'DKI Jakarta' sesuai kebutuhan
SELECT * FROM kasus_covid
WHERE wilayah = 'DKI Jakarta'
ORDER BY tanggal;
