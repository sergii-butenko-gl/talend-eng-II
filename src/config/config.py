import os
from typing import Any
import json


class BaseProviderClass:

    @staticmethod
    def get(item_name: str) -> Any:
        raise NotImplementedError("get method is not implemented")


class OSConfigProvider(BaseProviderClass):

    @staticmethod
    def get(item_name: str) -> Any:
        value = os.getenv(item_name)
        return value


class JSONConfigProvider(BaseProviderClass):

    @staticmethod
    def _read_config(config_path):
        with open(config_path) as json_file:
            return json.load(json_file)

    @staticmethod
    def get(item_name: str) -> Any:
        value = JSONConfigProvider._read_config("/home/sbutenko/repos/LnD/talend-eng-II/envs_configs/dev.json")
        # return value[item_name]
        return value.get(item_name)


class Config:
    """
    Holds all the settings of your framework
    """

    def __init__(self, config_providers) -> None:
        self.config_providers = config_providers

        self.conf_dict = {}
        self._register("BASE_URL")
        self._register("SQL_CONNECTION_STRING")
        self._register("NOSQL_CONNECTION_STRING")

    def get(self, item_name: str) -> Any:
        return self.conf_dict[item_name]

    def _register(self, item_name: str) -> None:
        for provider in self.config_providers:
            value = provider.get(item_name)
            if value is not None:
                self.conf_dict[item_name] = value
                return

        raise ValueError(f"{item_name} name is missing in config providers")


config = Config([OSConfigProvider, JSONConfigProvider])
print(config.get('NOSQL_CONNECTION_STRING'))
# print(config.NOSQL_CONNECTION_STRING)
