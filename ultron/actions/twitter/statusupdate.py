import os

from ultron.actions import Action
from ultron.helpers.twitter_helper import load_api


class StatusUpdate(Action):
    def __init__(self, media_file=None, text=None):
        self.api = load_api()
        self.status_update_status = False
        self.media_file = media_file
        self.text = text

    def pre_execute(self):
        if self.media_file is not None:
            if not os.path.exists(self.media_file):
                raise FileNotFoundError

    def execute(self):
        """
        Tweet from authenticated user account .
        """
        if self.media_file is not None:
            self.api.update_with_media(filename=self.media_file,
                                       status=self.text)
        else:
            self.api.update_status(status=self.text)
        self.status_update_status = True

    def post_execute(self):
        if self.status_update_status:
            print('Status Updated')
