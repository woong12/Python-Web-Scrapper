# 1.요청
# 2.응답
# 3.응답 파싱
# 4.데이터를 원하는대로 만지기

# 다운로드한 library 포함
from requests import get # http 요청을 위해 lib
from bs4 import BeautifulSoup # 응답 결과를 파싱 하여 가공하기 위한 lib

# 요청 사이트 url
main_url = "https://weworkremotely.com/remote-jobs/search?term="
# 검색할 키워드
search_term = "python"

# 요청후 응답 받기
response = get(f"{main_url}{search_term}")

# 응답에 따른 분기문
if not response.status_code == 200:
    print("Can't request the website!")
else:
    # html을 파싱하여 결과 받기
    soup = BeautifulSoup(response.text ,"html.parser")
    # 결과에서 원하는 데이터 추출
    results = []
    jobs = soup.find_all('section', class_="jobs")
    for job_section in jobs:
        job_posts = job_section.find_all('li')
        job_posts.pop(-1) # 마지막 요소 제거
        for post in job_posts:
            anchors = post.find_all('a')
            anchor = anchors[1]
            link = anchor['href']
            company, kind, region = anchor.find_all('span', class_="company")
            title = anchor.find('span', class_='title')
            job_data = {
                'company': company.string,
                'region': region.string,
                'position': title.string,
            }
            results.append(job_data)
    for result in results:
        print(result)
        print("//////////////////")