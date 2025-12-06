import requests
from bs4 import BeautifulSoup

url = "https://faruk-hasan.com/ai_resources/greetings.html"
data = requests.get(url).text

soup = BeautifulSoup(data, 'html.parser')
greetings = soup.find_all('div', class_='container')

for greeting in greetings:
    for i in greeting.find_all('p'):
        print(i.text)

# refined_greetings = []
# for greeting_phrase in greetings:
#     refined_greetings.append(greeting_phrase.text)

# print(refined_greetings)