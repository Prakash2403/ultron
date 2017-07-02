import os
import pwd

from ultron.actions.search_file import Search


if __name__ == '__main__':
    Search('test.txt',
           os.path.expanduser('/home/' +
                              pwd.getpwuid(os.getuid()).pw_name +
                              '/Desktop/test')
           ).execute()
