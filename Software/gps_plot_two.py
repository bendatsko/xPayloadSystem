from gmplot import *

Ann_Arbor_top_attraction_lats, Ann_Arbor_top_attraction_lons = zip(*[ (42.281993, -83.731163), (17.4156, 78.4750)
])
# centre of Ann Arbor
gmap = gmplot.GoogleMapPlotter(42.2808, -83.7430, 13)
gmap.scatter(Ann_Arbor_top_attraction_lats, Ann_Arbor_top_attraction_lons, '#FF0000',size = 100, marker = False)
gmap.plot(Ann_Arbor_top_attraction_lats, Ann_Arbor_top_attraction_lons, 'cornflowerblue', edge_width = 30)
gmap.apikey = "AIzaSyAywLkBvqvnLAA3FFg-lFp38iqjXsV6FKs"
gmap.draw("/home/wulfabie/Engin100/engin_map_two.html")