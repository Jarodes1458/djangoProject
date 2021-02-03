from django.shortcuts import render
import requests

def home(request):
    response = requests.get('https://api.spotify.com/v1/artists')
    dataapi = response.json()
    context = {
        'ids': dataapi['ids'],
        'country': dataapi['country_name']

    }
    return render(request, 'core/home.html',context)
# https://simpleisbetterthancomplex.com/tutorial/2018/02/03/how-to-use-restful-apis-with-django.html
