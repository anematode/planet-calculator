# planet-calculator
To find positions of planets and asteroids and such...

Valid dates: JD -1930633.5 to JD 5373483.5 (BC 9999 Mar 20 (20 March 9999 BCE) to AD 9999 Dec 31 (31 December 9999 CE) = 7304117 days)

# Storage of orbital elements for planets (or other solar-orbiting objects, for that matter)

Epoch: To get appropriate orbital elements, take time t in JD, add 1930633.5, divide by 32768, and take the floor

Semi-major Axis: store axisH and axisDay (semi-major axis, semi-major axis / day) as semi-major axis since epoch

Eccentricity: store eccH and eccDay (eccentricity, eccentricity shift / day) as eccentricity since epoch

Inclination: store inclH and inclDay (inclination, inclination shift / day) as inclination since epoch

Longitude of the Ascn. Node: store ascnH and ascnDay (longitude, longitude shift / day) as longitude of ascending node since epoch

Mean Anomaly: store anomalyH and anomalyDay (angle, angle shift / day) as mean anomaly since epoch

Argument of Perihelion: store periH and periDay (angle, angle shift / day) as argument of perihelion since epoch

These 12 numbers, when retrieved with an associated time t, should be able to give reasonably accurate (but more importantly, extremely quick) ephemeris data. We will store them in a Float64 array like so:

[axisH, axisDay, eccH, eccDay, inclH, inclDay, ascnH, ascnDay, anomalyH, anomalyDay, periH, periDay, ... ]

Over our desired time period, this gives ceil(7304117 / 32768) orbits * 12 data points / orbit * 8 bytes / orbit = 21408 bytes / body, which is not too bad.

Note: all angles should be expressed in radians, all lengths should be expressed in AU.

# The Formula

Let t be the time, in JD (Julian Date, i.e. time since January 1, 4713, negative if before). We get the **current orbital elements** for the epoch as follows (pseudocode):

```
currentEpoch = floor((t + 1930633.5) / 32768)
axisH = dataArray[currentEpoch]
axisDay = dataArray[currentEpoch+1]
.
.
.
periH = dataArray[currentEpoch+10]
periDay = dataArray[currentEpoch+11]
```

To get the time relative to the epoch and correct elements, we do this:

```
adjustedTime = t - currentEpoch
axis = axisH + adjustedTime * axisDay
ecc = eccH + adjustedTime * eccDay
incl = inclH + adjustedTime * inclDay
ascn = ascnH + adjustedTime * ascnDay
anomaly = anomalyH + adjustedTime * anomalyDay
peri = periH + adjustedTime * periDay
```

The computation of the actual position, in (x, y, z) coordinates (where the XY plane is the J2000 ecliptic), is more complex.

Our first step is solving **Kepler's equation**, an important equation in orbital dynamics. We need to compute the **eccentric anomaly** of the orbit using the eccentricity and mean anomaly, but that requires a root approximation method. We proceed like so:

```
eccAnomaly = anomaly
while (true) {
    deltaEcc = (eccAnomaly - ecc * sin(eccAnomaly) - anomaly) / (1 - ecc * cos(eccAnomaly))
    eccAnomaly -= deltaEcc
    if (deltaEcc < 1e-9) {
        break
    }
}
```

At the end of this process, eccAnomaly is the eccentric anomaly, the solution E to the equation M = E - ecc * sin(E). This is the most computationally expensive part of the orbital calculation process.

Our next step is computing the **true anomaly**. The formula is like so:

```
trueAnomaly = 2 * atan2(sqrt(1 + e) * sin(E / 2), sqrt(1 - e) * cos(E / 2))
```

With the trueAnomaly, we can calculate the orbital position relatively easily:

```
x = r * (Math.cos(ascn) * Math.cos(peri + trueAnomaly) - Math.sin(ascn) * Math.sin(peri + trueAnomaly) * Math.cos(incl));
y = r * (Math.sin(ascn) * Math.cos(peri + trueAnomaly) + Math.cos(ascn) * Math.sin(peri + trueAnomaly) * Math.cos(incl));
z = r * (Math.sin(incl) * Math.sin(peri + trueAnomaly));
```

That's our process!
