import requests

APIKey = 'KqbBKhQ9jjeF2NygFIdr2nWzKSZDYzUYUzWhgrbe'
API = f'https://mars.nasa.gov/rss/api/?feed=weather&category=insight_temperature&feedtype=json&ver=1.0'
response = requests.get(API)
data = response.json()
print(response.status_code)
sol = data['sol_keys']
#print(response.json())
def latestSols(): 
    for i in range(7) :
        print(f'Current Sol: {sol[i]}')
        print(f'Average Temperature: {data[sol[i]]['AT']['av']}')
        print(f'Horizontal Wind Speed: {data[sol[i]]['HWS']['av']}')

latestSols()