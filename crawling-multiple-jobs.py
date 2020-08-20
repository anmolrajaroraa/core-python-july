from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
from urllib.parse import urlencode
from babel.numbers import format_currency
from money import Money

query = input("Job title, keywords or company name: ")
salary = input("Min annual salary: ")
m = Money(salary, 'INR')
salary = m.format('hi_IN')
# salary = format_currency(salary*12, "INR")
query = query + salary[:-3]
location = input("Location: ")
URL = f"https://www.indeed.co.in/jobs?"
URL = URL + urlencode({"q": query, "l": location})
print(URL)

response = urlopen(URL)
htmlSourceCode = BS(response, 'lxml')

jobs = htmlSourceCode.find_all(
    'div', 'jobsearch-SerpJobCard')
print(len(jobs))
# print(jobs)
for counter, job in enumerate(jobs):
    heading = job.find('a', 'jobtitle')
    print((counter + 1), ". Job Title - ", heading.text.strip())
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
