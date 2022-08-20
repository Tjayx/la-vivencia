import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import traceback
import re
import sys
from keep_alive import keep_alive


#keep_alive()
headers = {"Accept-Language": "en-US, en; q=0.5"}

url = "https://www.cartoonsarea.xyz/Japanese-Dubbed-Videos/"



numpgperseason = []
numseason = []
sizelist = []
duralist = []

results = requests.get(url, headers=headers)
soup = BeautifulSoup(results.text, "html.parser")
cat_link = soup.find_all("div", class_= "Singamdasam")
cat_link.pop()

for letter in cat_link:
  for movlist in letter.find_all('a', href = True):
    pgs = "https:" + movlist['href']

    titles = []
    years = []
    status = []
    avgsize = []
    totsize = []
    avgtime = []
    tottime = []
    episodes = []
  
    url1 = str(pgs)
    results1 = requests.get(url1, headers=headers)
    soup = BeautifulSoup(results1.text, "html.parser")
    movlink = soup.find_all("div", class_= "Singamdasam")
    movlink.pop()
    #movlink.pop(2)

    for j in movlink:
      name = j.a.text
      titles.append(name)
      print(name)
      for oplink in j.find_all('a', href = True):
        movpg = "https:" + oplink['href']
        
        url2 = str(movpg)
        results2 = requests.get(url2, headers=headers)
        soup = BeautifulSoup(results2.text, "html.parser")
        movbox = soup.find_all('div', attrs = {'class': 'Box'})
        
        detsbox = movbox[0]
        if  detsbox.b.find('span', style='color: red;'):
          movstatus = detsbox.b.find('span', style='color: red;').text
          status.append(movstatus)
          
          movyear = detsbox.b.text
          movyear_ = movyear[-4:]
          years.append(movyear_)
          seasonbox = soup.find_all('div', class_= 'Singamdasam')
          seasonbox.pop()
          for l in seasonbox:
            for m in l.find_all('a', href = True):
              
              episopg = "https:" + m['href']
              print(episopg)
              url3 = str(episopg)
              results3 = requests.get(url3, headers=headers)
              soup = BeautifulSoup(results3.text, "html.parser")
              #print (soup)

              if soup.find('ul', class_= 'pagination'):
                episopag = soup.find('ul', class_= 'pagination')
                for n in episopag.find_all('li'):
                  for linkb in n.find_all('a', href = True):
                    pglink = linkb['href']
      
                    url4 = url3 + str(pglink)
                    results4 = requests.get(url4, headers=headers)
                    soup = BeautifulSoup(results4.text, "html.parser")
                    #sodesbox = soup.find('div', class_= 'none')
                    episnumb = soup.find_all('div', class_= 'Singamdasam')
                    episnumb.pop()
                    num = len(episnumb)
                    numpgperseason.append(num) #list of number of episodes in pages of a season 
                    for epis in episnumb:
                      for p in epis.find_all('a', href = True):
                        epislink = "https:" + p['href']

                        url5 = str(epislink)
                        results5 = requests.get(url5, headers=headers)
                        soup = BeautifulSoup(results5.text, "html.parser")
                        if soup.find_all('span', attrs= {'style': 'color:black;'}):
                          perepsbox = soup.find_all('span', attrs= {'style': 'color:black;'})
                          perepsboxx = perepsbox[0]
                          for q in perepsboxx.find_all('a', href = True):
                            todownloadpg = "https:" + q['href']

                            url6 = str(todownloadpg)
                            results6 = requests.get(url6, headers=headers)
                            soup = BeautifulSoup(results6.text, "html.parser")
                            if soup.find('div',  class_= 'Singamdasam text-center'):
                              descrbox = soup.find('div',  class_= 'Singamdasam text-center')
                              descrdets = descrbox.find_all('td', attrs= {'class': 'desc_value'})
                              size = descrdets[1].text
                              duration = descrdets[2].text
                              sizelist.append(size)
                              duralist.append(duration)
                            else:
                              continue
                        else:
                          continue
                    
              else:
                #sodesbox = soup.find('div', class_='none') if (soup.b.find('div', class_='none')) != None else results3
                episnumb = soup.find_all('div', class_= 'Singamdasam')
                episnumb.pop()

                num = len(episnumb)
                print(num)
                numpgperseason.append(num)

                for epis in episnumb:
                  for p in epis.find_all('a', href = True):
                    epislink = "https:" + p['href']

                    url5 = str(epislink)
                    results5 = requests.get(url5, headers=headers)
                    soup = BeautifulSoup(results5.text, "html.parser")
                    #print(url5)

                    if soup.find_all('span', attrs= {'style': 'color:black;'}):
                      #print(perepsbox)
                      perepsbox = soup.find_all('span', attrs= {'style': 'color:black;'})
                      perepsboxx = perepsbox[0]
                      for q in perepsboxx.find_all('a', href = True):
                        todownloadpg = "https:" + q['href']

                        url6 = str(todownloadpg)
                        #print(url6)
                        results6 = requests.get(url6, headers=headers)
                        soup = BeautifulSoup(results6.text, "html.parser")
                        if soup.find('div',  class_= 'Singamdasam text-center'):
                          descrbox = soup.find('div', class_= 'Singamdasam text-center')
                          descrdets = descrbox.find_all('td', attrs= {'class': 'desc_value'})
                          size = descrdets[1].text
                          duration = descrdets[2].text
                          sizelist.append(size)
                          duralist.append(duration)
                        else:
                          continue
                    else:
                      continue
        else:
          continue

        sodesperseason = sum(numpgperseason)
        episodes.append(sodesperseason)
        numpgperseason = []
        #numper = sum(numseason)
        #numseason= []
        
      
      if sizelist != [] and duralist != []:
        for i in sizelist:
          w = sizelist.index(i)
          j = i[0:-2]
          j = float(j)
          sizelist[w] = j
        for i in duralist:
          w = duralist.index(i)
          j = i.index(':')
          x = i[0:j]
          x = int(x)
          duralist[w] = x

        #print(duralist)
        #duralist = pd.DataFrame(duralist)
        #sizelist = sizelist.map(lambda x: x.rstrip('MB'), sizelist)
        #sizelist = pd.to_numeric(sizelist, errors='coerce')
        #duralist = duralist.str.replace(':', '.').astype(float)
        sizesum = round(sum(sizelist), 2)
        durasum = sum(duralist)
        avg_size = sizesum / len(sizelist)
        avg_size = round(avg_size, 2)
        avg_duration = durasum / len(duralist)
        avg_duration = round(avg_duration, 2)
        sizesum = round(sizesum / 1024, 2)
        sizelist = []
        duralist = []

        avgsize.append(avg_size)
        totsize.append(sizesum)
        avgtime.append(avg_duration)
        tottime.append(durasum)

        #episodes.append(numper)
        print(episodes)
      else:
        years.append('unknown')
        status.append('unknown')
        episodes.append('unknown')
        totsize.append('unknown')
        tottime.append('unknown')
        avgsize.append('unknown')
        avgtime.append('unknown')
    anime = pd.DataFrame({
      'Anime': titles,
      'Year_released': years,
      'Status': status,
      'Episodes': episodes,
      'Total_size_GB': totsize,
      'Total_duration_mins': tottime,
      'Average_size_mb': avgsize,
      'Average_time_mins': avgtime
    })
    anime.to_csv('Cartoonsarea japanese dub.csv', mode='a', index=True, header=False)





