function getData(){
    let selector = d3.select("selDataset");

    d3.json("http://127.0.0.1:5000/api/v1.0/counties").then((data) => {
   //console.log(data);
   //console.log(data[0].county);
   //var county_arr = Object.keys(data);
   const county_arr=[];
   for (let i = 0; i<data.length; i++){
    //console.log(data[i].county);
    county_arr.push(data[i].county);
   }
   //let result = "";
   var ele = document.getElementById("countyDropDown");
   for (let i = 0; i<county_arr.length; i++){
     var opt = document.createElement("OPTION");
     opt.text=county_arr[i];
     opt.value=county_arr[i+1];
     ele.options.add(opt);
    }
   //document.getElementByName("county").innerHTML=county_arr;
   
  // for(let i in data) {
  //  county_arr.push([i,data[i]]);
  //  console.log(county_arr[i]);
  // }
   //for(const [key, value] of Object.entries(data)) {
   // county_arr.push([`${key}`,`${value}`]);
    //console.log(county_arr[i]);
    //}
    //console.log(result)
    //console.log(selector);
    //return result
})
}

getData();