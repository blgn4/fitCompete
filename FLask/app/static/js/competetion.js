$(function() {
    $('a#gen_stream').bind('click', start_stream)
    console.log("Started!");
    
});

function start_stream() {
    $('#comp').html('')
setInterval(function(){ get_data();}, 300);
}

function get_data(){
        $.getJSON('/_start_competetion', {
          user_id:$('#user_id').val(),
          bmi: $('#Bmi').val(),
          cal: $('#Calories').val(),
          cr: $('#CR').val(),
          fat: $('#Fat').val(),
          floors: $('#Floors').val(),
          hr: $('#HR').val(),
          period: $('#Period').val(),
          speed: $('#Speed').val(),
          steps: $('#Steps').val()
        }, function(data) {
          render_graph(data.result)
        });
        return false;
      };


function render_graph(data) {
 
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

var svg = d3.select(".competetion").append("svg")
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
      .text("Frequency");

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

function getRand(min, max) {
  return Math.random() * (max - min) + min;
}

