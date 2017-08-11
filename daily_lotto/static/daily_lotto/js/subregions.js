//globals
var width, height, projection, path, graticule, svgmap,uganda;
// selected_subregion;
var clicked;
var subRegions;
function setMap() {
    	//width = 960,height = 500;
    	//width = 700,height = 500;
        width = 250, height=200;

	//Define map projection [lon,lat]
	projection = d3.geo.mercator()
	  .rotate([0,0])  
	  .center([32.25,1.4]) 
	  .translate([width/2, height/2])
	  .precision(0.1)
	  .scale([100*20]);

	path = d3.geo.path()
	    .projection(projection);

	
	svgmap = d3.select("#map").append("svg")
	   .attr("width", width)
	   .attr("height", height);
	loadMapData();  // let's load our data next

}

function loadMapData() {
    d3.json("data/ugsubRegion.json", function(error, ug) {
        uganda= ug;
        // console.dir(ug)
        
        drawMap();   // once all files are loaded, call the processData function passing
                            // the loaded objects as arguments
   })

}

setMap(); 


function drawMap() {

    subRegions = svgmap.selectAll(".region")   // select districts objects (which don't exist yet)
      .data(topojson.feature(uganda, uganda.objects.uganda).features)  // bind data to these non-existent objects
      .enter().append("path") // prepare data to be appended to paths
      .attr("class", "region") // give them a class for styling and access later
      .attr("d", path); // create them using the svg path generator defined above
    
      d3.selectAll(".region-label").style("visibility", "visible")
      d3.select('#map').selectAll('path').on("click",
        function(d){
             clicked=d
             selected_subregion = d.properties.subRegion
             selectRegion(d.properties.subRegion);
             genCdom();
             loadSubregionData(printData);
//              d3.select('#map').selectAll('path').attr("class", function(d){ return d===clicked? "active": "region";})
// //                        d3.select(this).style("fill",'#eee'); 
//              d3.select('#selected-regionx').text(d.properties.subRegion)
//              selected_subregion = d.properties.subRegion
      });
}

function selectRegion(name){
  d3.select('#map').selectAll('path').attr("class", function(d){ return d.properties.subRegion==name ? "active": "region";})                       
  // d3.select(this).style("fill",'#eee'); 
  d3.select('#selected-regionx').text(name)
}
