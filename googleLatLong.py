import googlemaps
import json
import csv

gmaps = googlemaps.Client(key='')


def getlatlong(storeAddress):
    # time.sleep(1)
    geocode_result = gmaps.geocode(storeAddress)
    return(geocode_result)


def main():
    with open("outputCSVs/combinedCSV1.csv", "r") as csvfile:
        writeStr = ""
        writeData = []
        errorStr = ""
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        sheetData = [row for row in csvreader if len(row) > 0]
        for row in sheetData:
            # time.sleep(0.5)
            searchStr1 = row[0] + ", " + row[4] + ", India"
            searchStr2 = row[0]
            print(searchStr1)
            try:
                res = getlatlong(searchStr1)
                # print(json.dumps(res, indent=2))
                writeStr += "\n\n\n" + \
                    json.dumps(res, indent=2)
                loc = res[0]["geometry"]["location"]
                writeData.append([loc["lat"], loc["lng"]])
            except Exception as e:
                print(e)
                errorStr += searchStr1
        with open("outputCSVs/geodataG.csv", "w") as fkn:
            csvwriter = csv.writer(fkn)
            csvwriter.writerow(["lat", "lng"])
            csvwriter.writerows(writeData)
            print(writeData)
        with open("Errors/errorG.txt", "w") as errorTxt:
            errorTxt.write(errorStr)


main()