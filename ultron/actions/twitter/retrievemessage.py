from ultron.actions import Action
from ultron.helpers.twitter_helper import load_api


class RetrieveMessage(Action):
    def __init__(self):
        self.api = load_api()
        self.retrieve_message_status = False
        self.messages = None

    def pre_execute(self):
        pass

    def execute(self):
        """
        Retrieves all text messages sent to current user.
        """
        self.messages = self.api.direct_messages(fulltext=True)
        self.retrieve_message_status = True

    def post_execute(self):
        if self.retrieve_message_status:
            for message in self.messages:
                print("Message:- " + message.text)
                print("Sender:- " + str(message.sender.name))
                print("Date:- " + str(message.created_at.date()))
                print("Time:- " + str(message.created_at.time()))
                print()
