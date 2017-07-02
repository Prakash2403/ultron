from tweepy import TweepError
from ultron.actions import Action
from ultron.helpers.twitter_helper import load_api


class SearchUsers(Action):
    def __init__(self):
        self.api = load_api()
        self.users = None
        self.search_user_status = True

    def pre_execute(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        """
        Search users based on keyword.
        :param args: Currently, no use.
        :param kwargs: keyword arguments, only 'text'
        is accepted, which indicates the query
        to be searched
        :return: None
        """
        try:
            self.users = self.api.search_users(kwargs['query'], 20, 1)
        except TweepError as search_error:
            print(search_error)
            self.search_user_status = False

    def post_execute(self, *args, **kwargs):
        print('Search results for '+kwargs['text'])
        for user in self.users:
            print("Screen Name: @" + user.screen_name)
            print("User Name: " + user.name)
            print()
