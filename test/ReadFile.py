
fname = 'SchoolList'
f = open(fname)
line = f.readline()

while line:
    #print line

    #print line.split(None, 1)[0]
    #print line
    #first, _, rest = line.partition(" ")
    lineFixed = ' '.join(line.split())
    first, _, rest = lineFixed.partition(" ")
    print first
    print rest

    schoolID= line.split(None, 1)[0]
    line = f.readline()
f.close()