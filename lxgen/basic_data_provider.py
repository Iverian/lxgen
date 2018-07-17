from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from class_registry import EntryPointClassRegistry


PROVIDERS = EntryPointClassRegistry('lxgen_data_provider')


class BasicDataProvider(ABC):
    def __init__(self, executable: str):
        """
        :param executable:
        """
        self.__executable = executable

    def get_executable(self):
        return self.__executable

    @staticmethod
    @abstractmethod
    def get_short_description() -> str:
        return 'Abstract class for data provider classes'

    @abstractmethod
    def __call__(self, directory: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        :param directory:
        :param data:
        :return:
        """
        return {}


def list_providers():
    return list(PROVIDERS.keys())


def get_provider(key: Optional[str], executable: str, *args):
    return PROVIDERS.get(key, executable, *args)
