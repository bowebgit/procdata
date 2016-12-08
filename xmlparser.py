from urllib.request import urlopen
from xml.etree.ElementTree import parse

url = 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml' 
u = urlopen (url)
doc = parse(u)

for item in doc.iterfind('channel/item'):
	#process items under the channel element
	title = item.findtext('title').encode('ascii', 'ignore')
	date = item.findtext('pubDate')
	link = item.findtext('link')
	print(title)
	print(date)
	print(link)
	print()