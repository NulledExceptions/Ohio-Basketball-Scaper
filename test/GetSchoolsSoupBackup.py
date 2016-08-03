from BeautifulSoup import BeautifulSoup
import urllib2



id='1020'

#def GetAddress(id):

url= 'http://schedules.myohsaa.org/SchoolHome/'+str(id)+'/information'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
#print soup
for e in soup.findAll('br'):
    e.extract()
div_content = soup.find("div", {"class": "displaySection"})

address = '\n'.join(str(div_content).split('\n')[6:8])
print address






'''
print div_content
for i in div_content:
    print i
#print str(div_content)
#div = soup.find('div',id="contentDiv")
'''
#print soup.prettify()

#print div