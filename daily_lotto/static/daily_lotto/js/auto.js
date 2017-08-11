//globals
var width, height, projection, path, graticule, svg, attributeArray = [], currentAttribute = 0, playing = false, inFull,d44, j=0,myTimer=setTimeout(0), blinkd;
var selected_week = '2015W45';
var inFull={'p1':'Proportion of ANC1 with unknown status tested',
 'p2':'Proportion of HIV+ women not yet on ART initiated',
 'p3':'Proportion of women tested positive out of those tested',
'reportingRate':'Reporting Rate',
'AdjReportingRate':'Non Reporting Score'};
var districtsToLoopThrough; 
var percentage_indicators = ['reportingRate','p1','p2','p3'];
pseudo_indicators2 = {"reportingRate":"Reporting rate","p1":"Testing rate","p2":"Initiation rate","p3":"Positivity rate"};

function init() {
  _.each(_.keys(pseudo_indicators2),function(indicator){
    $("<button />", {"class":"btn btn-default "+indicator}).text(pseudo_indicators2[indicator]).appendTo($("#indicators div"));
  });
  setMap();
  animateMap();             
}

function setMap() {
    	//width = 960,height = 500;
    	//width = 700,height = 500;
        // width = 864, height=700;
        width = 600, height=700;

	//Define map projection [lon,lat]
	projection = d3.geo.mercator()
	  .rotate([0,0])  
	  .center([32.25,1.4]) 
	  .translate([width/2, height/2])
	  .precision(0.1)
	  .scale([300*20*(7/8)]);
//	  [200*18]
	/*var projection = d3.geo.albers()
	    .center([0, 55.4])
	    .rotate([4.4, 0])
	    .parallels([50, 60])
	    .scale(1200*3)
	    .translate([width / 2, height / 2]); */

	path = d3.geo.path()
	    .projection(projection);

	/*var svg = d3.select("body").append("svg")
	    .attr("width", width)
	    .attr("height", height);*/


	/*width = 960, height = 580;  // map width and height, matches 

	projection = d3.geo.eckert5()   // define our projection with parameters
	.scale(170)
	.translate([width / 2, height / 2])
	.precision(.1);

	path = d3.geo.path()  // create path generator function
	.projection(projection);  // add our define projection to it*/

	//graticule = d3.geo.graticule(); // create a graticule
	
	
        // append a svg to our html div to hold our map
	svg = d3.select("#map").append("svg")
	   .attr("width", width)
	   .attr("height", height);

	/* svg.append("defs").append("path")   // prepare some svg for outer container of svg elements
	.datum({type: "Sphere"})
	.attr("id", "sphere")
	.attr("d", path);

	svg.append("use")   // use that svg to style with css
	.attr("class", "stroke")
	.attr("xlink:href", "#sphere"); */

        // use path generator to draw a graticule
//	svg.append("path").datum(graticule).attr("class", "graticule").attr("d", path);

	/*
	d3.json("Uganda.json", function(error, ug) {
	svg.selectAll('.states')
		.data(topojson.feature(ug, ug.objects.Ugandasimpl).features)
		.enter()
		.append('path')
		.attr('class', 'states')
		.attr('d', path)
		.on('mouseover', function(d){
			//var name = d.properties.id;
			var name =d.properties.name
			return document.getElementById('name').innerHTML=name;
		 });
	});
	*/
	loadData();  // let's load our data next

}

function loadData() {
    
    queue()   // queue function loads all external data files asynchronously 
    .defer(d3.json, "data/uganda-subcounties.json")  //.defer(d3.json, "world-topo.json")  // our geometries
    .defer(d3.json,"data/districtJson.json")  //.defer(d3.csv, "districtsRandom.csv")  // and associated data in csv file
    .defer(d3.json, "newData3/"+selected_week+".json")
    .await(processData);   // once all files are loaded, call the processData function passing
                            // the loaded objects as arguments
   
}

