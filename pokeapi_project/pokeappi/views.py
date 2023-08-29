from django.shortcuts import render
import requests

def index(request):
    return render(request, 'pokeappi/index.html')

def search_pokemon(request):
    if 'q' in request.GET:
        query = request.GET['q']
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{query}')
        data = response.json()
        return render(request, 'pokeappi/search_results.html', {'pokemon_data': data})
    return render(request, 'pokeappi/index.html')

def ability_detail(request, ability_name):
    response = requests.get(f'https://pokeapi.co/api/v2/ability/{ability_name}')
    ability_data = response.json()
    return render(request, 'pokeappi/ability_detail.html', {'ability_data': ability_data})
