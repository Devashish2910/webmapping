import folium

# create a map
us_map = folium.Map(location=(38, -96.7), zoom_start=5)

# convert it as a HTML
us_map.save('project_map.html')
