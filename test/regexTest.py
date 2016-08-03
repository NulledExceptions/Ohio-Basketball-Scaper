from BeautifulSoup import BeautifulSoup
import urllib2
url =
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
div_content = soup.find("div", {"class": "displaySection"})div class="accordionTeamSchedule