import csv
import webbrowser
import pygame

pygame.init()


def openChromeTab(url):
    return webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url, new=0, autoraise=False)
    # return webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open(url, new=0, autoraise=False)


def game(url):
    screen = pygame.display.set_mode([800, 600])
    screen.fill([125, 255, 125])
    pygame.display.set_caption(url)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # close by button [X]
                running = False
                pygame.display.quit()
                return -1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    running = False
                    return 0
                elif event.key == pygame.K_h:
                    running = False
                    return 1
                elif event.key == pygame.K_r:
                    running = False
                    print("REACH")
                    return 2
    pygame.display.quit()


def main():

    csvfile = open("outputCSVsAddress/combinedCSV1.csv", 'r')
    writefile = open("pictureJudgement/judgedCSV.csv", "a")
    textFile = open("pictureJudgement/judgementDone.txt", "a+")
    csvreader = csv.reader(csvfile)
    fields = newFields = next(csvreader)
    newFields.append("Judgement")
    sheetData = [row for row in csvreader if len(row) > 0]
    csvwriter = csv.writer(writefile)
    # csvwriter.writerow(newFields)
    stats = [0, 0, 0]
    textFile.seek(0)
    textList = [i.strip() for i in textFile.readlines()]
    print(textList)
    counter = 0
    for row in sheetData:
        if counter > 10:
            break
        if row[0] not in textList:
            openChromeTab(row[5])
            writeRow = row
            if game(row[5]) == 0:
                stats[0] += 1
                writeRow.append("Accepted")
            elif game(row[5]) == 1:
                stats[1] += 1
                writeRow.append("Doubtful")
            elif game(row[5]) == 2:
                stats[2] += 1
                writeRow.append("Rejected")
            print(writeRow)
            csvwriter.writerow(writeRow)
            textFile.write(f"\n{row[0]}")
            counter += 1
            print(
                f"{stats[0]} Accepted, {stats[1]} Doubtful, {stats[2]} Rejected")


main()
