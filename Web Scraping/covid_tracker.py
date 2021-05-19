import requests
from bs4 import BeautifulSoup


url = "https://3news.com/"
web_response = requests.get(url)
web_contents = web_response.text
soup = BeautifulSoup(web_contents, 'html5lib')

for stats in soup.find_all('div', class_='coronatracker-card'):
    for headers in stats.find_all('h2'):
        print(f"\n{headers.text.strip()}")
        print("="*len(headers.text))
        a = stats.text.strip().replace(headers.text, "").split()
        print(f"{' '.join(a[1:3])}:  {a[0]}\n{' '.join(a[4:6])}:  {a[3]}\n{' '.join(a[-2:])}:  {a[-3]}")
