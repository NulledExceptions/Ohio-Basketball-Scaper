from BeautifulSoup import BeautifulSoup
import urllib2
import csv




url ='http://schedules.myohsaa.org/SchoolHome/102/information'
#url= self.base_url.format(school_id=id)
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

for breaks in soup.findAll('br'):
    breaks.extract()
for ahref in soup.findAll('a'):
        ahref.extract()
#print soup
div_content = soup.find("div", {"id": "schoolAddressCell"})

span_content = soup.find("span", {"class": "schoolAddress"})

print span_content.renderContents().replace('\n', '').strip()








'''
< div
id = "schoolAddressCell" >
< span


class ="schoolAddress"
for e in soup.findAll('br'):
            e.extract()

'''
