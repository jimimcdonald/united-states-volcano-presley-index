import math
import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation > 3000:
        return 'orange'
    else:
        return 'red'

def distance_from_elvis(lat, lon):
    return int(math.sqrt((lat - 35.0477) **2 + (lon - -90.0260) **2) * 69)

map = folium.Map(location=[39.8283, -98.5795], zoom_start=5)

fgv = folium.FeatureGroup(name="Volcanos")

for lt, ln, el, nm in zip(lat, lon, elev, name):
    fgv.add_child(folium.CircleMarker(location=[lt, ln],
        popup= nm + ".  Elevation: " + str(int(el*3.28084)) + " ft.  " + str(distance_from_elvis(lt, ln))+ " miles from Elvis.",
            fill=True, color='brown', fill_color=color_producer(el)))

map.add_child(fgv)
map.save("USVPI.html")
