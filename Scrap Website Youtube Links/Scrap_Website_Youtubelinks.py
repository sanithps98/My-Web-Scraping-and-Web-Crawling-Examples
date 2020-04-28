from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('/home/sanithps98/PROJECTS/Web Scraping & Web Crawling Examples/cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['HEADLINES', 'SUMMARY', 'VIDEO LINK'])

#Analyse the html code of the webpage in order to find where the youtube links are present 

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        # Try-Except Block is used to handle the case when the youtube link is not present
        # and the parser could not come out of the loop because of the non-availability of the link
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()

df = pd.read_csv('/home/sanithps98/PROJECTS/Web Scraping & Web Crawling Examples/cms_scrape.csv')
print(df)
