import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from lxml.html import fromstring


class ArticleObject:
    def __init__(self, bs_obj_main_page):

        self.data_project = json.loads(bs_obj_main_page.get('data-project'))
        self.project_dict = dict()
        self.page_soup = None
        self.properties_dict = None

        self.set_id()
        self.set_url()
        self.set_page_soup_and_properties_dict()
        self.set_creator()
        self.set_title()
        self.set_dollars_pledged()
        self.set_dollars_goal()
        self.set_num_backers()
        self.set_days_to_go()
        self.set_all_or_nothing()
        self.set_text()

    def set_url(self):
        self.project_dict['url'] = self.data_project.get('urls').get('web').get('project')

    def set_id(self):
        self.project_dict['id'] = self.data_project.get('id')

    def set_creator(self):
        self.project_dict['Creator'] = self.data_project.get('creator').get('name')

    def set_title(self):
        self.project_dict['Title'] = self.data_project.get('name')

    def set_text(self):
        session = requests.session()
        html_page = session.get(self.get_url())
        page = fromstring(html_page.content)

        graph_slug = self.get_url().split("projects/")[1].split("?")[0]
        graph_data = [{
            "operationName": "Campaign",
            "variables": {
                "slug": graph_slug
            },
            "query": "query Campaign($slug: String!) {\n  project(slug: $slug) "
                     "{\n    id\n    isSharingProjectBudget\n    risks\n    showRisksTab\n    "
                     "story(assetWidth: 680)\n    currency\n    spreadsheet {\n      displayMode\n      "
                     "public\n      url\n      data {\n        name\n        value\n        phase\n        "
                     "rowNum\n        __typename\n      }\n      dataLastUpdatedAt\n      __typename\n    }\n    "
                     "environmentalCommitments {\n      id\n      commitmentCategory\n      description\n      "
                     "__typename\n    }\n    __typename\n  }\n}\n"
        }]

        csrf_token = page.xpath('//meta[@name="csrf-token"]')[0].get('content')
        headers = dict()
        headers['x-csrf-token'] = csrf_token

        response = session.post("https://www.kickstarter.com/graph", json=graph_data, headers=headers)
        graph_json = response.json()
        story = graph_json[0]['data']['project']['story']
        soup = BeautifulSoup(story, 'lxml')
        self.project_dict['Text'] = soup.text

    def set_dollars_pledged(self):
        self.project_dict['DollarsPledged'] = self.properties_dict.get('project').\
            get('project_current_amount_pledged_usd')

    def set_dollars_goal(self):
        self.project_dict['DollarsGoal'] = self.properties_dict.get('project').get('project_goal_usd')

    def set_num_backers(self):
        self.project_dict['NumBackers'] = self.data_project.get('backers_count')
    
    def set_days_to_go(self):
        today = datetime.now().date()
        end_day = datetime.fromtimestamp(int(self.data_project.get('deadline'))).date()
        self.project_dict['DaysToGo'] = (end_day - today).days - 1

    def set_all_or_nothing(self):
        self.project_dict['AllOrNothing'] = self.properties_dict.get('project').get('project_deadline')

    def set_page_soup_and_properties_dict(self):
        page_html = requests.get(self.get_url()).text
        self.page_soup = BeautifulSoup(page_html, 'lxml')
        properties_script = self.page_soup.find_all('script')[4]
        self.properties_dict = json.loads(properties_script.text.
                                          split('window.ksr_track_properties =')[-1].splitlines()[0])

    def get_article_details(self):
        return self.project_dict

    def get_url(self):
        return self.project_dict['url']
