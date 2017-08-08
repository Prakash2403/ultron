"""
The base class for all actions.
For defining a new action, inherit this class, then define all the associated methods.
"""
from abc import abstractmethod, ABC


class Action(ABC):

    @abstractmethod
    def execute(self, *args, **kwargs):
        return

    @abstractmethod
    def post_execute(self, *args, **kwargs):
        return

    @abstractmethod
    def pre_execute(self, *args, **kwargs):
        return

    def run(self):
        self.pre_execute()
        self.execute()
        self.post_execute()
