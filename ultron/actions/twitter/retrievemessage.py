from tweepy import TweepError
from ultron.actions import Action
from ultron.helpers.twitter_helper import load_api


class RetrieveMessage(Action):
    def __init__(self):
        self.api = load_api()
        self.retrieve_message_status = True
        self.messages = None

    def pre_execute(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        """
        Retrieves all text messages sent to current user.
        :param args: Currently, no use.
        :param kwargs: Currently, no use.
        :return: None
        """
        try:
            self.messages = self.api.direct_messages(fulltext=True)
        except TweepError as retrieve_message_error:
            print(retrieve_message_error)
            self.retrieve_message_status = False
        self.post_execute()

    def post_execute(self, *args, **kwargs):
        if self.retrieve_message_status:
            print(self.messages)
