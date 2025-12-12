import requests
import pandas as pd
from bs4 import BeautifulSoup
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

url = "https://faruk-hasan.com/ai_resources/greetings.html"
data = requests.get(url).text

soup = BeautifulSoup(data, 'html.parser')
greetings = soup.find_all('div', class_='container')


greetings_list = []
for greeting in greetings:
    for i in greeting.find_all('p'):
        greetings_list.append(i.text)

print(greetings_list)
print("\n\n\n")


vectorizer = CountVectorizer()

x = vectorizer.fit_transform(greetings_list)
print(x)
print("\n\n\n")

print(vectorizer.get_feature_names_out())


counts_df = pd.DataFrame(
    data=x.toarray(),
    columns=vectorizer.get_feature_names_out()
)

counts_df.to_csv('output.csv', index=False)