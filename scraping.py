import requests
from bs4 import BeautifulSoup
url = 'https://stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for questions in html.select('.question-summary'):
    title = questions.select_one('.question-hyperlink')
    data = questions.select_one('.relativetime')
    votes = questions.select_one('.vote-count-post ')
    print(data.text, title.text, votes.text , sep='\t')