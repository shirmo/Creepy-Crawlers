from bs4 import BeautifulSoup
import articleObject as ac
import requests
import json
import time

NUM_PAGES = 25  # 25*12 == 300
START_URL = 'https://www.kickstarter.com/discover/advanced?category_id=16&woe_id=0&sort=magic&seed=2727457&page='
SLEEP_TIME_BETWEEN_REQUESTS = 3


def main():
    article_objects = []

    for page in range(1, NUM_PAGES + 1):
        main_page_url = f'{START_URL}{page}'
        main_page_html = requests.get(main_page_url).text
        main_page_soup = BeautifulSoup(main_page_html, 'lxml')
        articles = main_page_soup.find_all('div', class_="js-react-proj-card grid-col-12 grid-col-6-sm grid-col-4-lg")

        for article in articles:
            article_object = ac.ArticleObject(article)
            article_objects.append(article_object)
            time.sleep(SLEEP_TIME_BETWEEN_REQUESTS)

    json_list = [article.get_article_details() for article in article_objects]
    json_dict = {"records": {"record": json_list}}

    with open("sample.json", "w") as outfile:
        json.dump(json_dict, outfile, indent=2)


if __name__ == "__main__":
    main()
