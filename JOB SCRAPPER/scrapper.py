# from requests import get
# from bs4 import BeautifulSoup
# from extractors.wwr import extract_wwr_jobs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

browser.get("https://kr.indeed.com/jobs?q=python&limit=50")

print(browser.page_source)

while (True):
    pass
"""
jobs = extract_wwr_jobs("python")

base_url = "https://kr.indeed.com/jobs?q="
search_terms = "python"

response = get(f"{base_url}{search_terms}")

if response.status_code != 200:
    # 현재 indeed에서 스크래핑 막음
    print("Cant request page")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    job_list = soup.find("ul", class_="jobsearch-ResultsList")
    jobs = job_list.find_all('li', recursive=False)
    for job in jobs:
        print(job)
        print("//////")
"""