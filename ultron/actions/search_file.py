import os
from fnmatch import fnmatch

from ultron.actions import Action


class Search(Action):
    class FileObject(object):
        def __init__(self, file_path):
            self.file_path = file_path
            self.file = file_path.split('/').pop()

        def match(self, file):
            """
            Function to check match for file.
            :return: True if matched else False.
            """
            return fnmatch(self.file, file)

    def __init__(self, file, path='/home'):
        """
        Initialize object for searching.
        :param path: Path to start looking.
        :param file: File to search in given path.
        """
        self.path = path
        self.file = file
        self.matched_files = []
        self.matched_paths = []

    def pre_execute(self):
        """
        This will generate a iterable for searching.
        :return: Iterable to search the matches for file.
        """
        for root, dirs, files in os.walk(self.path):
            for directory in dirs:
                for filename in directory:
                    filename = os.path.join(root, filename)
                    if os.path.isfile(filename) or os.path.isdir(filename):
                        yield self.FileObject(filename)

            for filename in files:
                filename = os.path.join(root, filename)
                if os.path.isfile(filename) or os.path.isdir(filename):
                    yield self.FileObject(filename)

    def execute(self):
        """
        This will actually search for file
        and generate a iterable of matches
        which will be printed in post_execute().
        :return: No returns.
        """
        for file in self.pre_execute():
            if file.match(self.file):
                self.matched_files.append(file.file)
                self.matched_paths.append(file.file_path)
        self.post_execute()

    def post_execute(self):
        """
        This will print out all the found items.
        :return: No returns.
        """
        if not self.matched_files:
            print('Sorry No matches')
        else:
            print('The matches for your file are:')
            for i in range(len(self.matched_files)):
                print(str(i+1), '\b.', self.matched_files[i], 'at:')
                print('\t', self.matched_paths[i])
