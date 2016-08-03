from BeautifulSoup import BeautifulSoup
import urllib2
import csv

class SchoolAddressScraper(object):
    def __init__(self):
        self.base_url='http://schedules.myohsaa.org/SchoolHome/{school_id}/information'

    def get_address(self,id):

        url= self.base_url.format(school_id=id)
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page.read())
        #print soup
        for e in soup.findAll('br'):
            e.extract()
        div_content = soup.find("div", {"id": "schoolAddressCell"})

        ##address = '\n'.join(str(div_content).split('\n')[6:8])

        return address





'''
< div
id = "schoolAddressCell" >
< span


class ="schoolAddress"

'''
