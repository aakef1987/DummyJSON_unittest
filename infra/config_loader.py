import json
import os

class Config:
    _data = None

    @classmethod
    def load(cls):
        if cls._data is None:
            project_root = os.path.dirname(os.path.dirname(__file__))
            path = os.path.join(project_root, "config.json")

            with open(path, "r") as f:
                cls._data = json.load(f)

        return cls._data
