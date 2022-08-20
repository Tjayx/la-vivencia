import requests
from requests import get
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
headers = {"Accept-Language": "en-US, en; q=0.5"}
driver = webdriver.Chrome()
Location = input("Enter a location you want to move to in the UK: ")
print("Searching for apartments, please wait...")

driver.get("https://www.openrent.co.uk")
assert "OpenRent" in driver.title

geoboy = driver.find_element(By.ID, "searchBox")

geoboy.send_keys(Location)
time.sleep(5)

driver.find_element(By.ID, "embeddedSearchBtn").click()

current_url = driver.current_url
results = requests.get(str(current_url), headers=headers)
soup = BeautifulSoup(results.text, "html.parser")
count = soup.find('span', class_= 'prop-count')

lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount==lenOfPage:
        match=True

fullnk = driver.current_url
results = requests.get(str(fullnk), headers=headers)
soup = BeautifulSoup(results.text, "html.parser")
price = []
prop_name = []
prop_link = []
descr = []
land_link = []

properts = soup.find_all('a', class_= 'pli clearfix')
for props in properts:
    prc = props.find("div", class_= 'pim pl-title')
    pris = prc.h2.text
    price.append(pris)
    nme = props.find("span", class_= 'banda pt listing-title')
    prop_name.append(nme.text)
    proplnk = "https://www.openrent.co.uk" + props['href']
    prop_link.append(proplnk)

    results = requests.get(proplnk, headers=headers)
    soup = BeautifulSoup(results.text, "html.parser")
    descript = soup.find("div", class_= "description")
    descr.append(descript.text)
    landlnk = soup.find('a', class_= "btn btn-primary")
    land_link.append(("https://www.openrent.co.uk" + landlnk['href']))
    

for i in price:
    j = i
    while j[0] != "£":
        j = j[1:]

    print("/////" * 5)
    print(prop_name[price.index(i)], j)
    print(i) #price
    print(descr[price.index(i)])
    print(land_link[price.index(i)])
