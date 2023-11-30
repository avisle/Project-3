function getData(){
   let selector = d3.select("#countyDropDown");

   d3.json("http://127.0.0.1:5000/api/v1.0/counties").then((data) => {
   const county_arr=[];
   for (let i = 0; i<data.length; i++){
    county_arr.push(data[i].county);
   }
   var ele = document.getElementById("countyDropDown");
   for (let i = 0; i<county_arr.length; i++){
     var opt = document.createElement("OPTION");
     opt.text=county_arr[i];
     opt.value=county_arr[i];
     ele.options.add(opt);
    }
})
}

getData();