# pip install bs4
# pip install lxml
import bs4
import urllib.request

URL = "https://www.indeed.co.in/jobs?q=python&l="

response = urllib.request.urlopen(URL)
# print(response)
htmlSourceCode = bs4.BeautifulSoup(response, 'lxml')
# print(htmlSourceCode)
# class -> jobtitle
# tagname -> a
heading = htmlSourceCode.find('a', 'jobtitle')
print(heading.text)
companyName = htmlSourceCode.find('span', 'company')
print(companyName.text)
jobSummary = htmlSourceCode.find('div', 'summary')
print(jobSummary.text)
