from bs4 import BeautifulSoup
import sys
import articleObject as cc
import requests
import json


def main(htmlFile):
    articlesObj = []
    html = requests.get(htmlFile).text

    soup = BeautifulSoup(html, 'lxml')
    articles = soup.find_all('div', class_="js-react-proj-card grid-col-12 grid-col-6-sm grid-col-4-lg")
    for article in articles:
        articlesObj.append(cc.articleParams(article))
    jsonList = []
    for article in articlesObj:
        jsonList.append(article.getJson())
    jsonDict = {"records": {"record": jsonList}}
    # json_object = json.dumps(jsonDict, indent=4)
    with open("sample.json", "w") as outfile:
        json.dump(jsonDict, outfile)
    # print(json_object)

if __name__ == "__main__":
    # htmlFile = sys.argv[1]
    htmlFile = 'https://www.kickstarter.com/discover/advanced?category_id=16&woe_id=0&sort=magic&seed=2727457&page=1'
    main(htmlFile)
