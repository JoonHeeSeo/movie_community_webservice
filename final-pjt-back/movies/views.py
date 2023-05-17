from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

from pprint import pprint

# Create your views here.

api_url = 'https://api.themoviedb.org/3/movie/top_rated?api_key=af5292844a6af1d68203e1c0b3104130&language=ko-kr'

def movies(request):
    response = requests.get(api_url).json()
    pprint(response['results'])
    test_set = set()
    for idx in response['results']:
        if idx['title'] not in test_set:
            test_set.add(idx['title'])
    print(test_set)

    return response(request, response)