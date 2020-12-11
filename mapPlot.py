import numpy as np
import pandas as pd
import csv
from PIL import Image
import matplotlib.pyplot as plt


def getBBox():
    df = pd.read_csv("outputCSVs/geodataGunique.csv")

    BBox = (df.lng.min(), df.lng.max(), df.lat.min(), df.lat.max())

    print(BBox)


def removeDup():
    with open("outputCSVs/geodataG.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        sheetData = [row for row in csvreader if len(row) > 0]
        writeData = []
        for row in sheetData:
            if row not in writeData:
                bounds = [19.35, 72.75, 18.85, 73.0]
                lat = float(row[0])
                lng = float(row[1])
                if lat <= bounds[0] and lat >= bounds[2]:
                    if lng >= bounds[1] and lng <= bounds[3]:
                        writeData.append(row)
        # sheetData = list(set([" ".join(i) for i in sheetData]))
        with open("outputCSVs/geodataGunique.csv", "w") as fkn:
            csvwriter = csv.writer(fkn)
            csvwriter.writerow(["lat", "lng"])
            csvwriter.writerows(writeData)


def plotM():
    ruh_m = plt.imread('map6.png')
    data = np.zeros((2983, 1336, 3), dtype=np.uint8)
    data.fill(255)
    print(data)
    img = Image.fromarray(data, 'RGB')
    df = pd.read_csv("outputCSVs/geodataGunique.csv")

    BBox = (df.lng.min(), df.lng.max(), df.lat.min(), df.lat.max())

    fig, ax = plt.subplots(figsize=(8, 8))
    points_whole_ax = 5 * 0.8 * 72    # 1 point = dpi / 72 pixels
    radius = 0.0452
    points_radius = 2 * radius / 1.0 * points_whole_ax
    ax.scatter(df.lng, df.lat, zorder=1, alpha=0.025,
               c='b', s=points_radius**2)
    ax.set_title('Plotting Data')
    ax.set_xlim(BBox[0], BBox[1])
    ax.set_ylim(BBox[2], BBox[3])
    ax.imshow(img, zorder=0, extent=BBox, aspect='equal', cmap=plt.cm.gray)

    plt.gcf().savefig('heatmaps/heatmapG300a25B.png', dpi=500)
    plt.show()


def main():
    # removeDup()
    # getBBox()
    plotM()


main()
