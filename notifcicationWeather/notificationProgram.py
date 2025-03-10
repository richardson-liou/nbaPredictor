import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
from windows_toasts import Toast, WindowsToaster
# toaster = WindowsToaster('Python')
# newToast = Toast()
# newToast.text_fields = ['Hello, world!']
# newToast.on_activated = lambda _: print('Toast clicked!')
# toaster.show_toast(newToast)

lat = 32.715736
long = -117.161087

url =  f"https://api.weather.gov/points/{lat},{long}"
response = requests.get(url)
weatherUrl = response.json()["properties"]["forecast"]
print(weatherUrl)
print(response.json())

forecast = requests.get(weatherUrl).json()
for i in forecast["properties"]["periods"]:
    print(f"{i['name']}: {i['detailedForecast']}")

# note = ToastNotifier()
# def getData(url):
#     r = requests.get(url)
#     return r.text
# #htmlData = getData("https://weather.com/en-IN/weather/today/l/543bbfddbee58187429c6def75c8240755442adb8d12511cf10c977521cd38f3")
# #soup = BeautifulSoup(htmlData,"html.parser")
# #currentTemperature = soup.find_all()
# temp = 4
# tempRain = 6
# note.show_toast("Live weather data",f"Temperature: {temp} chances of rain{tempRain},", duration = 10)
n = ToastNotifier()

n.show_toast("Weather", "Mostly sunny, with a high near 80. West wind around 5 mph.", duration = 10)