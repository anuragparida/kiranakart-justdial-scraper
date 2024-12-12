import googlemaps
from googlegeocoder import GoogleGeocoder
import csv
import requests
import urllib
import json
import time

gmaps = googlemaps.Client(key='') # key here


def getlatlong(storeAddress):
    # time.sleep(1)
    geocode_result = gmaps.geocode(storeAddress)
    return(geocode_result)
    # geocoder = GoogleGeocoder("") #key here
    # search = geocoder.get("Watts Towers")
    # search[0].geometry.location.lat


def formatQ(searchQ):
    return(urllib.parse.quote(searchQ))


def makeReq(searchQ):
    resp = requests.get(url=searchQ)
    return(resp.json())


def main():
    with open("outputCSVs/combinedCSV1.csv", "r") as csvfile:
        writeStr = ""
        writeData = []
        errorStr = ""
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        sheetData = [row for row in csvreader if len(row) > 0]
        for row in sheetData[:1]:
            # time.sleep(0.5)
            # enter dev.virtualearth key below
            searchStr1 = "" + \
                formatQ(row[0] + ", " + row[4] + ", India")
            searchStr2 = row[0]
            print(json.dumps(getlatlong(searchStr2), indent=2))
        #     try:
        #         print(row[0] + row[4])
        #         # jsonC = makeReq(searchStr1)
        #         jsonC = requests.get(url=searchStr1).json()
        #         writeStr += "\n\n\n" + \
        #             json.dumps(jsonC, indent=2)
        #         jsonFirst = jsonC["resourceSets"][0]["resources"][0]
        #         # if jsonFirst["address"]["locality"] != "Mumbai":
        #         #     errorStr += "\n" + row[0] + " " + row[4]
        #         writeData.append(jsonFirst["point"]["coordinates"])
        #         # print(jsonFirst["point"]["coordinates"])
        #     except Exception as e:
        #         print(e)
        #         errorStr += "\n" + row[0] + " " + row[4]
        # with open("outputCSVs/geodata.csv", "w") as fkn:
        #     csvwriter = csv.writer(fkn)
        #     csvwriter.writerow(["lat", "lng"])
        #     csvwriter.writerows(writeData)
        #     print(writeData)
        #     # try:
        #     #     print(getlatlong(searchStr2))
        #     #     continue
        #     # except Exception as e:
        #     #     print(e)
        # # with open("Errors/geodata.json", "w") as jsonF:
        # #     jsonF.write(writeStr)
        # with open("Errors/error.txt", "w") as errorTxt:
        #     errorTxt.write(errorStr)


main()
