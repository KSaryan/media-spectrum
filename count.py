from operator import itemgetter
import pickle


EXCLUDE_LIST = ['advertisement', 'buzzfeed', 'times', 'new', 'york', 'fox', 'news', 'that', 'that', 'what', 'this', 'with', 'from', 'after']


def count_words(key):
	texts = pickle.load( open( "html_info.py", "rb" ) )
	text = texts[key]
	count = {}
	for word in text.split(" "):
		word = word.lower().rstrip('.,":;!?')
		count[word]= count.get(word, 0) + 1
	word_list = [(x, y) for x,y in count.items() if len(x) > 4 and x not in EXCLUDE_LIST]
	word_list = sorted(word_list, key=itemgetter(1))[-25:]
	frequency_dict = [{"text": x,"size":y * 5} for x, y in word_list]
	frequency_dict = {x:y for x, y in word_list}
	return frequency_dict


def count_one_word(word, sites):
	texts = pickle.load( open( "html_info.py", "rb" ) )
	counts = {}
	word = word.lower()
	for site in sites:
		count = 0
		text = texts[site]
		for w in text.split(" "):
			w = w.lower().rstrip('.,":;!?')
			if w == word:
				count += 1
		counts[site] = count

	return counts

