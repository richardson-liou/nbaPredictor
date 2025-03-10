from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd


def getRows():
    url = "https://www.espn.com/nba/teams/comparison/_/team1/atl/team2/bos"
    path = "C:\\Users\\richa\\OneDrive\\Desktop\\chromedriver-win64\\chromedriver.exe"

    options = Options()
    options.add_argument("--headless")

    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)

    var = "//table[@class='tablehead']//tbody"
    containers = driver.find_elements(by="xpath", value=var)
    list = []
    if len(containers) > 1 :

        # print("There is more than one tbody we are getting to the second ")
        second_tbody = containers[2]
        rows = second_tbody.find_elements(by="xpath", value=".//tr")
        for row in rows:
            list.append(row.text)

    else:
        print("There is only one for some reason ")
    driver.quit()
    return list

data = getRows()[2:]

teams = []
stats = []
players = []
values = []




for i in data:
    parts = i.split()
    stat = parts[0] + " " + parts[1] if "%" in parts[1] else parts[0]

    player1 = parts[1] if "%" not in parts[1] else parts[2] + " " + parts[3]

    value1 = parts[-4]
    player2 = parts[-3] + " " + parts[-2]
    value2 = parts[-1]

    stats.append(stat)
    players.append(player1)
    values.append(value1)
    teams.append("ATLANTA")

    teams.append("BOSTON")
    stats.append(stat)
    players.append(player2)
    values.append(value2)

newData = {"stats":stats, "teams":teams, "values":values, "players":players}
df= pd.DataFrame(newData)
df.to_excel("example.xlsx", index = False)
print(df)










print(getRows())



# patter =r"(\w+ \d{1,2})\s+([A-Za-z]+ \d{1,3},)\s+([A-Za-z]+ \d{1,3}(?: \(OT\))?)\s+(\w+ \d+ Pts)\s+(\w+ \d+ Pts)"
