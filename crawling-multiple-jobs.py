from bs4 import BeautifulSoup as BS
from urllib.request import urlopen

URL = "https://www.indeed.co.in/jobs?q=python&l="

response = urlopen(URL)
htmlSourceCode = BS(response, 'lxml')

jobs = htmlSourceCode.find_all(
    'div', 'jobsearch-SerpJobCard')
print(len(jobs))
# print(jobs)
for job in jobs:
    heading = job.find('a', 'jobtitle')
    print("Job Title - ", heading.text.strip())
    companyName = job.find('span', 'company')
    print("Company name - ", companyName.text.strip())
    jobSummary = job.find('div', 'summary')
    print("Job Summary - ", jobSummary.text.strip())
    jobLocation = job.find('div', 'location')
    jobLocation = jobLocation if jobLocation else job.find('span', 'location')
    print("Job Location - ", jobLocation.text.strip())
    salary = job.find('span', 'salaryText')
    salary = salary.text.strip() if salary else "Salary Not Specified"
    print("Salary - ", salary)
    print("*********************************")
