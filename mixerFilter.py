import os
import csv
import json

csv_list = os.listdir("zoneCSVsAddress")

mainFields = ["Name", "Distance", "Rating",
              "Votes", "Address", "Website", "OriginFile"]
mainData = []
mainDataNameAddress = []


def firstFunc():
    for sheetName in csv_list:
        sheetData = []
        with open("zoneCSVsAddress/" + sheetName, 'r') as sheet:
            csvreader = csv.reader(sheet)
            fields = next(csvreader)
            sheetData = [row for row in csvreader if len(row) > 0]
            for row in sheetData:
                if [row[0], row[4]] not in mainDataNameAddress:
                    mainDataNameAddress.append([row[0], row[4]])
                    x = row
                    x.append(sheetName.split(".")[0])
                    mainData.append(x)

    with open("outputCSVsAddress/combinedCSV.csv", 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(mainFields)
        csvwriter.writerows(mainData)


def secondFunc():
    areaNumbers = {}
    zoneList = [["Fort", "Churchgate", "Nariman_Point", "Dhobi_talao"],
                ["Malabar_Hill", "Kemps Corner", "Walkeshwar"],
                ["Altamound Road", "Tardeo", "Cumballa Hill",
                    "Breach Candy", "Mumbai Central"],
                ["Kalbadevi", "Cavel", "Marine Lines", "Marine Drive"],
                ["Dadar", "Matunga East", "Matunga West",
                    "Antop Hill", "Prabhadevi", "Koliwada", "Mahim"],
                ["Dongri", "Bhuleshwar", "Girgaon"],
                ["Colaba", "CuffeParade"],
                ["Kamathipura", "Agripada", "Byculla", "CottonGreen"],
                ["Khar", "BandraEast", "Bandra West"],
                ["LowerParel", "Worli", "Mahalaxmi"],
                ["Juhu", "VileParleEast", "Santacruz", "VileParleWest"],
                ["Parel"],
                ["AndheriEast", "Jogeshwari", "AndheriWest"],
                ["Kurla", "Chembur", "Sion", "Govandi", "Mankhurd"],
                ["Goregaon"],
                ["Powai"],
                ["Ghatkopar"],
                ["Malad", "Kandivali west", "Kandivali east"],
                ["Mulund", "Thane", "Nahur"],
                ["Kanjurmarg", "Vikhroli"],
                ["Borivali", "Dahisar"],
                ["Mira-Bhayandar"], ["Trombay"]]
    with open("outputCSVsAddress/combinedCSV.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        sheetData = [row for row in csvreader if len(row) > 0]
        copySheetData = sheetData
        passCount = 0
        totalCount = 0
        starThreshold = 3.5
        nVotesThreshold = 5
        for row in sheetData:
            totalCount += 1
            if row[2] == "":
                continue
            if float(row[2]) < starThreshold:
                continue
            if int(row[3].split(" ")[0]) < nVotesThreshold:
                continue
            failKeywordList = ["dry", "godrej", "reliance"]
            keyCheck = True
            for keyword in failKeywordList:
                if keyword in row[0].lower():
                    keyCheck = False
                    continue
            if not(keyCheck):
                continue
            areaNumbers[row[5]] = areaNumbers.get(row[5], 0) + 1
            passCount += 1
            mainData.append(row)
    # print(json.dumps(areaNumbers, indent=2))
    zoneNumbers = {}
    for zone in zoneList:
        for area in zone:
            try:
                zoneNumbers[", ".join(zone)] = areaNumbers[area] + \
                    zoneNumbers.get(", ".join(zone), 0)
            except Exception as e:
                print("Error Area:", area)
                print(e)
    print(json.dumps(zoneNumbers, indent=2))
    print(passCount, totalCount)
    with open("outputCSVsAddress/combinedCSV1.csv", 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(mainFields)
        csvwriter.writerows(mainData)
    with open(f"FilterStats/{nVotesThreshold}at{starThreshold}.txt", "w") as statsFile:
        statStr = f"{passCount} stores passed out of {totalCount} total stores\n{json.dumps(zoneNumbers, indent=2)}\n{json.dumps(areaNumbers, indent=2)}"
        statsFile.write(statStr)


def main():
    secondFunc()


main()
