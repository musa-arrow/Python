import requests

from bs4 import BeautifulSoup

url = "https://musa-arrow.github.io/mySite/"
response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

# print(soup.prettify()) # soup.prettify() -> Bir HTML veya XML dökümanını daha okunabilir, girintili (indentli) biçimde döndürür.

# print(soup.find_all("a")) # a etiketlerini yazdırır

for i in soup.find_all("a"):
    print(i.get("href"))
    print("*********************************************")

for i in soup.find_all("a"):
    print(i.text)
    print("*********************************************")

print(soup.find_all("div",{"class":"container"}))


# Not: Bu yöntem statik HTML sayfalarda çalışır
# Dinamik (JS ile yüklenen) içerik için requests + BeautifulSoup yeterli olmaz
# O zaman Selenium veya Playwright gerekir