import requests
import json

API = 'https://mars.nasa.gov/rss/api/?feed=weather&category=msl&feedtype=json'
response = requests.get(API)
data = response.json()
print(response.status_code)

text = str(data)
firstEntry = text.find("\'terrestrial_date\'")
temp = text[firstEntry+10:]
secondEntry = firstEntry + 10 + temp.find("\'terrestrial_date\'")

info = text[firstEntry:secondEntry]
info = info.split(",")
info.pop()
info.pop()

solCount = info[1][info[1].find(":") + 3 : len(info[1])-1]
terrestrial_date = info[0][info[0].find(":") + 3 : len(info[0])-1]
minTemp = info[4][info[4].find(":") + 3: len(info[4])-1] 
maxTemp = info[5][info[5].find(":") + 3: len(info[5])-1] 

def getSol() :
    print(f'Current Sol: {solCount}')
def getTerrestrial() :
    print(f'Current Terrestrial Date: {terrestrial_date}')
def getMin():
    print(f'Min Temp: {minTemp}')
def getMax():
    print(f'Max Temp: {maxTemp}')


getSol()
getTerrestrial()
getMin()
getMax()