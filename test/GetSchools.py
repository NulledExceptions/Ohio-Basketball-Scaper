from htmldom import htmldom
dom = htmldom.HtmlDom()
#or
dom = htmldom.HtmlDom( "http://schedules.myohsaa.org/SchoolHome/100/information" )
print dom

elem = dom.find( "div[id=contentDiv]" )
print elem.html()


# Getting p element from html data
p = dom.find( "p" )
# You can print html content using "html" method of HtmlNodeList object
print( p.html() )

# Getting all elements
all = dom.find( "*" )
print (all.html() )
