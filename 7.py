from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

fig = plt.figure()

m = Basemap()

m.drawcoastlines()

m.fillcontinents(color='lightgray')

m.drawcountries()

plt.title("Base Map")

plt.show()
