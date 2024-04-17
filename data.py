import pandas as pd, urllib.request, json, requests


with urllib.request.urlopen('https://mars.nasa.gov/rss/api/?feed=weather&category=msl&feedtype=json') as url:
    data = json.load(url)
df = pd.DataFrame(data['soles'])
df['terrestrial_date'] = pd.to_datetime(df['terrestrial_date'], format = '%Y-%m-%d')
df = df.sort_values(by='terrestrial_date', ascending = True)
pd.set_option('display.max_rows', None)


recentDate = df['terrestrial_date'][0]
recentMin = df['min_temp'][0]
recentMax = df['max_temp'][0]
recentSol = df['sol'][0]


def getTerrestrial(x) :
    date = df['terrestrial_date'][x]
    print(date)
def getMin(x) :
    min = df['min_temp'][x]
    print(min)
def getMax(x) :
    max = df['max_temp'][x]
    print(max)
def getSol(x):
    sol = df['sol'][x]
    print(sol)
def getLastWeek() :
    for i in range(7, -1, -1):
        print('Terrestrial Day:')
        getTerrestrial(i)
        print('Min Temp:')
        getMin(i)
        print('Max Temp:')
        getMax(i)
        print('Martian Sol:')
        getSol(i)
        print(' ')
def currentConditions():
    print(f'Today\'s Date: {recentDate}')
    print(f'Today\'s Sol: {recentSol}')
    print(f'Today\'s Min Temp: {recentMin}')
    print(f'Today\'s Max Temp: {recentMax}')


getLastWeek()
currentConditions()




