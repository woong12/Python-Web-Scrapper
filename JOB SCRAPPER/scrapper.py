from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from extractors.wwr import extract_wwr_jobs
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options=options)

def get_page_count(keyword):
    base_url = 'https://kr.indeed.com/jobs?q='
    browser.get(f"{base_url}{keyword}")

    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("ul", class_="pagination-list")
    if pagination == None:
        return 1
    pages = pagination.find_all("li", recursive = False)
    print(len(pages))

get_page_count("nest")


def extract_indeed_jobs(keyword):
    base_url = "https://kr.indeed.com/jobs?q="
    browser.get(f"{base_url}{keyword}")

    results = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    job_list = soup.find('ul', class_= "jobsearch-ResultsList css-0")
    jobs = job_list.find_all('li', recursive = False)
    #ul 바로밑 li만을 찾아낼 것이다
    for job in jobs:
        zone = job.find("div", class_="mosaic-zone")
        #find는 찾은 element를 주거나 None을 준다
        if zone == None:#job li에서 job을 추출한다
            anchor = job.select_one("h2 a")
            title = anchor['aria-label']
            link = anchor['href']
            company = job.find("span",class_="companyName")
            region = job.find("div",class_="companyLocation")
            job_data = {
                'link' : f"https://www.indeed.com{link}",
                'company' : company.string,
                'location' : region.string,
                'position' : title
            }
            results.append(job_data)
    for result in results:
        print(result, "\n//////\n")

while (True):
    pass