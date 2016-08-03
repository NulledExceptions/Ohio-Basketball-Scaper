import urllib2
from BeautifulSoup import BeautifulSoup

##PAGEINATE ME
schoolId = '100'
url ='http://schedules.myohsaa.org/SchoolHome/' + schoolId + '/ListPrintView/Basketball/Boys/Varsity/3-31-2015/3-5-2016'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
#print soup
##table_content = soup.find("table", {"class": "printCalendarScheduleTable"})
##for match in soup.findAll('span', {"class": ""}):
##    match.unwrap()

#datetable_content = soup.findAll("span", {"class": ""})
#print datetable_content
#for a in datetable_content:
##    print a.renderContents()


#table_content = soup.find("table",attrs= {"class": "printCalendarScheduleTable"})

table_content = soup.findChildren('tr')
##my_table = table_content[8]

for a in table_content:
    sch=a.findChildren('td')
    for a in sch:
        ##print a.renderContents().strip()
        span=a.findChildren('span')
        if span:
            print span[0].renderContents().strip()
        else:
            print a.renderContents().strip()
#sch = table_content.find('td')
#text = sch.renderContents().strip()


'''
sch=table_content.findChildren('td')
for a in sch:
    print a.renderContents().strip()
#print sch


#mySchedule = table_content.find("td").renderContents().strip()

##print table_content
##print mySchedule





for e in soup.findAll('br'):
    e.extract()
div_content = soup.find("div", {"class": "displaySection"})
'''