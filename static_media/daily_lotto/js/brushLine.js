var y,y2,color,focus=0,week_ends,yAxis,pline;
function line(){
  var margin = {top: 10, right: 100, bottom: 100, left: 40},
      margin2 = {top: 430, right: 10, bottom: 20, left: 40},
      width = 960 - margin.left - margin.right,
      height = 500 - margin.top - margin.bottom,
      height2 = 500 - margin2.top - margin2.bottom;

  // var formatDate = d3.time.format("%d-%b-%y");
  var parseDate = d3.time.format("%b %Y");

  var x = d3.time.scale()
      .range([0, width]);
  var x2 = d3.time.scale()
      .range([0, width]);

  y = d3.scale.linear()
      .range([height, 0]);
  y2 = d3.scale.linear()
  .range([height2, 0]);

  var xAxis = d3.svg.axis()
      .scale(x)
  	// .tickFormat(d3.time.format("%b %y"))
      .orient("bottom");
  var xAxis2 = d3.svg.axis()
      .scale(x2)
    // .tickFormat(d3.time.format("%b %y"))
      .orient("bottom");

  yAxis = d3.svg.axis()
      .scale(y)
      .orient("left");

  var brush = d3.svg.brush()
      .x(x2)
      .on("brush", brushed);

  var area = d3.svg.area()
      .interpolate("monotone")
      .x(function(d) { return x(d[0]); })
      .y0(height)
      .y1(function(d) { return y(d[1]); });

  var area2 = d3.svg.area()
      .interpolate("monotone")
      .x(function(d) { return x2(d[0]); })
      .y0(height2)
      .y1(function(d) { return y2(d[1]); });

  pline = d3.svg.line()
      .x(function(d) { return x(d.date); })
      .y(function(d) { return y(d.data); });
  var line2 = d3.svg.line()
      .x(function(d) { return x(d[0]); })
      .y(function(d) { return y(d[1]); });

  //     var area = d3.svg.area()
  //     .interpolate("monotone")
  //     .x(function(d) { return x(d.date); })
  //     .y0(height)
  //     .y1(function(d) { return y(d.data); });

  // var area2 = d3.svg.area()
  //     .interpolate("monotone")
  //     .x(function(d) { return x2(d.date); })
  //     .y0(height)
  //     .y1(function(d) { return y2(d.data); });

  // var line = d3.svg.line()
  //     .x(function(d) { return x(d.date); })
  //     .y(function(d) { return y(d.data); });


  var svg = d3.select("body").select("#trend").append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom);
    // .append("g")
    //   .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  svg.append("defs").append("clipPath")
      .attr("id", "clip")
    .append("rect")
      .attr("width", width)
      .attr("height", height);

  focus = svg.append("g")
      .attr("class", "focus")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  var context = svg.append("g")
      .attr("class", "context")
      .attr("transform", "translate(" + margin2.left + "," + margin2.top + ")");

  // d3.tsv("data.tsv", type, function(error, data) {
  //   if (error) throw error;

  week_ends = _.map(weeks,function(week){return getDateOfISOWeek(parseInt(week.slice(5),10), week.slice(0,4))})

  
  x.domain(d3.extent(week_ends));
  // y.domain(d3.extent(y0));
  y.domain([d3.min([].concat(y0,y1)),d3.max([].concat(y0,y1))]);
  x2.domain(x.domain());
  y2.domain(y.domain());

  // console.log(area([week_ends[5],3]))
  color = d3.scale.category10();
  kolor = function(name){
              if(name=="nationa"){
                  return "blue";
              }
              else if(name=="subregional"){
                  return "#555";
              }
              // else if(name=="Fast Moving Average"){
              //     return "green";
              // }
            };

  color.domain(cdom);
  // color.domain(["National","Sub-regional"]);
  // color.domain(["Slow Moving Average","Fast Moving Average"]);
  // color.domain(["Actual","Slow Moving Average","Fast Moving Average"]);

  var data = color.domain().map(function(name){
        // console.log(y0);
        return {
          name: name,
          values: _.map(_.keys(weeks),function(i){
              if(name=="national"){
                  return {date: week_ends[i], data:y0[i]};
              }
              else if(name=="subregional"){
                  // return {date: week_ends[i], data:ys[i]};
                  return {date: week_ends[i], data:y1[i]};
              }
              // else if(name=="Fast Moving Average"){
              //     return {date: week_ends[i], data:yf[i]};
              // }
            })

            
        }
  });


  // []
  // var data = _.zip(week_ends, y0,y1)
  // var data = _.zip(week_ends, y0,y1,y2)

  var data0 = _.zip(week_ends, yxs)
  // var data1 = _.zip(week_ends, y0)
  // var data2 = _.zip(week_ends, y2)
  // console.log(data);	

  // console.log(y0)
  // console.log(week_ends)
  focus.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  focus.append("g")
      .attr("class", "y axis")
      .call(yAxis);
    // .append("text")
    //   .attr("transform", "rotate(-90)")
    //   .attr("y", 6)
    //   .attr("dy", ".71em")
    //   .style("text-anchor", "end")
    //   .text("Price ($)");

  // focus.append("path")
  //   .datum(data0)
  //   .attr("class", "focus area")
  //   .attr("d", line2);

  context.append("path")
      .datum(data0)
      .attr("class", "area")
      .attr("d", area2);

  context.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height2 + ")")
      .call(xAxis2);

  context.append("g")
      .attr("class", "x brush")
      .call(brush)
    .selectAll("rect")
      .attr("y", -20)
      .attr("height", height2 + 20);

  avg_line = focus.selectAll(".avg")
                .data(data)
                .enter().append("g")
                .attr("class","city");

  // console.log(data);
  avg_line.append("path")
              .attr("class","line")
              .attr("d", function(d,i){
                // console.log(_.pluck(d.values,"date"));
                // console.log(d.values[0].data);
                return pline(d.values);})
              .style("stroke", function(d) { return kolor(d.name); });

  // avg_line.append("text")
  //     .datum(function(d) { return {name: d.name, value: d.values[d.values.length - 1]}; })
  //     .attr("transform", function(d) { return "translate(" + x(d.value.date) + "," + y(d.value.data) + ")"; })
  //     .attr("x", 3)
  //     .attr("dy", ".35em")
  //     .text(function(d) { return d.name; });


  function brushed() {
    x.domain(brush.empty() ? x2.domain() : brush.extent());
    focus.select(".area").attr("d", area);
    focus.selectAll(".line").attr("d", function(d){return pline(d.values);});
    focus.select(".x.axis").call(xAxis);
  }




}
function lineUpdate(){
    y.domain([d3.min([].concat(y0,y1)),d3.max([].concat(y0,y1))]);
    y2.domain(y.domain());

    color.domain(cdom);

    var data = color.domain().map(function(name){
          // console.log(y0);
          return {
            name: name,
            values: _.map(_.keys(weeks),function(i){
                if(name=="national"){
                    return {date: week_ends[i], data:y0[i]};
                }
                else if(name=="subregional"){
                    // return {date: week_ends[i], data:ys[i]};
                    return {date: week_ends[i], data:y1[i]};
                }
                // else if(name=="Fast Moving Average"){
                //     return {date: week_ends[i], data:yf[i]};
                // }
              })

              
          }
    });
    // // console.log(data);

    var data0 = _.zip(week_ends, yxs);
    focus.select(".y.axis").call(yAxis)

    avline = focus.selectAll(".city")
                .data(data)

    avline.enter().append("g")
                .attr("class","city");

    d3.selectAll(".line").remove();

    d3.selectAll(".city").append("path")
              .attr("class","line")
              .attr("d", function(d,i){
                // console.log(_.pluck(d.values,"data"));
                // console.log(d.values[0].data);
                return pline(d.values);})
              .style("stroke", function(d) { return kolor(d.name); });

    // avline.transition().attr("d", function(d,i){
    //             return line(d.values);})
    avline.exit().remove()
}

function type(d) {
  d.date = formatDate.parse(d.date);
  d.close = +d.close;
  return d;
}

function getDateOfISOWeek(w, y) {
    var simple = new Date(y, 0, 1 + (w - 1) * 7);
    var dow = simple.getDay();
    var ISOweekStart = simple;
    if (dow <= 4)
        ISOweekStart.setDate(simple.getDate() - simple.getDay() + 1 + 6);
    else
        ISOweekStart.setDate(simple.getDate() + 8 - simple.getDay() + 6);
    return ISOweekStart;
}