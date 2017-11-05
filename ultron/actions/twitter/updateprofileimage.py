import os
from ultron.actions import Action
from ultron.exception import NotAbsolutePathException
from ultron.helpers.twitter_helper import load_api


class UpdateProfileImage(Action):
    def __init__(self, filename):
        self.api = load_api()
        self.update_profile_status = False
        self.filename = filename

    def pre_execute(self):
        if self.filename is not None:
            if not os.path.abspath(self.filename):
                raise NotAbsolutePathException
            if not os.path.exists(self.filename):
                raise FileNotFoundError

    def execute(self):
        """
        Updates the profile image of authenticated user.
        """
        self.api.update_profile_image(filename=self.filename)
        self.update_profile_status = True

    def post_execute(self):
        if self.update_profile_status:
            print('Updated Profile Picture')
