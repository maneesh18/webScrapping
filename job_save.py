from bs4 import BeautifulSoup
import requests

JOB_BOARD_URL = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=java&txtLocation='

def find_jobs():
    html_text = requests.get(JOB_BOARD_URL).text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        posted_date = job.find('span', class_ = 'sim-posted').span.text
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
        skills = job.find('div',class_ = 'srp-skills').text.split()
        job_link = job.a['href']
        if 'few' in posted_date:
            with open(f'posts/job_{index}.txt','w') as f:
                f.write(f"Company Name: {company_name.strip()}\n")
                f.write(f"Skills: {skills}\n")
                f.write(f"Job link: {job_link}\n")
            print(f"Job number {index} saved as file named - job_{index}.txt")


if __name__ == '__main__':
    find_jobs()