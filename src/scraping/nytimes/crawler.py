import datetime, time
import pprint
from urllib import request, response, error, parse
from urllib.request import urlopen
from bs4 import BeautifulSoup, NavigableString, CData, Tag
import jsonlines
import re
import pandas as pd
import uuid
import jsonlines
import time

from covid_scraping import test_jsonlines
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--rescrape",action='store_true')
args = parser.parse_args()
diff = ''
if args.rescrape:
    diff = 'stage/'

def crawl():
    name = 'NYTimes'
    url = 'https://www.nytimes.com/interactive/2020/world/coronavirus-tips-advice.html'
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    questions, answers = [], []
    for panelgroup in soup.findAll("div", {"class": "g-question-wrap"}):
        q = panelgroup.find('h3').getText()
        a = ''.join(panelgroup.find('div', {'class': "g-answer-wrap"}).getText().splitlines())
        questions.append(q)
        answers.append(a)

    lastUpdateTime = time.mktime(time.strptime(soup.find('time').getText(), "Updated %B %d, %Y"))

    faq = []
    for question, answer in zip(questions, answers):
        faq.append({
            'sourceUrl': url,
            'sourceName': name,
            "dateScraped": time.time(),
            "sourceDate": None,
            "lastUpdateTime": lastUpdateTime,
            "needUpdate": True,
            "containsURLs": "https://" in answer or "http://" in answer,
            "typeOfInfo": "QA",
            "isAnnotated": False,
            "responseAuthority": "",
            "questionUUID": str(uuid.uuid1()),
            "answerUUID": str(uuid.uuid1()),
            "exampleUUID": str(uuid.uuid1()),
            "questionText": question,
            "answerText": answer,
            "hasAnswer": True,
            "targetEducationLevel": "NA",
            "topic":"",
            "extraData": {},
        })

    with jsonlines.open('../../../data/scraping/schema_v0.1/' + diff + 'NYTimes_v0.1.jsonl', 'w') as writer:
            writer.write_all(faq)

    test_jsonlines('../../../data/scraping/schema_v0.1/' + diff + 'NYTimes_v0.1.jsonl')
    
if __name__ == "__main__":
    crawl()
