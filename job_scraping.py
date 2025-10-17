from bs4 import BeautifulSoup
import requests
import time

JOB_BOARD_URL = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=java&txtLocation='
RUN_FOR_EVERY_MIN = 10

def find_jobs():
    html_text = requests.get(JOB_BOARD_URL).text
    soup = BeautifulSoup(html_text,'lxml')
    # print(soup)
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for job in jobs:
        # print(job.text)
        posted_date = job.find('span', class_ = 'sim-posted').span.text
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
        skills = job.find('div',class_ = 'srp-skills').text.replace(' ','')
        job_link = job.a['href']
        print(job_link)

if __name__ == '__main__':
    while True:
        find_jobs()
        time.sleep(RUN_FOR_EVERY_MIN*60)
        print('____________________________________________')