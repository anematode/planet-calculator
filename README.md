# planet-calculator
Finds positions of planets and asteroids and such

Valid dates: JD -1930633.5 to JD 5373483.5 (BC 9999 Mar 20 to AD 9999 Dec 31 = 7304117 days)

Storage of orbital elements for planets besides Earth

Epoch: To get appropriate orbital elements, take time t in JD, add 1930633.5, divide by 32768, and take the floor
Semi-major Axis: store axisH and axisDay (semi-major axis, semi-major axis / day) as semi-major axis since epoch
Eccentricity: store eccH and eccDay (eccentricity, eccentricity shift / day) as eccentricity since epoch
Inclination: store inclH and inclDay (inclination, inclination shift / day) as inclination since epoch
Longitude of the Ascn. Node: store ascnH and ascnDay (longitude, longitude shift / day) as longitude of ascending node since epoch
Mean Anomaly: store anomalyH and anomalyDay (angle, angle shift / day) as mean anomaly since epoch
Argument of Perihelion: store periH and periDay (angle, angle shift / day) as argument of perihelion since epoch

These 12 numbers, when retrieved with an associated time t, should be able to give reasonably accurate (but more importantly, extremely quick) ephemeris data.

# The Formula
