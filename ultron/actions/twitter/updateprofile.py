from ultron.actions import Action
from ultron.helpers.twitter_helper import load_api


class UpdateProfile(Action):
    def __init__(self, profile_data=None):
        self.api = load_api()
        self.update_profile_status = False
        self.profile_data = profile_data

    def pre_execute(self):
        pass

    def execute(self):
        """
        Updates profile of authenticated user.
        """
        self.api.update_profile(name=self.profile_data.get('name', None),
                                location=self.profile_data.get(
                                    'location', None),
                                url=self.profile_data.get('url', None),
                                description=self.profile_data.get('description', None))
        self.update_profile_status = True

    def post_execute(self):
        if self.update_profile_status:
            print("Profile updated")
