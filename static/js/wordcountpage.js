// functions for getting keys and values from obj
function* keys(obj) {
    for (let prop of Object.keys(obj)) 
                                       
        yield prop;
}

function* values(obj) {
    for (let prop of Object.keys(obj)) 
                                       
        yield obj[prop];
}


// displaying word count reuslts
function displayWordCount(result){
	var ctx = document.getElementById("myChart").getContext("2d");
	ctx.canvas.width = 600;
	ctx.canvas.height = 600;
	var options = { responsive: true };
	var labels = Array.from(keys(result));
	var data =  Array.from(values(result));
	var myChart = new Chart(ctx, {
	    type: 'bar',
	    data: {
	        labels: labels,
	        datasets: [{
	            label: 'Word Frequency',
	            data: data,
	            backgroundColor: [
	                'rgba(255, 99, 132, 0.2)',
	                'rgba(54, 162, 235, 0.2)',
	                'rgba(255, 206, 86, 0.2)',
	                'rgba(75, 192, 192, 0.2)',
	                'rgba(153, 102, 255, 0.2)',
	                'rgba(255, 159, 64, 0.2)',
	                'rgba(255, 99, 132, 0.2)',
	                'rgba(54, 162, 235, 0.2)',
	                'rgba(255, 206, 86, 0.2)',
	                'rgba(75, 192, 192, 0.2)',
	                'rgba(153, 102, 255, 0.2)',
	                'rgba(255, 159, 64, 0.2)',
	                'rgba(255, 99, 132, 0.2)'
	            ],
	            borderColor: [
	                'rgba(255,99,132,1)',
	                'rgba(54, 162, 235, 1)',
	                'rgba(255, 206, 86, 1)',
	                'rgba(75, 192, 192, 1)',
	                'rgba(153, 102, 255, 1)',
	                'rgba(255, 159, 64, 1)',
	                'rgba(255,99,132,1)',
	                'rgba(54, 162, 235, 1)',
	                'rgba(255, 206, 86, 1)',
	                'rgba(75, 192, 192, 1)',
	                'rgba(153, 102, 255, 1)',
	                'rgba(255, 159, 64, 1)',
	                'rgba(255,99,132,1)'
	            ],
	            borderWidth: 1
	        }]
	    },
	    options: options
	});
}

function clearChart(){
	// removing old chart
	$('#displaydiv').empty()
	$('#displaydiv'). append('<canvas id="myChart"></canvas><div id="chartLegend" class="chart-legend"></div>')
}


function getWordCount(evt){
	evt.preventDefault();
	// getting chosen word
	clearChart();
	var word = $('#word').val();
	// getting all checked sites
	var sites = []
	$('input[name="sites"]:checked').each(function() {
   	sites.push(this.value);
   	});

   	// sending AJAX request to get word count 
	var data = {word: word, sites: JSON.stringify(sites)};
	$.get('/word_count.json', data, displayWordCount)
}


function getFreqObj(){
    // sending AJAX request to get word frequescy object for this site
    var url = $('#hiddendiv').val();
    var data = {url: url}
    $.get('/word_frequency.json', data, displayWordCount)
}

// event listeners
$(document).ready(getFreqObj)
$('#word-count').on('submit', getWordCount);