from bs4 import BeautifulSoup
import requests

site_url = "https://www.olx.uz/oz/rabota/"
response_url = requests.get(site_url)
print("Statuc code :", response_url)

# Biz bu yerda html kodlarini o'qib olamiz lxml orqali
soup = BeautifulSoup(response_url.text, 'lxml')

# masalan bizga html ichidan kerak boladigan teg ni tanlab olib undagi malumotlarni olishimmiz mumkin boladi
#  misol uchun : h1, div, img, p, ..... ixtiyori tegdagi malumotlarni olamiz


# # misol uchun title ni olamiz
#
# title = soup.title
# # bu ko'rinishda qilsak bizda html ichidan title ni olamiz
# print(title)
# # bu orqali esa title textini olamiz
# print(title.text)


# endi esa ixtiyori teg va yoki shu teglarni olishni koramiz
# demak olx saytidagi ishlarni olish kodi
all_div_tags = soup.find_all('div', class_="jobs-ad-card css-1ju4r67")

for div in all_div_tags:
    # print(div)
    print(div.text)
    # print(div.text.strip())  # bu orqali esa div textini qabli qilib olamiz
