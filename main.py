import requests
from bs4 import BeautifulSoup

url = "https://faruk-hasan.com/ai_resources/greetings.html"
data = requests.get(url).text

soup = BeautifulSoup(data, 'html.parser')
greetings = soup.findAll('p')
print(greetings)

refined_greetings = []
for greeting_phrase in greetings:
    refined_greetings.append(greeting_phrase.text)

print(refined_greetings)