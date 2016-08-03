
#http://schedules.myohsaa.org/SchoolHome/100/Month/Basketball/Boys/Varsity/1/2016/#



fname = 'SchoolList'
f = open(fname)
line = f.readline()

while line:
    #print line

    #print line.split(None, 1)[0]
    #print line
    #first, _, rest = line.partition(" ")


    line_formatted = ' '.join(line.split())
    schoolID, _, school_name = line_formatted.partition(" ")


##http://schedules.myohsaa.org/SchoolHome/100/ListPrintView/Basketball/Boys/Varsity/3-31-2015/3-5-2016
months=['11/2015/','12/2015/','1/2016/','2/2016/']
days=['30','31','31','29']
base_url ='http://schedules.myohsaa.org/SchoolHome/' + schoolID + '/Month/Basketball/Boys/Varsity/'+months[0]