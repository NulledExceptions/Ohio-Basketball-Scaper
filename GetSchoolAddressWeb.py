from BeautifulSoup import BeautifulSoup
import urllib2
school_list_url= 'http://www.ohsaa.org/members/school_id.htm'

page = urllib2.urlopen(school_list_url)
soup = BeautifulSoup(page.read())


each_table = soup.find('table')
for table in each_table:
    #print table
    print '******'
    #each_td= each_table.findChildren('tr')
    each_td = each_table.find('tr')
    #print each_td
    #print each_td.renderContents().strip()
    for td in each_td:
        each_tr=td.find('td')
        #print each_tr.renderContents()
        print each_tr
        print '*******'
        if each_tr=='7th &amp; 8thGrade Schools':
            break
        #print each_tr.renderContents().strip()



'''

from BeautifulSoup import BeautifulSoup
import urllib2
school_list_url= 'http://www.ohsaa.org/members/school_id.htm'

page = urllib2.urlopen(school_list_url)
soup = BeautifulSoup(page.read())


each_table = soup.findAll('table')
for table in each_table:
    #print table
    print '******'
    each_td= each_table.find('tr')
    #print each_td
    #print each_td.renderContents().strip()
    for td in each_td:
        each_tr=td.find('td')
        #print each_tr.renderContents()
        print each_tr.getText()
        print '*******'
        #print each_tr.renderContents().strip()

'''
'''
for b in soup:
    try:
        sch = list(b.findChildren('tr'))
    except:
        continue
    for td in b:
        hs_td = b.findChildren('tr'),{'class':"xl22"}
        print hs_td
        print '*******'


for td in b:
        #print td.renderContents().strip()
        print td
            '''