import os
from bs4 import BeautifulSoup
import csv


def formatText(text):
    return " ".join((text).strip().split())


# CHANGE LINE 10, I MOVED HTMLS INTO HTML, SHOULD BE IN ROOT
site_list = [f.path for f in os.scandir() if f.is_file()]

for file in site_list:
    fields = ["Name", "Distance", "Rating", "Votes", "Address"]
    data = []
    if file == ".\scraper.py":
        continue
    print(file)
    content = open(file, "r", encoding="utf8").read()
    soup = BeautifulSoup(str(content), 'html.parser')
    li_list = []
    for li in soup.find_all("li", class_="cntanr"):
        li_list.append(li)
    # print(li_list[0].prettify())
    # open("li.html", "w").write(li_list[0].prettify())

    # print(formatText(soup.find("span", class_="lng_cont_name")))
    # print(soup.prettify())

    for li in li_list:
        currentData = []
        soup = BeautifulSoup(str(li), 'html.parser')

        try:
            # currentData.append(formatText(
            #     soup.find("span", class_="lng_cont_name").get_text()))
            x = formatText(soup.find("li", class_="cntanr")["data-href"])
            x = x.split("/")[4]
            x = " ".join(x.split("-"))
            currentData.append(x)
        except:
            currentData.append("")

        try:
            currentData.append(formatText(
                soup.find("span", class_="dist").span.get_text()))
        except:
            currentData.append("")

        try:
            currentData.append(formatText(
                soup.find("span", class_="green-box").get_text()))
        except:
            currentData.append("")

        try:
            currentData.append(formatText(
                soup.find("span", class_="lng_vote").get_text()))
        except:
            currentData.append("")

        try:
            currentData.append(formatText(
                soup.find("span", class_="cont_fl_addr").get_text()))
        except:
            currentData.append("")

        # print(currentData)
        data.append(currentData)

    csvName = "zoneCSVs/" + file.split("\\")[1].split(".")[0] + ".csv"
    with open(csvName, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(data)
