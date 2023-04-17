function createCharts(forecast) {
    var dates = [];
    var temps = [];
    var precip = [];
    var uv = [];
  
    forecast.forEach(function(day) {
      dates.push(day.date);
      temps.push(day.temp);
      precip.push(day.precip);
      uv.push(day.uv);
    });

    var tempChart = new Chart(document.getElementById('temperature-chart'), {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
            data: temps,
            fill: false,
            borderColor: 'red'
            }]
        },
        options: {
            plugins: {
                legend: {
                    display: false
                }
            },
            responsive: true,
            title: {
            display: true,
            text: 'Temperature Forecast'
            }
        }
    });
  
    var precipChart = new Chart(document.getElementById('precipitation-chart'), {
        type: 'bar',
        data: {
        labels: dates,
        datasets: [{
            data: precip,
            backgroundColor: 'blue'
        }]
        },
        options: {
            plugins: {
                legend: {
                    display: false
                }
            },
        responsive: true,
        title: {
            display: true,
            text: 'Precipitation Forecast'
        }
        }
    });
  
    var uvChart = new Chart(document.getElementById('uv-chart'), {
        type: 'line',
        data: {
        labels: dates,
        datasets: [{
            data: uv,
            fill: false,
            borderColor: 'green'
        }]
        },
        options: {
            plugins: {
                legend: {
                    display: false
                }
            },
        responsive: true,
        title: {
            display: true,
            text: 'UV Forecast'
        }
        }
    });
  }