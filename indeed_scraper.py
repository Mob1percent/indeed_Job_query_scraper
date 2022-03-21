import requests
from bs4 import BeautifulSoup

keys = ['co-op','intern','internship','coop']
keys2=['software','computer','developer']
## needed info (Comany,Discipline,City,Job_title,Level,Link)
def extract(type,city,page):
  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
  indeed_softwaredeveloper_URL = f'https://ca.indeed.com/jobs?q={type}&l={city}&start={page}'
  r = requests.get(indeed_softwaredeveloper_URL, headers)
  soup = BeautifulSoup(r.content, 'html.parser')
  return soup

def transform(soup):
   #planning to write a if-else statement that read title and check if it said 'software developer etc'-software discipline or 'power engnieer etc' - hardware discipline
  #level = 'full-time'  #planning to write a if-else statement that read title and check if it said 'coop' or 'intern' to declare it as intern-level
  for EachPart in soup.select('a[class*="tapItem fs-unmask result job"]'):
      (EachPart.get_text())
      part=EachPart['href']
      url='ca.indeed.com'+part
  divs = soup.find_all('div', class_ = 'job_seen_beacon')
  for item in divs:
    title = item.find('h2').text
    company = item.find('span',class_ ='companyName').text
    companylocation = item.find('div',class_ = 'companyLocation').text
    if (any(key in title.lower() for key in keys)):
        level = 'intern'
    else:
        level = 'Full-time'
    if(any(key in title.lower() for key in keys2)):
        discipline = 'software'
    else:
        discipline ='hardware'
    job ={
      'company':company,
      'Discipline':discipline,
      'location':companylocation,
      'title':title,
      'level':level,
      'URL':url
    }
    joblist.append(job)
  return
  #job url is in different subset of div. So far not sure how to get it
#  divs2 = soup.find_all('div', class_ ='mosaic-provider-jobcards')
#  for item2 in divs2:
#    url = item.find('section', class_ ='data-aoclk').text
#    print(url)


joblist =[]

c = extract('software%20developer%20intern','toronto', 0)
transform(c)
print(joblist)