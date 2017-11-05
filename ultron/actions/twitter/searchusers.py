from ultron.actions import Action
from ultron.helpers.twitter_helper import load_api


class SearchUsers(Action):
    def __init__(self, query):
        self.api = load_api()
        self.users = None
        self.query = query
        self.search_user_status = False

    def pre_execute(self):
        pass

    def execute(self):
        """
        Search users based on keyword.
        """
        self.users = self.api.search_users(self.query, 20, 1)
        self.search_user_status = True

    def post_execute(self):
        print('Search results for '+self.query)
        for user in self.users:
            print("Screen Name: @" + user.screen_name)
            print("User Name: " + user.name)
            print()
