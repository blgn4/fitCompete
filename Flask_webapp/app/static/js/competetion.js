function start_stream() {
	$('.competetion').show();
   $.getJSON("/_start_stream",function(data){
      console.log('started streaming')
  });
	setInterval(function(){ get_data();}, 1000);
}

function get_data(){
  $.getJSON("/_get_stats", function(data) {
    console.log(user_selected)
    //render_graph(data.result)
    var str1 = data.result[0][1]
    //console.log(str1)
    var str2 = data.result[1][1]
    //console.log(str2)
    def_data=[0,0,0]
    var dat1 = str1.split(',')
    var dat2 = str2.split(',')
    if (dat1[0] == 1 ) render_table1(dat1)
    else if (dat2[0] == 1 ) render_table1(dat2)
    else render_table1(def_data)

    if (dat2[0] == 0 ) render_table2(dat2)
    else if (dat1[0] == 0 ) render_table2(dat1)
    else render_table2(def_data)
});        
};

function render_table1(data)
{
  console.log(data)
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
  table2 += '<tr>  <th>User_ID:</th> <td> User: '+ user_selected +' </td> </tr>'
  table2 += '<tr> <th> Average Run rate per 3 secs </th> <td> '+ data[1] +'</td> </tr>'
  table2 += '<tr> <th> Pace </th> <td> '+ data[2] +'</td> </tr>'
  table2+='</tbody> </table>'
  $('.box2').html(table2)
}