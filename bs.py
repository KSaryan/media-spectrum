
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib
from operator import itemgetter


EXCLUDE_LIST = ['times', 'new', 'york', 'fox', 'news', 'that', 'that', 'what', 'this', 'with', 'from']
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)


def count_words(url):

	html = urllib.urlopen(url).read()
	count = {}
	for word in (text_from_html(html)).split(" "):
		word = word.lower()
		count[word]= count.get(word, 0) + 1
		word_list = [(x, y) for x,y in count.items() if len(x) > 4 and x not in EXCLUDE_LIST]
		word_list = sorted(word_list, key=itemgetter(1))
		frequency_list = [{"text": x,"size":y} for x, y in word_list]
	print frequency_list


count_words('https://www.nytimes.com/')