import json

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

# title = soup.title
# # bu ko'rinishda qilsak bizda html ichidan title ni olamiz
# print(title)
# # bu orqali esa title textini olamiz
# print(title.text)


# endi esa ixtiyori teg va yoki shu teglarni olishni koramiz
# demak olx saytidagi ishlarni olish kodi
# all_div_tags = soup.find_all('div', class_="jobs-ad-card css-1ju4r67")
# for div in all_div_tags:
#     # print(div)
#     print(div.text)
#     # print(div.text.strip())  # bu orqali esa div textini qabli qilib olamiz


# endi esa qiyinroq vazifa qilamiz. yani olgan malumotlarimizni listga dict korinishida yani json formatiga otkazib olamiz

all_divs_ = soup.find_all("div", class_="jobs-ad-card css-1ju4r67")
jobs_json = []
for job in all_divs_:
    job_name = job.find("h4", class_="css-amfvow").text.strip()
    job_price = job.find("p", class_="css-zgm539").text.strip()
    job_address = job.find("span", class_="css-jw5wnz").text.strip()
    time = job.find("p", class_="css-15khyzd").text.strip()
    stavka = job.find("p", class_="css-15khyzd").text.strip()
    date = job.find("p", class_="css-996jis").text.strip()

    job_dic = {
        "job_name": job_name,
        "job_price": job_price,
        "job_address": job_address,
        "time": time,
        "stavka": stavka,
        "date": date
    }
    jobs_json.append(job_dic)
    print("Succseffull +++++++++++++++++++++")

print(len(jobs_json))
print(json.dumps(jobs_json, indent=4, ensure_ascii=False))

