
// displaying word count reuslts
function displayWordCount(result){
	$('#wc-resultstable').show();
	for(item in result){
		$('#wcresults').append(`<tr>
	                           <td>${item}</td>
	                           <td>${result[item]}</td>
	                           </tr>`)
	};
}

function getWordCount(evt){
	evt.preventDefault();

	// getting chosen word
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

// event listener 
$('#word-count').on('submit', function(evt){$('#wcresults').empty();
											getWordCount(evt);});
$(document).ready(function(){$('#wc-resultstable').hide();})