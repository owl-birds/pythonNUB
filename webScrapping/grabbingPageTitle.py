import requests
# get a webpage through a requests
result = requests.get("http://example.com")
print(type(result))
# seeing the page html
# print(result.text)
# print(type(result.text))
import bs4
soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup)
print(type(soup))
# selecting the html tag for the title
print(soup.select("title")[0].getText())
# grabbing html tag for paragraph (<p></p>)
siteParagraph = soup.select("p")
print(type(siteParagraph[0]))
print(siteParagraph[0].getText())
