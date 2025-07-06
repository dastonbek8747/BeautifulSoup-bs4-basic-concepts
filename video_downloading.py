from bs4 import BeautifulSoup
import requests

url = "https://www.blipcut.com/sora-video-generator.html"
response = requests.get(url)
print("Status Code : ", response)

soup = BeautifulSoup(response.text, "lxml")
# video ni url ni chiqarib olib koramiz oldiniga
videos_urls = soup.find_all("h1")
print(videos_urls)

for video in videos_urls:
    print(video["src"])
    print("////////////////////////////////////////////////////////////////////")
