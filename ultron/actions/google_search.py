from ultron.actions import Action
import webbrowser

class googleSearch(Action):
    def __init__(self):
        self.search_engine = 'http://www.google.com/?#q='
        self.search_query = ''

    def execute(self, search_query, **kwargs):
        self.search_query = search_query
        webbrowser.open_new_tab(self.search_engine + search_query)
        pass

    def pre_execute(self):
        pass

    def post_execute(self):
        #Close the newly opened Tab
        pass