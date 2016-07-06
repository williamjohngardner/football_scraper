from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse


def player_stat_view(request):
    player = request.GET.get("player") or "joe flacco"
    url = "http://www.nfl.com/search?query={}".format(player)
    content = requests.get(url).text
    souper = BeautifulSoup(content, "html.parser")
    data_table = souper.find(class_="stats").attrs['href']
    content = requests.get(data_table).text
    souper = BeautifulSoup(content, "html.parser")
    player_stats = str(souper.find(id="main-content"))

    return render(request, "index.html", {"data_table": data_table, "player_stats": player_stats})
