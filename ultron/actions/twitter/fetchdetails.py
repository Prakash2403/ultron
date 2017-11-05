from tweepy import TweepError

from ultron.actions import Action
from ultron.exception.twitterexceptions import InvalidUserException
from ultron.helpers.twitter_helper import load_api


class FetchDetails(Action):
    def __init__(self, screen_name):
        self.api = load_api()
        self.fetch_details_status = False
        self.details = None
        self.screen_name = screen_name

    def pre_execute(self):
        pass

    def execute(self):
        """
        Fetch details about given user.
        """
        try:
            self.details = self.api.get_user(screen_name=self.screen_name)
        except TweepError:
            raise InvalidUserException
        self.fetch_details_status = True

    def post_execute(self):
        print('Name :' + str(self.details.name))
        print('Descriptions :' + str(self.details.description))
        print("Followers :" + str(self.details.followers_count))
        print("Friends :" + str(self.details.friends_count))
        print("URL :" + str(self.details.url))
        print("ID string :" + str(self.details.id_str))
        print("Screen name :" + str(self.details.screen_name))