// var  data2visualise =['p1','p2','p3','reportingRate','AdjReportingRate']
var  data2visualise =['p1','p2','p3','reportingRate']
var weeklydata;
function processData(error,ug,districtDatax,weeksdata) {
    
    var data = districtDatax;
    // console.log(data)
    weeklydata=weeksdata;
    districtList = _.keys(data['data'])
    weekmetadata = data['weekmetadata']
    districtmetadata = data['fieldMetadata']

    generateWorst();
    var posindicators=[]
    for(ind in data2visualise){
        indicatorpos = _.indexOf(districtmetadata, data2visualise[ind])
        posindicators.push(indicatorpos)
    }
//    console.log(posindicators)

    posweek =  _.indexOf(weekmetadata, selected_week)

    allindicators=[]
    for(idistrict in districtList){

        datax = data['data'][districtList[idistrict]][posweek]
        indicatorsx=[]
        for(ix in posindicators){
            indicatorsx.push(datax[posindicators[ix]])
        }
//    #     allindicators.append(data['data'][district][posweek])
        allindicators.push(indicatorsx)
    }
    
//    console.dir(allindicators)
    
    districtData =allindicators
    
    
  // function accepts any errors from the queue function as first argument, then
  // each data object in the order of chained defer() methods above
  var districts = ug.objects.districts.geometries;  // store the path in variable for ease
  attributeArray = data2visualise;
  for (var i in districts) {    // for each geometry object
    for (var j in districtData) {  // for each row in the CSV
      if(districts[i].properties.name == districtList[j]) { //districtData[j]['District']) {   // if they match
//        console.log(districts[i].properties.name )
//        console.log(districtList[j])
        for(var k in data2visualise){ // districtData[i]) {   // for each column in the a row within the CSV
//            console.log(k)
            if(k != 'District' && k != 'name') {  // let's not add the name or id as props since we already have them

            if(data2visualise[k]=='AdjReportingRate'){
                districts[i].properties[data2visualise[k]] = 100*(1-Number(districtData[j][k]))  // add each CSV column key/value to geometry object
                }else{
                    districts[i].properties[data2visualise[k]] = Number(districtData[j][k])
                }
          } 
        }
        break;  // stop looking through the CSV since we made our match
      }
    }
  }
  $("."+[attributeArray[currentAttribute]]).addClass("active");
  d3.select('#clock').html(inFull[attributeArray[currentAttribute]]);  // populate the clock initially with the current year
  drawMap(ug);  // let's mug the map now with our newly populated data object
}

function generateWorst(){
    //console.dir(weeklydata)
    //curweekdata[‘districtlevel’][‘data’][‘districtname’][‘districtvals’][indicator]
    // console.log(weeklydata)
    var metadata = weeklydata['districtLevel']['districtmetadata']
    var alldata=[]
    districtList=_.keys(weeklydata['districtLevel']['data'])
    for (i in districtList){
        district = districtList[i]
        districtvals = weeklydata['districtLevel']['data'][district]['districtvals']
        districtObject = _.object(_.zip(metadata,districtvals))
        districtObject['district']=district
        alldata.push(districtObject)
    }
    // console.dir(alldata)  
    var cf = crossfilter(alldata);
    //var  data2visualise =['p1','p2','p3','reportingRate','AdjReportingRate']
    listings = {}
    for (i in data2visualise ) {
        indicator=data2visualise[i]
        var byindicator =cf.dimension(function(d){return d[indicator];});
        if(indicator=='p3'){
             listings[indicator]=byindicator.top(5) 
        }else{
            listings[indicator]=byindicator.bottom(5) 
        }
        
    }
    // console.log(listings)
}

