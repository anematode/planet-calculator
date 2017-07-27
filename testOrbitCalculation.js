// Note: data is for Mercury at instant of J2000

var a = 3.870982121840369E-01;  // Semi-major axis
var e = 2.056302929816634E-01;  // Eccentricity
var i = 7.005014140699190E+00 * Math.PI/180;  // Inclination
var W = 4.833053733981040E+01 * Math.PI/180;  // Longitude of Ascending Node

var M = (1.747958829506606E+02) * Math.PI/180;  // Mean anomaly
var w = 2.912428280936123E+01 * Math.PI/180;  // Longitude of perihelion

var E = M;  // Eccentric anomaly

// Newton's method: find root of M - E + e * sin(E)
while (true) {
  var dE = (E - e * Math.sin(E) - M)/(1 - e * Math.cos(E));
  E -= dE;
  if (Math.abs(dE) < 1e-9) break;
}

// True anomaly
var v = Math.atan2(Math.sqrt(1 + e) * Math.sin(E / 2), Math.sqrt(1 - e) * Math.cos(E / 2)) * 2;

// Distance to center body
var r = (a * (1 - e * e)) / (1 + e * Math.cos(v));

// x, y, z coords relative to J2000 ecliptic
var x = r * (Math.cos(W) * Math.cos(w + v) - Math.sin(W) * Math.sin(w + v) * Math.cos(i));
var y = r * (Math.sin(W) * Math.cos(w + v) + Math.cos(W) * Math.sin(w + v) * Math.cos(i));
var z = r * (Math.sin(i) * Math.sin(w + v));

console.log(x,y,z);
