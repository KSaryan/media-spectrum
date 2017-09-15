
function displayWordCount(result){
	for(item in result){
		$('#wcresults').append('<div>' + item+': '+result[item] +'</div>')
	};
}

function getWordCount(evt){
	evt.preventDefault();
	var word = $('#word').val();
	var sites = []
	$('input[name="sites"]:checked').each(function() {
   	sites.push(this.value);
   	});
	var data = {word: word, sites: JSON.stringify(sites)};
	$.get('/word_count.json', data, displayWordCount)

}
$('#word-count').on('submit', function(evt){$('#wcresults').empty();
											getWordCount(evt);});