import requests 

BASE = "http://127.0.0.1:5000/"

data = [{'likes': 10, 'name': 'Tim', 'views': 100},
        {'likes': 11, 'name': 'Tim2', 'views': 1000},
        {'likes': 12, 'name': 'Tim3', 'views': 10}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())


input()

response = requests.get(BASE + 'video/6')
print(response.json())