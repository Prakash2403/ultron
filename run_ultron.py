import os

from ultron.ui import BaseInterpreter
from ultron.ui.twitter import Twitter
from ultron.ui.youtube import Youtube


class RunUltron(BaseInterpreter):
    def __init__(self):
        super().__init__()
        self.prompt = "Ultron>>> "

    def do_youtube(self, *args):
        Youtube().cmdloop()

    def do_twitter(self, *args):
        Twitter().cmdloop()


if __name__ == '__main__':
    os.environ['PROJECT_DIR'] = os.path.dirname(os.path.abspath(__file__))
    try:
        RunUltron().cmdloop()
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        print("Goodbye")
        exit(0)
