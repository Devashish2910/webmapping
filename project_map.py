import folium
from read_volcanoes import volcanoes as v
from color import get_color


# create a map
us_map = folium.Map(location=(38, -96.7), zoom_start=5)

# insert markers as children
fg = folium.FeatureGroup("US Volcanoes Markers")

for (name, location, elevation, lat, lon) in v:
    txt = "Name: "+name+" | Elevation: "+str(elevation)+" m | Location: "+location
    pop = folium.Popup(txt, parse_html=True)
    fg.add_child(folium.Marker(location=(lat, lon), popup=pop,
                               icon=folium.Icon(color=get_color(elevation))))

us_map.add_child(fg)

# convert it as a HTML
us_map.save('project_map.html')
