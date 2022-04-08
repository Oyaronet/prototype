let myChart = document.getElementById('myChart').getContext('2d');
let lessonsChart = new Chart(myChart, {
    type: 'line', // bar, horizontalBar, pie, doughnut, rader
    data: {
        labels: ['Monday', 'Tuesday','Wednesday','Thursday','Friday'],
        datasets: [{
            label: 'Missed',
            data: [4,5,2,6,22]
        }]
    },
    options: {}
})