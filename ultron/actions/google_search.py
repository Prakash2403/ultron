import webbrowser

from ultron.actions import Action
from google import google


class GoogleSearch(Action):
    def __init__(self, search_query):
        self.search_query = search_query

    def pre_execute(self):
        pass

    def execute(self, *args, **kwargs):

        """
        Here all the Links and the Names, that are available on the first page of Google Search,
        of a given query are displayed.
        The user chooses which link to open and that link is opened in a new tab of
        the default web browser using the webbrowser module
        """

        search_results = google.search(self.search_query, 1)

        if len(search_results) == 1:
            result_stat = "1 result found"
        else:
            result_stat = str(len(search_results))+" results found"
        print(result_stat+"\n")

        tmp = 1
        for each_pair in search_results:
            print(str(tmp) + ".) " + each_pair.name)
            print(each_pair.link)
            print()
            tmp = tmp + 1

        if len(search_results) > 0:
            print("__________________________________________________"
                  "____________________________________________________________\n")
            i = int(input("Enter the link number to be open\n"))
            webbrowser.open(search_results[i - 1].link)
        pass

    def post_execute(self):
        pass
