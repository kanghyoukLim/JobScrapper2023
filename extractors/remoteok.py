import requests
from bs4 import BeautifulSoup

def extract_jobs(term):
#  term=("react")
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  
  if request.status_code == 200:
    results = []
    soup = BeautifulSoup(request.text, "html.parser")
  
    jobs = soup.find_all('td', class_='company')
    
    for job_section in jobs:
      job_posts = job_section.find("h2")
      company = job_section.find("h3")
      regions = job_section.find("div", class_="location")
      region = str(regions)
      link = job_section.find("a", class_="preventLink")
      
  #    print(job_posts.string)
  #    print(company.string)
  #    print(region[24:-6])
  
      job_data = {
        'company' : company.string,
        'location' : region[24:-6],
        'position' : job_posts.string,
        "link": link
      }
      results.append(job_data)
    return results
    
  else:
    print("Can't get jobs.")
