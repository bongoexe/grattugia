from bs4 import BeautifulSoup
import urllib.request
import xlsxwriter

url = "www.example.com"
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0' }
req = urllib.request.Request(url, headers = headers)

with urllib.request.urlopen(req) as response:
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for link in soup.find_all("a"):
        links.append(link.get("href"))

workbook = xlsxwriter.Workbook('links.xlsx')
worksheet = workbook.add_worksheet()
for row, link in enumerate(links):
    worksheet.write(row, 0, link)
workbook.close()
