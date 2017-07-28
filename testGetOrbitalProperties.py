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
    data.append(360 / Ylist[epoch] * degToRad)
    
    data.append(Wlist[epoch] * degToRad)
    data.append((Wlist[epoch+1] - Wlist[epoch])/16384 * degToRad)

import math

def shorten(f):
  if (f == 0):
    return '0'
  if (abs(f) < 1):
    normal = ('%10.10f' % f).replace(' ','').strip('0')
    if (normal[0] == '-' and normal[1] == '0'):
      normal = '-' + normal[2:]
    exponent = int(math.floor(math.log10(abs(f))))
    multiplyBy = f/(10 ** exponent);
    if (multiplyBy % 1 == 0.0):
      multiplyBy = int(multiplyBy)
    else:
      multiplyBy = round(multiplyBy,10+exponent)
    new = str(multiplyBy) + 'e' + str(exponent)
    if (len(new) > len(normal)):
      if (normal == '.' or normal == '-.'):
        return '0'
      return normal
    else:
      return new
  return str(f)

print 'new Float64Array([%s]);' % ','.join(shorten(s) for s in data)
