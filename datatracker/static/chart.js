var labels = [ "North American Sales", "European Sales", "Japanese Sales", "Other Sales"];

var data = {
    labels: labels,
    datasets: [{
        label:'My first dataset',
        backgroundColor: 'rgb(255, 99, 132)',
        borderColor: 'rgb(255,99,132)',
        data: [0, 10, 5, 2, 20, 30, 45]
    }]
    };

var config = {
    type: 'line',
    data,
    options: {}
};