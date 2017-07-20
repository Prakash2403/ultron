import requests
from bs4 import BeautifulSoup
from ultron.actions import Action


class SearchVideo(Action):
    """
    execute method raises errors and exceptions, so if you are
    using this class anywhere, make sure that you have handled them.

    See execute method documentation for more details.
    """

    def __init__(self, query):
        """

        :param query: query to be searched.
        """
        self.search_results = []
        self.query = query
        self.search_status = True

    def pre_execute(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        """
        Scrapes the first page of youtube search results and store
        the contents in search_results list.

        Raises error(s) if something is wrong with requests or
        network connection

        """
        self.search_status = False
        url = "https://www.youtube.com/results?search_query=" + self.query
        try:
            response = requests.get(url)
        except Exception as e:
            self.search_status = False
            raise e
        html = response.text
        soup = BeautifulSoup(html, "lxml")
        for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
            self.search_results.append(vid)
        self.search_status = True

    def post_execute(self, *args, **kwargs):
        pass

    def get_search_results(self):
        """

        :return: list of search results.
        """
        return self.search_results
