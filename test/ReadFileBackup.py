
import string

fname = 'SchoolList'
f = open(fname)
line = f.readline()

while line:
    #print line
    print line.split(None, 1)[0]
    print line
    schoolID= line.split(None, 1)[0]
    line = f.readline()
f.close()