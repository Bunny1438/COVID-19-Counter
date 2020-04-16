import requests
from bs4 import BeautifulSoup

url="https://www.worldometers.info/coronavirus/country/india/"
r= requests.get(url)
s= BeautifulSoup(r.text,"html.parser")
data = s.find_all("div",class_ = "maincounter-number")

print("total Cases:", data[0].text.strip())

print("total Deaths:", data[1].text.strip())

print("total Recovered:", data[2].text.strip()) 