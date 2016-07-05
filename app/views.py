from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse

# from urllib.parse import urlparse

def get_stats(player):
    url = "http://search.nfl.com/search?query={}".format(player)
    content = requests.get(url).text
    souper = BeautifulSoup(content, "html.parser")
    data_table = souper.find(class_="stats")
    player_url = data_table.a.attrs['href']
    # print(player_url.a.attrs['href'])
    content = requests.get(player_url).text
    souper = BeautifulSoup(content, "html.parser")
    return data_table

def player_stat_view(request):
    player = request.GET.get("player") or "drew brees"
    data_table = get_stats(player)
    return render(request, "index.html", {"data_table": data_table, "player": player})
