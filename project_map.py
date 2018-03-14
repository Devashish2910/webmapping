import folium
from read_volcanoes import volcanoes as v
from color import get_color


# create a map
us_map = folium.Map(location=(40, -98.7), zoom_start=5,tiles='Mapbox Bright')

# insert markers as children
fg = folium.FeatureGroup("US Volcanoes Markers")

for (name, location, elevation, lat, lon) in v:
    txt = "Name: "+name+" | Elevation: "+str(elevation)+" m | Location: "+location
    pop = folium.Popup(txt, parse_html=True)
    fg.add_child(folium.CircleMarker(location=(lat, lon), radius=8, popup=pop, fill = True,
                                     fill_color=get_color(elevation), fill_opacity=0.8, color=get_color(elevation)))

us_map.add_child(fg)

# Creating Legend
legend_html =   '''
                <div style="position: fixed; 
                            bottom: 45px; left: 45px; width: 138px; height: 120px; 
                            border:2px solid grey; z-index:9999; font-size:14px;
                            ">&nbsp; <b>Volcanoes of USA</b><br>
                              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <b><ins>Elevation</ins></b><br>
                              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <1000 &nbsp;&nbsp;&nbsp;&nbsp; <i class="fa fa-circle" style="color:#00BFFF"></i><br>
                              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; < 3000 &nbsp;&nbsp;&nbsp; <i class="fa fa-circle" style="color:#FFA500"></i><br/>
                              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; >= 3000 &nbsp; <i class="fa fa-circle" style="color:#B22222"></i>
                </div>
                '''
us_map.get_root().html.add_child(folium.Element(legend_html))

# convert it as a HTML
us_map.save('project_map.html')
