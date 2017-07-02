from tweepy import TweepError
from ultron.actions import Action
from ultron.helpers.twitter_helper import load_api


class StatusUpdate(Action):
    def __init__(self):
        self.api = load_api()
        self.status_update_status = True

    def pre_execute(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        """
            Tweet from authenticated user account .
            :param args: Currently, no use.
            :param kwargs: keyword arguments, only 'filename'
            and 'text' are accepted, where 'filename' is absolute
            path to media file to be uploaded as tweet.
            Note that, file must be present on local
            machine.
            'text' contains the text to be uploaded as tweet.
            :return: None
        """
        try:
            if kwargs.get('filename', None) is not None:
                self.api.update_with_media(filename=kwargs['filename'],
                                           status=kwargs.get('text', None))
            else:
                self.api.update_status(status=kwargs['text'])

        except TweepError as status_update_error:
            print(status_update_error)
            self.status_update_status = False

    def post_execute(self, *args, **kwargs):
        if self.status_update_status:
            print('Status Updated')
