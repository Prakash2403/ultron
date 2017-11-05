from ultron.ui import BaseInterpreter
from ultron.ui.twitter import Twitter
from ultron.ui.youtube import Youtube


class UltronCLI(BaseInterpreter):
    def __init__(self):
        super().__init__()
        self.prompt = "Ultron>>> "

    def do_youtube(self, *args):
        Youtube().cmdloop()

    def do_twitter(self, *args):
        Twitter().cmdloop()
