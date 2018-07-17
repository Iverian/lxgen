import subprocess
import json

from typing import Dict, Any
from .basic_data_provider import BasicDataProvider


class DefaultProvider(BasicDataProvider):
    def __init__(self, executable: str):
        BasicDataProvider.__init__(self, executable)

    @staticmethod
    def get_short_description():
        return 'Provides data by calling external executable: exec <directory> <data>'

    def __call__(self, directory: str, data: Dict[str, Any]) -> Dict[str, Any]:
        return json.loads(
            subprocess.run([self.get_executable(), directory, json.dumps(data)], stdout=subprocess.PIPE, check=True,
                           shell=True).stdout)
