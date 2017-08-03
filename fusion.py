import urllib2,math,struct

f = urllib2.urlopen('https://raw.githubusercontent.com/anematode/planet-calculator/master/currentPlanet.dat')
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

epochlength = 330
# (in days)

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
    # data.append((Alist[epoch+1]-Alist[epoch])/timediff)
    
    data.append(EClist[epoch])
    # data.append((EClist[epoch+1]-EClist[epoch])/timediff)
    
    data.append(INlist[epoch] * degToRad)
    # data.append((INlist[epoch+1]-INlist[epoch])/timediff * degToRad)
    
    data.append(OMlist[epoch] * degToRad)
    # data.append((OMlist[epoch+1]-OMlist[epoch])/timediff * degToRad)
    
    data.append(MAlist[epoch] * degToRad)
    data.append(360 / Ylist[epoch] * degToRad)
    
    data.append(Wlist[epoch] * degToRad)
    #data.append((Wlist[epoch+1] - Wlist[epoch])/timediff * degToRad)

with open('out.bin', 'wb') as f:
    for datapoint in data:
        f.write(struct.pack('f', datapoint))
