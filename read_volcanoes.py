import pandas as pd

vol_df = pd.read_csv('Volcanoes_USA.txt')
vol_df.set_index('VOLCANX020')

lat = list(vol_df['LAT'])
lon = list(vol_df['LON'])
name = list(vol_df['NAME'])
loc = list(vol_df['LOCATION'])
elev = list(vol_df['ELEV'])

volcanoes = list(zip(name, loc, elev, lat, lon))
