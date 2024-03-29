# 1.요청
# 2.응답
# 3.응답 파싱
# 4.데이터를 원하는대로 만지기

# 다운로드한 library 포함
from requests import get # http 요청을 위해 lib
from bs4 import BeautifulSoup # 응답 결과를 파싱 하여 가공하기 위한 lib

def extract_wwr_jobs(keyword):
    # 요청 사이트 url
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
    # 요청후 응답 받기
    response = get(f"{base_url}{keyword}")
    # 응답에 따른 분기문
    if response.status_code != 200:
        print("Can't request the website!")
    else:
        # 결과에서 원하는 데이터 추출
        results = []
        # html을 파싱하여 결과 받기
        soup = BeautifulSoup(response.text ,"html.parser")
        jobs = soup.find_all('section', class_="jobs")
        for job_section in jobs:
            job_posts = job_section.find_all('li')
            job_posts.pop(-1) # 마지막 요소 제거
            for post in job_posts:
                anchors = post.find_all('a')
                anchor = anchors[1]
                link = anchor['href']
                company, kind, location = anchor.find_all('span', class_="company")
                title = anchor.find('span', class_='title')
                job_data = {
                    'link': f"https://weworkremotely.com{link}",
                    'company': company.string.replace(",", " "),
                    'location': location.string.replace(",", " "),
                    'position': title.string.replace(",", " "),
                }
                results.append(job_data)
        return results