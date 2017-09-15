var url;

function getScreenShot(result){

	var src = "/static/img/thumbnail_" + url + "?" + result;
	$('#screenshot-display-div').prepend($('<img>',{id:'theImg',src: src}));
}

function getTime(){
	url = this.dataset.url
	$.get('/get_time', getScreenShot);
}



$('.npbtn').on('click', getTime)

