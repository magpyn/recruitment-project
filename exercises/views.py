from django.shortcuts import render
import requests


def home(request):
    url = 'https://randomuser.me/api/?results=10'
    r = requests.get(url)
    content = r.json()

    for user in content['results']:
        nat = user['nat']
        userUrl = 'https://restcountries.eu/rest/v2/name/{}'.format(nat)
        r = requests.get(userUrl)
        userContent = r.json()
        flag = userContent[0]['flag']
        user['flag'] = flag
    return render(request, 'home.html', {'content': content['results']})
