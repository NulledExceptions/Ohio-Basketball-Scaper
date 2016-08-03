from BeautifulSoup import BeautifulSoup
import urllib2


url=event_url="http://schedules.myohsaa.org/SchoolHome/102/GetEventInfo?eventId=2818810"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())


div_content = soup.findAll("div", {"class": "infoBox"})
count=0
for a in div_content:
    if count ==2:
     print a.getText().strip()
    count+=1
