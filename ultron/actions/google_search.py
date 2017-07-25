from ultron.actions import Action
import requests
from bs4 import BeautifulSoup


class GoogleSearch(Action):
    def __init__(self, search_query):
        self.search_query = search_query
        self.links = []
        self.names = []

    def pre_execute(self):
        pass

    def execute(self, *args, **kwargs):

        url = 'http://www.google.co.in/search?q='\
              +self.search_query.replace(' ', '+')

        res = requests.get(url)
        web_data = BeautifulSoup(res.text, "lxml")

        tags = web_data.find_all('h3')

        for each_tag in tags:

            link = each_tag.find_all('a')

            if(len(link) > 0):
                self.names.append(each_tag.text)
                self.links.append(link[0].get('href')
                                  .replace('/url?q=', ''))
        pass

    def post_execute(self):
        pass

    def get_links(self):
        return self.links

    def get_names(self):
        return self.names
