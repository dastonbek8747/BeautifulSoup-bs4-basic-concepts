from pathlib import Path

from bs4 import BeautifulSoup
import requests
import json

url = "https://stock.adobe.com/uz/search/images?k=8k+wallpaper"
response = requests.get(url)
print("Status Code :", response)
soup = BeautifulSoup(response.text, "lxml")

images_all = soup.find_all("img", class_="js-lazy align-center")
for url in images_all:
    print(url["data-lazy"])
    print("----------------------------------------------------")

    filename = url["data-lazy"].split("/")[-1]

    # 3. Rasmni olish
    # response = requests.get(url["data-lazy"])
    # print(response)

    # 4. Saqlanadigan papka
    save_dir = Path("images")
    save_dir.mkdir(exist_ok=True)


    # 5. Rasmni yozamiz
    with open(save_dir / filename, "wb") as f:
        f.write(requests.get(url["data-lazy"]).content)

    print(f"✅ Rasm saqlandi: {save_dir / filename}")
