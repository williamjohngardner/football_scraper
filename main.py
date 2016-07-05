import requests
from bs4 import BeautifulSoup

hostname = "http://www.nfl.com/player/drewbrees/2504775/careerstats"
content = requests.get(hostname)


souper = BeautifulSoup(content.text, "html.parser")

elements = souper.find(class_="data-table1") #class is a reserved word in Python, the _class is a hack

for stats in elements.find_all():
    print(stats)
