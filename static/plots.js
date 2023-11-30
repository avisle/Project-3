

function optionChanged(countyName){
    let selector = d3.select("countyDropDown");
    var url = (`http://127.0.0.1:5000/api/v1.0/flu_data/${countyName}`);
    d3.json(url).then(function(data) {
        let fluseason = []
        let vacc = []
        for (i = 0 ; i< data.length; i++){
            fluseason.push(data[i].flu_season)
            vacc.push(data[i].percentage_healthcare_professionals_vaccinated)
         }
        var trace = {
            x: fluseason,
            y: vacc,
            type: 'line'
        }

        var data = [trace];

        var layout = {
            title: "County Healthcare Professionals % Vacc Vs Season",
            xaxis: {
                title: 'Flu Season'
            },
            yaxis: {
                title: 'Healthcare Professionals % Vaccinated'
                }
            }

            Plotly.newPlot("plot", data, layout);
     })
}

//get the selected county value in the DropDown options
var dropDown=document.getElementById("countyDropDown");
var selectedCounty=dropDown.selectedCounty;

optionChanged(selectedCounty);


