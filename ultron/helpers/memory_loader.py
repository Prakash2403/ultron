import json
import os


class Default:
    memory_dict = None

    @staticmethod
    def load_defaults(force_load=False):
        if Default.memory_dict is None or force_load:
            memory_file = os.path.join(os.environ.get('ULTRON_PROJECT_DIR'), 'memory.json')
            with open(memory_file,'r') as mem_file:
                Default.memory_dict = json.load(mem_file)
        return Default.memory_dict
