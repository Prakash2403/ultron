from tweepy import TweepError
from ultron.actions import Action
from ultron.helpers.twitter_helper import load_api


class SendMessage(Action):
    def __init__(self):
        self.api = load_api()
        self.send_message_status = True

    def pre_execute(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        """
        Sends a text message to your follower.
        :param args: Currently, no use.
        :param kwargs: keyword arguments, only 'screen_name'
        and 'text' are accepted, where 'screen_name' is screen
        name of receiver and 'text' is the text message you want
        to send.
        :return: None
        """
        try:
            self.api.send_direct_message(screen_name=kwargs['screen_name'],
                                         text=kwargs['text'])
        except TweepError as send_message_error:
            print(send_message_error)
            self.send_message_status = False

    def post_execute(self, *args, **kwargs):
        if self.send_message_status:
            print('Message sent')
