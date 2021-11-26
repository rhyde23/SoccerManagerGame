import requests, re, pickle, html
from bs4 import BeautifulSoup

def build_link(league_number) :
	return 'https://www.fifaindex.com/teams/fifa21/?league='+league_number

def scrape(link) :
    page = requests.get(link)
    soup = html.unescape(str(BeautifulSoup(page.content, 'html.parser')))
    return soup

def main() :
	link = build_link('61')
	soup = scrape(link)
	#print(soup)
	#quit()
	found = {f.split('\"')[-2][:-8]:re.findall('[0-9]+', f)[0] for f in re.findall('href=\"/team/[0-9]+/[^/]+/[^/]+/\" title=\"[^"]+\"', soup)}
	return found

print(main())
