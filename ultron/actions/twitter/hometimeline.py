from ultron.actions import Action
from ultron.helpers.twitter_helper import load_api


class HomeTimeLine(Action):
    def __init__(self):
        self.api = load_api()
        self.status_list = None
        self.home_timeline_status = False

    def pre_execute(self):
        pass

    def execute(self):
        """
        Retrieves latest 20 tweets on your timeline.
        """
        self.status_list = self.api.home_timeline()
        self.home_timeline_status = True

    def post_execute(self, *args, **kwargs):
        for status in self.status_list:
            print(status.text + "    " + status.author.screen_name + "\n")
