from openpyxl import Workbook
import re
import itertools
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

path = "C:\\Users\\richa\\OneDrive\\Desktop\\chromedriver.exe"


def getRows():
    url = "https://www.espn.com/nba/boxscore?gameId=401705153"

    options = Options()
    options.add_argument("--headless")

    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)
    print("#####################")
    print(url)
    driver.get(url)

    # how to get game link

    # var = ""
    var = "//table[contains(@class, 'mod-data')]//tbody"
    # var2 = "//*[@id=\"fittPageContainer\"]/div[2]/div/div/div/div[5]/div/div[1]/section"
    # var3 = "//*[@id=\"fittPageContainer\"]/div[2]/div/div/div/div[5]/div/div[1]/section/div/div/div/div[1]/div/div[2]/div/table/tbody"
    var = "//table[@class='Table__TBODY']//tbody"
    # var2 = "//*[@id=\"fittPageContainer\"]/div[2]/div/div/div/div[5]/div/div[1]/section/div/div/div/div[1]/div/div[2]/div/table/tbody"
    rows = driver.find_elements(by = "xpath", value = "//div[contains(@class, 'Boxscore')]//div//div//table//tbody[contains(@class, 'Table__TBODY')]//tr")
    print("Containers", )

    for row in rows:
        print(row.text)


    # list = []
    #
    # if len(containers) > 1:
    #
    #     print("Containers has data")
    #
    #     # print("There is more than one tbody we are getting to the second ")
    #     # second_tbody = containers[0]
    #     rows = containers.find_elements(by="xpath", value=".//tr")
    #     print(rows)
    #     for row in rows:
    #         list.append(row.text)
    # print(list)
    driver.quit()


def get_game_data ():
    options = Options()
    options.add_argument("--headless")

    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(game_url)

    print(rows)

    # game_data = []
    #
    # for row in rows:
    #     cells = row.find_elements(by="tag name", value="td")
    #     if len(cells) < 7:
    #         team_name = row.find_element(by="tag name", value="th").text
    #         if team_name:
    #             current_team = team_name
    #         continue
    #
    #     player_stats = [current_team] + [cell.text for cell in cells]
    #     game_data.append(player_stats)

    driver.quit()
    # return game_data
#get_game_data()


print(getRows())

