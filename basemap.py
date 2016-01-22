import matplotlib as mpl
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


def run():
    basemap = set_basemap_projection()
    draw_plot(basemap)
    save_plot()


def set_basemap_projection():
    axes = []
    basemaps = []

    subplots = plt.subplots(nrows=1, ncols=2)
    axes.extend(subplots[1])
    basemaps.append(Basemap(projection='ortho', lon_0=270, lat_0=90., resolution='c', ax=axes[0]))
    basemaps.append(Basemap(projection='ortho', lon_0=90, lat_0=-90., resolution='c', ax=axes[1]))
    return basemaps


def draw_plot(basemaps):
    for idx, basemap in enumerate(basemaps):
        # Cant draw a valid PDF readable by Adobe Reader XI
        basemap.readshapefile('shapefiles/Earth', 'globe')

        # Split shapefile into northern and southern hemisphere coordinates (2 shapefiles) and it draws fine.
        #
        # if idx == 0:
        #     basemap.readshapefile('shapefiles/Earth_north', 'nh')
        # else:
        #     basemap.readshapefile('shapefiles/Earth_south', 'sh')


def save_plot():
    plt.savefig('map.pdf')
    plt.close()

run()
