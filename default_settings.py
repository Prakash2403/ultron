import json

import os


def default_settings():
    os.environ['ULTRON_PROJECT_DIR'] = os.path.dirname(
        os.path.abspath(__file__))
    defaults = {'VIDEO_STORAGE_DIRECTORY': os.path.expanduser('~/Downloads'),
                'AUDIO_STORAGE_DIRECTORY': os.path.expanduser('~/Downloads'),
                'TIMEZONE': 'Asia/Kolkata'}
    memory_file_path = os.path.join(
        os.environ['ULTRON_PROJECT_DIR'], 'memory.json')
    if not os.path.exists(memory_file_path):
        with open(memory_file_path, 'w') as memory_file:
            json.dump(defaults, memory_file)
    if os.environ.get('PYTHONPATH', None) is None:
        os.environ['PYTHONPATH'] = os.environ['ULTRON_PROJECT_DIR']
    else:
        path_list = str(os.environ['PYTHONPATH']).split(':')
        if not os.environ['ULTRON_PROJECT_DIR'] in path_list:
            os.environ['PYTHONPATH'] += os.pathsep + \
                                        os.environ['ULTRON_PROJECT_DIR']
