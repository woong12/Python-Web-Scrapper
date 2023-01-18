from requests import get
from bs4 import BeautifulSoup

main_url = "https://weworkremotely.com/remote-jobs/search?term="

search_term = "python"

response = get(f"{main_url}{search_term}")

if not response.status_code == 200:
    print("Can't request the website!")
else:
    soup = BeautifulSoup(response.text ,"html.parser")
    jobs = soup.find_all('section', class_="jobs")
    for job_section in jobs:
        job_posts = job_section.find_all('li')
        job_posts.pop(-1)
        for post in job_posts:
            print(post)
            print("//////////////")