function drawMap(ug) {
    g_district = svg.selectAll("g")
      .data(topojson.feature(ug, ug.objects.districts).features)
      .enter()
      .append("g")
      .attr("class","g-district")

    g_district.append("path")
      .attr("class", "district")
      .attr("id", function(d) { return "code_" + d.properties.id; }, true)
      .attr("d", path);

    // svg.selectAll(".district")   // select districts objects (which don't exist yet)
    //   .data(topojson.feature(ug, ug.objects.districts).features)  // bind data to these non-existent objects
    //   .enter().append("path") // prepare data to be appended to paths
    //   .attr("class", "district") // give them a class for styling and access later
    //   .attr("id", function(d) { return "code_" + d.properties.id; }, true)  // give each a unique id for access later
    //   .attr("d", path); // create them using the svg path generator defined above

   
    d3.selectAll('.district')  // select all the districts
    .attr('fill', function(d) {
//        console.log(attributeArray[currentAttribute])
//        console.log(attributeArray)
//        console.log(d.properties)
       // console.log(currentAttribute)
        return color(d.properties[attributeArray[currentAttribute]],attributeArray[currentAttribute]);
    })
    .style('fill-opacity',0.65);

    districtsToLoopThrough = ['LUWERO','GULU', 'ABIM','NTUNGAMO','WAKISO'];
    
//    blinkd();
//    var bi = setInterval(blinkd, 1000)
    tout = function(){
        // myTimer = setTimeout(blinkd,3500);
        myTimer = setInterval(blinkd,3500);
    }
    
    // tout()
    blinkd = function(){
      // console.log(j)
        if(playing == false) {
          d44.transition().duration(500)
              .style("stroke", "#FFF");

          d44 = ""
          clearInterval(myTimer);
          return;
        }
        updateNotice();
      // console.log(districtsToLoopThrough[j])
        if(j>0) {
//            d44.transition().duration(0);
            d44.transition().duration(500)
              .style("stroke", "#FFF");

            d44 = ""

        }

//        if(j>=4) clearInterval(bi);
        if(j<5) {
          d44 = d3.selectAll('.district').filter(function (d, i) { return d.properties.name == districtsToLoopThrough[j];});
          d3.selectAll('.district').sort(function (a, b) { return (a.properties.name == districtsToLoopThrough[j])?1:-1;})
          // .text("d1");
  //        repeat(d44)
           d44.transition().duration(500)
          .style("stroke", "#000");

          $("#district-list ul").find(".active").removeClass("active");
          $("#district-list li").eq(j).addClass("active");
          j++;
          // myj = j;
          // repeat(d44);
          // tout();
        } else {
          $("#district-list").hide();
          clearInterval(myTimer);
        }
        
    }

    function capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
    }

    function updateNotice(){
      if(j>4){
        var ind_dat = listings[attributeArray[currentAttribute]][0]
        _.each(_.keys(ind_dat), function(key){
            $("#"+key).text("");
        });
       $("#hover-district").text("District")
       return;
     }
      var ind_dat = listings[attributeArray[currentAttribute]][j]
      _.each(_.keys(ind_dat), function(key){
          $("#"+key).text(Math.round(ind_dat[key]));
      });
      $("#hover-district").text(capitalizeFirstLetter(ind_dat.district)+" District")
    }
    
//    var textLabels = text
//                 .attr("x", function(d) { return d.cx; })
//                 .attr("y", function(d) { return d.cy; })
//                 .text( function (d) { return "( " + d.cx + ", " + d.cy +" )"; })
//                 .attr("font-family", "sans-serif")
//                 .attr("font-size", "20px")
//                 .attr("fill", "red");
//    districtsToLoopThrough.forEach(function(dist){
//        var d44 = d3.selectAll('.district').filter(function (d, i) { return d.properties.name == dist;});
//        d3.selectAll('.district').sort(function (a, b) { return (a.properties.name == dist)?1:-1;});
////        console.log(d44)
//        repeat(d44)
//        setTimeout(kill(d44),2000)
//    });
//    
//    function kill(ad){
//        return function(){
//        ad.transition();
//        }
//    }
//    console.log(_.map(ug.objects.districts.geometries, (function(g){ return g.properties.name})))
//    console.log(topojson.feature(ug, ug.objects.districts).features.forEach(function(r){
//        return r.properties.name
//    }))
//    console.log(d3.map(d3.selectAll('.district'),function(d){ console.log(d)}) )
    // d3.map(d3.selectAll('.district'),function(d){ console.log(d)}) 
