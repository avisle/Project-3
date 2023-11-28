
function init(){
    
        var trace1 = {
            x: xData,
            y: yData
        };

        var data = [trace1];

        var layout = {
            title: "County % Vacc Vs Season"
        }

        Plotly.newPlot("plot", data, layout);
}

init();