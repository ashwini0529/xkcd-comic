import urllib2
import urllib
from bs4 import BeautifulSoup

url = "http://xkcd.com/"
for i in range(1,20):
	new_url = url+str(i)
	soup = BeautifulSoup(urllib2.urlopen(new_url).read())
	for each_div in soup.findAll('div',{'id':'ctitle'}):
		    print each_div.get_text()
		    for div in soup.findAll('div', attrs={'id':'comic'}):
		    	imageSource = div.find('img')['src']
		    	imageSource = "http://"+imageSource[2:]
		    	print imageSource
		    	urllib.urlretrieve(imageSource, each_div.get_text()+".jpg")