import folium
import pandas
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])


def color_hi(elv):
    if elv > 3000:
        return "red"
    elif elv < 1000:
        return "green"
    else:
        return "orange"


map1 = folium.Map()

mkV = folium.FeatureGroup(name="Volcano")
for lt, lo, el in zip(lat, lon, elev):
    mkV.add_child(folium.CircleMarker(location=(lt, lo), radius=6, tooltip=str(el)+str(" m"),
                                      fill_color=color_hi(el), fill_opacity=1, color="grey"))

mkP = folium.FeatureGroup(name="Population")
mkP.add_child(folium.GeoJson(data=open("world.json", 'r', encoding="utf-8-sig").read(),
                             style_function=lambda x: {"fillColor": "green" if x['properties']["POP2005"] < 10000000
                             else 'yellow' if 10000000 <= x['properties']["POP2005"] < 20000000 else 'red'}))

map1.add_child(mkP)
map1.add_child(mkV)

map1.add_child(folium.LayerControl())
map1.save("map.html")
