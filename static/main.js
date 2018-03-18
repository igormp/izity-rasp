/*
	fa-spinner fa-spin
	fa-stop
*/

/*function toggleRecording(button) {
	if (document.getElementById("butn").className == "fas fa-play") {
		document.getElementById("butn").className = "fas fa-check"; 
		document.body.style.backgroundColor = "green";
	}
	else{
		document.getElementById("butn").className = "fas fa-play";	
		document.body.style.backgroundColor = "red";
	}
	console.log("hello");
}*/

/*function toggleRecording() {
	document.getElementById("butn").className = "fas fa-spinner fa-spin"; 
	var xhttp = new XMLHttpRequest();
	xhttp.open("GET", "http://localhost:5000", true);
  	xhttp.send();
  	xhttp.onreadystatechange = function() {
		console.log(this.response);
		if (this.response == "true") {
			document.getElementById("butn").className = "fas fa-check"; 
			document.body.style.backgroundColor = "green";
		}
		else{
			document.getElementById("butn").className = "fas fa-times";	
			document.body.style.backgroundColor = "red";
		}
	};
}*/

/*function toggleRecording(){
	document.getElementById("butn").className = "fas fa-spinner fa-spin"; 
	$.get( "http://localhost:5000", function( data ) {
		console.log(data)
		if (data == "true") {
			document.getElementById("butn").className = "fas fa-check"; 
			document.body.style.backgroundColor = "green";
		}
		else{
			document.getElementById("butn").className = "fas fa-times";	
			document.body.style.backgroundColor = "red";
		}
	});
}*/

function toggleRecording(){
	document.getElementById("butn").className = "fas fa-spinner fa-spin"; 
	$.ajax({
            url: "http://localhost:5000",
            type: "GET",
            crossDomain: true,
            success: function (response) {
                console.log(response)
				if (response == "true") {
					document.getElementById("butn").className = "fas fa-check"; 
					document.body.style.backgroundColor = "green";
				}
				else{
					document.getElementById("butn").className = "fas fa-times";	
					document.body.style.backgroundColor = "red";
				}
            },
            error: function (xhr, status) {
            	document.getElementById("butn").className = "fas fa-times";	
				document.body.style.backgroundColor = "red";
                console.log("error");
                console.log(status);
            }
        });
}