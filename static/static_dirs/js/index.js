
const tempSpace = document.getElementById('tempValue')
let time = 0
let dataPoints = []
let chart;

window.setInterval(function(){
    $.get("http://127.0.0.1:8000/getSensorData", function(tempData, status){
        console.log(tempData);
        tempSpace.innerHTML = tempData.temperature;
    });

    $.get("http://127.0.0.1:8000/liveGraph", function(tempArray, status){
        console.log(tempArray);
        console.log(time)
        let x = [];
        let p = 0;
        $.each(tempArray, function(key, value){
            p = p + 1;
            x.push(p*10);
        })
        console.log(dataPoints)
        console.log("x", x)
        chart = new Chart(document.getElementById("line-chart"),{
            type: 'line',
            data: {
                labels: x,
                datasets: [{ 
                    data: tempArray,
                    label: "Temperature change",
                    borderColor: "#3e95cd",
                    fill: false
                }]
            }
        });
    });
    time += 10
    chart.destroy();
}, 10000);



