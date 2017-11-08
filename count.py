from operator import itemgetter
import pickle


EXCLUDE_LIST = ['advertisement', 'buzzfeed', 'times','after', 'should', 'video', 'videos']


def count_words(site):
	"""returns most commong words from particular site"""
	# get html
	text = site.html
	count = {}
	# get count for each word and add to count dict
	text = [word for word in text.split(" ") if word != '']
	for word in text:
		word = word.lower().rstrip('.,":;!?')
		count[word]= count.get(word, 0) + 1
	# turning dict into list of tuples and sorting
	word_list = [(x, y) for x,y in count.items() if len(x) > 4 and x not in EXCLUDE_LIST]
	word_list = sorted(word_list, key=itemgetter(1))[-25:]
	# creating dict out of most common words
	frequency_dict = {x:y for x, y in word_list}
	
	return frequency_dict


def count_one_word(word, sites):
	"""returns how often a particular word appears in chosen sites"""

	counts = {}
	word = word.lower()
	# count how often word shows up in each site and adds to count dict
	for site in sites:
		count = 0
		text = site.html
		for w in text.split(" "):
			w = w.lower().rstrip('.,":;!?')
			if w == word:
				count += 1
		counts[site.site_name] = count

	return counts