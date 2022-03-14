import requests
from bs4 import BeautifulSoup


## needed info (Comany,Discipline,City,Job_title,Level,Link)
def extract(city,page):
  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}
  indeed_softwaredeveloper_URL = f'https://ca.indeed.com/jobs?q=software%20developer&l={city}&start={page}'
  r = requests.get(indeed_softwaredeveloper_URL, headers)
  return r.status_code

print(extract('Markham', 0))