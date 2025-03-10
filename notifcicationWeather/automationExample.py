from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



def getRows(url):
    path = "C:\\Users\\richa\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

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
        second_tbody = containers[1]
        rows = second_tbody.find_elements(by="xpath", value=".//tr")
        for row in rows:
            list.append(row.text)

    else:
        print("There is only one for some reason ")
    driver.quit()
    return list

test = getRows("https://www.espn.com/nba/teams/comparison/_/year/2024/team1/atl/team2/bos")
print(test)

#
# for i in containers:
#     try:{
#         print(i.text)
#     }
#     except:
#         # Handle cases where <h3> might not be found
#         print("")



