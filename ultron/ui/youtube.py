import os

from ultron.actions.youtube.downloadvideo import DownloadVideo
from ultron.exception import NotAbsolutePathException, UnknownException
from ultron.helpers.memory_loader import Default
from ultron.ui import BaseInterpreter


class Youtube(BaseInterpreter):
    def __init__(self):
        super().__init__()
        self.prompt = "Youtube>> "
        self.memory = Default.load_defaults()

    def do_download_video(self, *args):
        query = input("Enter search keyword\n")
        storage_directory = os.path.expanduser(input("Where do you want to save your file."
                                                     " Leave blank to save in ~/Downloads.\n"))
        filename = input(
            "Enter a custom file name. Leave blank to use auto-generated filename.\n")
        if len(storage_directory.strip()) == 0:
            storage_directory = os.path.expanduser(
                self.memory.get('VIDEO_STORAGE_DIRECTORY'))
        if len(filename.strip()) == 0:
            filename = None
        video_downloader = DownloadVideo(query=query,
                                         filename=filename,
                                         storage_directory=storage_directory)
        Youtube.run(video_downloader)

    @staticmethod
    def run(youtube_obj):
        try:
            youtube_obj.run()
        except FileExistsError:
            print('File with same name exists in '
                  'destination directory.')
        except PermissionError:
            print("You don't have permission to "
                  "access the files in destination directory.")
        except NotAbsolutePathException:
            print("Destination directory path is not absolute.")
        except IndexError:
            print("Wrong choice. Please retry.")
        except UnknownException:
            #  If this block is being executed,
            #  then LOL, you are screwed.
            print('Unknown exception occurred. Please retry.')
