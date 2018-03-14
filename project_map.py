import folium
from read_volcanoes import volcanoes as v
from color import get_color


# create a map
us_map = folium.Map(location=(40, -98.7), zoom_start=4,tiles='Mapbox Bright')

# insert markers as children
# Feature group for World Population Data (Polygon Layer)
fgp = folium.FeatureGroup("World Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function= lambda x: {'fillColor': '#228B22' if x['properties']['POP2005'] < (1000000 * 25)
                             else '#FFFF00' if (1000000 * 25) <= x['properties']['POP2005'] < (1000000 * 50)
                             else '#FFA500' if (1000000 * 50) <= x['properties']['POP2005'] < (1000000 * 100)
                             else '#FF0000'}))

us_map.add_child(fgp)

# Feature group for Volcanoes data
fgv = folium.FeatureGroup("US Volcanoes")

for (name, location, elevation, lat, lon) in v:
    txt = "Name: "+name+" | Elevation: "+str(elevation)+" m | Location: "+location
    pop = folium.Popup(txt, parse_html=True)
    fgv.add_child(folium.CircleMarker(location=(lat, lon), radius=8, popup=pop, fill=True,
                                     fill_color=get_color(elevation), fill_opacity=0.8, color=get_color(elevation)))

us_map.add_child(fgv)



# Creating Legend
legend_html_volcanoes = '''
                <div style="position: fixed; 
                            bottom: 45px; left: 45px; width: 138px; height: 115px; 
                            border:2px solid grey; z-index:9999; font-size:14px;
                            ">&nbsp; <b>Volcanoes of USA</b><br>
                              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b><ins>Elevation</ins></b><br>
                              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <1000 &nbsp;&nbsp;&nbsp;&nbsp; <i class="fa fa-circle" style="color:#00BFFF"></i><br>
                              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; < 3000 &nbsp;&nbsp;&nbsp; <i class="fa fa-circle" style="color:#FFA500"></i><br/>
                              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; >= 3000 &nbsp; <i class="fa fa-circle" style="color:#B22222"></i>
                </div>
                '''
us_map.get_root().html.add_child(folium.Element(legend_html_volcanoes))

legend_html_population = '''
                <div style="position: fixed; 
                            bottom: 45px; right: 45px; width: 140px; height: 115px; 
                            border:2px solid grey; z-index:9999; font-size:14px;
                            ">&nbsp;&nbsp; <b><ins>World Population</ins></b><br>
                              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <1000 M &nbsp; <i class="fa fa-square" style="color:#FF0000"></i><br>
                              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; >1000 M &nbsp; <i class="fa fa-square" style="color:#FFA500"></i><br/>
                              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; >500 M &nbsp;&nbsp;&nbsp; <i class="fa fa-square" style="color:#FFFF00"></i><br/>
                              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; >250 M &nbsp;&nbsp;&nbsp; <i class="fa fa-square" style="color:#288B22"></i>
                </div>
                '''
us_map.get_root().html.add_child(folium.Element(legend_html_population))

# Add Layer Control
us_map.add_child(folium.LayerControl())
# convert it as a HTML
us_map.save('project_map.html')
