import urllib2,math

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
Ylist = []

for i in xrange(1,len(splitData),5):
  currLine = splitData[i-1]
  Tlist.append(float(currLine[:10]))
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
  Ylist.append(float(currLine[57:78]))

data = []

degToRad = math.pi/180

for epoch in xrange(0,len(Tlist),2):
    startTime = Tlist[epoch]
    endTime = Tlist[epoch+1]
    
    data.append(Alist[epoch])
    data.append((Alist[epoch+1]-Alist[epoch])/16384)
    
    data.append(EClist[epoch])
    data.append((EClist[epoch+1]-EClist[epoch])/16384)
    
    data.append(INlist[epoch] * degToRad)
    data.append((INlist[epoch+1]-INlist[epoch])/16384 * degToRad)
    
    data.append(OMlist[epoch] * degToRad)
    data.append((OMlist[epoch+1]-OMlist[epoch])/16384 * degToRad)
    
    data.append(MAlist[epoch] * degToRad)
    data.append(32768 / Ylist[epoch] * 2 * math.pi)
    
    data.append(Wlist[epoch] * degToRad);
    data.append((Wlist[epoch+1] - Wlist[epoch])/16384 * degToRad);

print 'new Float64Array(%s);' % ','.join('%10.10f' % s for s in data)
