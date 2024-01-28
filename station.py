# Import Meteostat library
from meteostat import Stations

station=Stations()
print ("enter lat")
lat = float(input (" "))
print ("enter long")
lon = float(input (""))
station=station.nearby(lat, lon)
station.fetch(1)