import urllib2

f = urllib2.urlopen('https://raw.githubusercontent.com/anematode/planet-calculator/master/mercurytest.dat')
data = f.read()

splitData = data.split('\n')

EClist = []
INlist = []
OMlist = []
Wlist = []
MAlist = []
Alist = []
Tlist = []

for i in xrange(1,len(splitData),5):
  currLine = splitData[i-1]
  Tlist.append(float(currLine[:10])-2451545.0)
  currLine = splitData[i]
  EClist.append(float(currLine[5:26]))
  INlist.append(float(currLine[57:78]))
  currLine = splitData[i+1]
  OMlist.append(float(currLine[5:26]))
  Wlist.append(float(currLine[31:52]))
  currLine = splitData[i+2]
  MAlist.append(float(currLine[31:52]))
  currLine = splitData[i+3]
  Alist.append(float(currLine[5:26]))
  
