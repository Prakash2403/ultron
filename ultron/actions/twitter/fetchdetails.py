from tweepy import TweepError
from ultron.actions import Action
from ultron.helpers.twitter_helper import load_api


class FetchDetails(Action):
    def __init__(self):
        self.api = load_api()
        self.fetch_details_status = True
        self.details = None

    def pre_execute(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        """
        Fetch details about given user.
        :param args: Currently, no use.
        :param kwargs: keyword arguments, only 'screen_name'
        is accepted, where 'screen_name' is screen
        name of target user.
        :return: None
        """
        try:
            self.details = self.api.get_user(screen_name=kwargs['screen_name'])
        except TweepError as fetch_details_error:
            print(fetch_details_error)
            self.fetch_details_status = False

    def post_execute(self, *args, **kwargs):
        print('Name :' + self.details.name)
        print('Descriptions :' + self.details.description)
        print("Followers :" + str(self.details.followers_count))
        print("Friends :" + str(self.details.friends_count))
        print("URL :" + self.details.url)
        print("ID string :" + self.details.id_str)
        print("Screen name :" + self.details.screen_name)
