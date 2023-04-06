from numpy import sin, cos, arccos, pi, round
latitude= (44.860556, 44.860556)
longitude= (24.867778000000044, 24.867778000000044)
theta = longitude[0] - longitude[1]
distance = 60 * 1.1515 * arccos(round((sin(latitude[0]*pi/180) * sin(latitude[1]*pi/180)) + (cos(latitude[0]*pi/180) * cos(latitude[1]*pi/180) * cos(theta*pi/180)),7))*180/pi
print(distance)