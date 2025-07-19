document.addEventListener("DOMContentLoaded", async () => {
    const response = await fetch("http://127.0.0.1:8000/covid/indonesia");
    const data = await response.json();

    const labels = data.map((row) => row.tanggal);
    const kasusBaru = data.map((row) => row.kasus_baru);
    const sembuh = data.map((row) => row.sembuh);
    const meninggal = data.map((row) => row.meninggal);

    const ctx = document.getElementById("covidChart").getContext("2d");
    new Chart(ctx, {
        type: "line",
        data: {
            labels: labels,
            datasets: [
                { label: "Kasus Baru", data: kasusBaru, borderColor: "red", fill: false },
                { label: "Sembuh", data: sembuh, borderColor: "green", fill: false },
                { label: "Meninggal", data: meninggal, borderColor: "gray", fill: false },
            ],
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true },
            },
        },
    });
});
