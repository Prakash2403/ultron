from tweepy import TweepError
from ultron.actions import Action
from ultron.helpers.twitter_helper import load_api


class HomeTimeLine(Action):
    def __init__(self):
        self.api = load_api()
        self.status_list = None
        self.home_timeline_status = True

    def pre_execute(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        """
        Retrieves latest 20 tweets on your timeline.
        :param args: currently, not using.
        :param kwargs: currently, not using
        :return: None
        """
        try:
            self.status_list = self.api.home_timeline()
        except TweepError as home_timeline_error:
            print(home_timeline_error)
            self.home_timeline_status = False

    def post_execute(self, *args, **kwargs):
        for status in self.status_list:
            print(status.text + "    " + status.author.screen_name)
