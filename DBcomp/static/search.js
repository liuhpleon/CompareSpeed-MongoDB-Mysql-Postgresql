var myurl = "http://localhost:5000/"; 
var load = $("#loading"); 
var unload = $("#unloading");

function send_query(data){
	$.ajax({
		url: myurl,
		type: 'POST',
		dataType: 'json',
		data: data,
		beforeSend: function(){
		    load.show();
	        unload.hide();
		},
	})
	.done(function(result) {
		load.hide();
		unload.show();
		
		var mysql = JSON.parse(result.mysql);
		$("#mysql_time").text(mysql.time);
		$("#mysql_count").text(mysql.count);
		
		var postgresql = JSON.parse(result.postgresql);
		$("#postgresql_time").text(postgresql.time);
		$("#postgresql_count").text(postgresql.count);
		var mongodb = JSON.parse(result.mongodb);
		$("#mongodb_time").text(mongodb.time);
		$("#mongodb_count").text(mongodb.count);
		//console.log(mysql.time);
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
	
}

$("#submit").click(function(event) {
	/* Act on the event */
	var datasize = $("#data_size").val();
	/*
    var startprice = $("#start").val();
    var endprice = $("#end").val();
    */
    var word = $("#word").val();
    data = {
    	"word":word,
    	/*
    	"startprice":startprice,
    	"endprice":endprice,
    	*/
    	"datasize":datasize
    }
    send_query(data);
});

load.hide();
unload.show();