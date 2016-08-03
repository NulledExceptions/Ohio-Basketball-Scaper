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
        for breaks in soup.findAll('br'):
            breaks.extract()
        for ahref in soup.findAll('a'):
            ahref.extract()
        # print soup
        span_content = soup.find("span", {"class": "schoolAddress"})
        if not span_content:
            print span_content, id
            return None
        ##RAISE EXCEPTION INSTEAD OF RETURNING NONE

        address= span_content.renderContents().replace('\n', '').strip()

        return address


##





