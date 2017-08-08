from tweepy import TweepError

from ultron.actions import Action
from ultron.exception.twitterexceptions import InvalidUserException
from ultron.helpers.twitter_helper import load_api


class SendMessage(Action):
    def __init__(self, screen_name, text):
        self.api = load_api()
        self.screen_name = screen_name
        self.text = text
        self.send_message_status = False

    def pre_execute(self):
        pass

    def execute(self):
        """
        Sends a text message to your follower.
        """
        try:
            self.api.send_direct_message(screen_name=self.screen_name,
                                         text=self.text)
        except TweepError:
            raise InvalidUserException
        self.send_message_status = True

    def post_execute(self):
        if self.send_message_status:
            print('Message sent')
