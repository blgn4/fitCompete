$(function() {

   $('.user_list ').on('click' , function(e) {
        console.log(e)
   });

    $('a#gen_stream').bind('click', start_stream)
    
    
});

function start_stream() {
  console.log("Started!");
  
setInterval(function(){ get_data();}, 1000);
}

function get_data(){
        $.getJSON("/_start_competetion", function(data) {
          //render_graph(data.result)
          var str1 = data.result[0][1]
          //console.log(str1)
          var str2 = data.result[1][1]
          //console.log(str2)
          def_data=[0,0,0]
          var dat1 = str1.split(',')
          var dat2 = str2.split(',')
          if (dat1[0] == 1 ) render_table1(data1)
          else if (dat2[0] == 1 ) render_table1(data2)
          else render_table1(def_data)

          if (dat2[0] == 0 ) render_table2(data2)
          else if (dat1[0] == 0 ) render_table2(data1)
          else render_table2(def_data)
          console.log(usr1)
          console.log(usr2)
          
});
        
};

function render_table1(data)
{
  var table1 =  "<table><tbody>";
  table1 += '<tr>  <th>User_ID:</th> <td> User: '+ $('#user_id').val() +' </td> </tr>'
  table1 += '<tr> <th> Average Run rate per 3 secs </th> <td> '+ data[1] +'</td> </tr>'
  table1 += '<tr> <th> Pace </th> <td> '+ data[2] +'</td> </tr>'
  table1+='</tbody> </table>'
    $('.box1').html(table1)
}

function render_table2(data)
{
     var table2 =  "<table><tbody>";
  table2 += '<tr>  <th>User_ID:</th> <td> User: '+ $('#user_id').val() +' </td> </tr>'
  table2 += '<tr> <th> Average Run rate per 3 secs </th> <td> '+ data[1] +'</td> </tr>'
  table2 += '<tr> <th> Pace </th> <td> '+ data[2] +'</td> </tr>'
  table2+='</tbody> </table>'
    $('.box1').html(table2)
}


function render_graph(data) {
  $('#comp').html('')
 console.log(data)
var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 250 - margin.left - margin.right,
    height = 250 - margin.top - margin.bottom;

var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

var svg = d3.select("#comp").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


  x.domain(data.map(function(d) { return d.letter; }));
  y.domain([0, d3.max(data, function(d) { return d.frequency; })]);

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("HR");

  svg.selectAll(".bar")
      .data(data)
    .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.letter); })
      .attr("width", x.rangeBand())
      .attr("y", function(d) { return y(d.frequency); })
      .attr("height", function(d) { return height - y(d.frequency); });
}


function render_graph2(data) { 
  console.log(data)
var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 250 - margin.left - margin.right,
    height = 550 - margin.top - margin.bottom;
var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);
var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .ticks(10, "%");

var svg = d3.select("#b2").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


  x.domain(data.map(function(d) { return d.letter; }));
  y.domain([0, d3.max(data, function(d) { return d.frequency; })]);

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("HR");

  svg.selectAll(".bar")
      .data(data)
    .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.letter); })
      .attr("width", x.rangeBand())
      .attr("y", function(d) { return y(d.frequency); })
      .attr("height", function(d) { return height - y(d.frequency); });
}

function type(d) {
  d.frequency = +d.frequency;
  return d;
}

