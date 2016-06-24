 $(function() {
 	console.log('Hello')
      $('a#find_users').bind('click', function() {
        $.getJSON('/_obtain_users', {
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
          $("#user_list").text(data.result);
        });
        return false;
      });
    });