//    d44.transition()
//        .duration(1000)
//        .style("opacity", 0);
//    repeat();
//    d3.transition('.district')
//    .delay(function(d, i) { return i / n * duration; });
    
    function repeat(currentD){
//        if (currentD.properties.name === undefined) return;
//        console.log(currentD)
        currentD.transition()
        .duration(50)
        .style("stroke", "#FFF")
        .each("end", function(){
            if(myj==j){
              d3.select(this)
                .transition()
                .duration(10)
                .style("stroke", "#000")
                .each("end",function(){
                    repeat(currentD);
                });
            }
        });
//        d44.transition()
//        .duration(10)
//        .style("opacity", 1)
//        .each("end",repeat);
    };

}

var color = function(di,indicator){
            if(indicator=='p1' || indicator=='reportingRate'||indicator=='p2' ||indicator=='AdjReportingRate' ){

                if(di>100){ return "#FF0000";}//Red "rgb(255,0,0)"
                else if (di>=90){ return "#008000";}//Green "rgb(0,128,0)"
        				else if(di>=50){ return "#FFA500";}//Orange "rgb(255,165,0)"
                else if (di<50){ return "#FF0000";}//Red "rgb(255,0,0)"
            } else if(indicator=='p3'){
      				if(di>=5){ return "#FF0000";} //Red "rgb(255,0,0)"
      				else if(di>=3){  return   "#FFA500";} //Orange "rgb(255,165,0)"
      				else if(di>=0){ return "#008000";} //Green "rgb(0,128,0)"
			     }

}
    
function sequenceMap() {
    // d3.selectAll('.g-district text').remove();
    // d3.selectAll('.g-district').append("text").text(function(d){
    //   return Math.round(d.properties[attributeArray[currentAttribute]]);
    // })
    // .attr("x",function(d){ return path.centroid(d)[0]})
    // .attr("y",function(d){ return path.centroid(d)[1]});

    d3.selectAll('.district')
      // .transition()  //select all the districts and prepare for a transition to new values
      //.delay(700)
      // .duration(0)  // give it a smooth time period for the transition
      .attr('fill', function(d) {
        // console.log(d.properties.name+"-"+d.properties[attributeArray[currentAttribute]]+"-"+attributeArray[currentAttribute]+"-"+color(d.properties[attributeArray[currentAttribute]],attributeArray[currentAttribute]));
        return color(d.properties[attributeArray[currentAttribute]],attributeArray[currentAttribute]);  // the end color value
    });
    districtsToLoopThrough = _.map(listings[attributeArray[currentAttribute]], function(obj){
        return obj.district;
    });
    // console.log(districtsToLoopThrough);

    $("#district-list li").each(function(i){
      $(this).text(districtsToLoopThrough[i])
    });
    $("#district-list").show();
    j=0;
    blinkd();
    tout()
     
}

function animateMap() {

  var timer;  // create timer object]
  d3.select('#play')  
    .on('click', function() {  // when user clicks the play button
      if(playing == false) {  // if the map is currently playing
        // currentAttribute -=1;
        playing = true;
        sequenceMap();
        d3.select('#clock').html(inFull[attributeArray[currentAttribute]]);  // update the clock
        timer = setInterval(function(){   // set a JS interval
          if(currentAttribute < attributeArray.length-1) {  
              currentAttribute +=1;  // increment the current attribute counter
          } else {
              currentAttribute = 0;  // or reset it to zero
          }
          sequenceMap();  // update the representation of the map 
          // console.log(attributeArray)
          $("#indicators div").find(".active").removeClass("active");
          $("."+[attributeArray[currentAttribute]]).addClass("active");
          d3.select('#clock').html(inFull[attributeArray[currentAttribute]]);  // update the clock
        }, 20000);
      
        d3.select(this).html('stop');  // change the button label to stop
        // playing = true;   // change the status of the animation
      } else {    // else if is currently playing
        clearInterval(timer);   // stop the animation by clearing the interval
        d3.select(this).html('play');   // change the button label to play
        playing = false;   // change the status again
      }
  });
}


window.onload = init();  // magic starts here