from bs4 import BeautifulSoup
import sys
import articleObject as cc
import lxml
import requests


def main(htmlFile):
    articlesObj = []
    html = requests.get(htmlFile).text

    soup = BeautifulSoup(html, 'html')
    print(soup.prettify())
    # print(len(soup.find_all('div', class_="bg-white black relative border-grey-500")))
    # articles = soup.find_all()
    # articles = soup.find_all('div')
    # for e in articles:
    #     # if e.__class__ == "bg-white black relative border-grey-500":
    #     print(e)
    # for element, ind in articles.iteritems():
    #     articlesObj.append(cc.articleParams(ind, element))
    # create a big JSON using articlesObj


if __name__ == "__main__":
    # htmlFile = sys.argv[1]
    htmlFile = 'http://www.kickstarter.com/discover/advanced?category_id=16&woe_id=0&sort=magic&seed=2727457&page=6'
    main(htmlFile)
