SELECT 
    wilayah,
    SUM(kasus_baru) AS total_kasus,
    SUM(sembuh) AS total_sembuh,
    SUM(meninggal) AS total_meninggal
FROM kasus_covid
GROUP BY wilayah;


SELECT * FROM kasus_covid;

SELECT * FROM covid_stats LIMIT 1;
