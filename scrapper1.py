import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Sufism"

response = requests.get(url)
response = response.content
soup = BeautifulSoup(response,'html.parser')
print(soup)
paragraph = soup.find_all('p')[0:4]
print(paragraph)
div = soup.find_all('div')[0:2]
print(div)

Bektashi = soup.find_all(text="Bektashi")
print(Bektashi)
Ibn_Arabi = soup.find_all(text="Ibn Arabi")
print(Ibn_Arabi)

bayah = soup.find_all(text="bayah")
print(bayah)
