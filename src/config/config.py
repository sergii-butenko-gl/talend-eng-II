import json
import os
from typing import Any

from src.config.base_provider import BaseProviderClass


class DictConfigProvider(BaseProviderClass):

    def __init__(self, input_values: dict) -> None:
        super().__init__()
        self.values = input_values

    def get(self, item_name: str) -> Any:
        return self.values[item_name]


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
        value = JSONConfigProvider._read_config(
            "/framework/envs_configs/dev.json"
        )
        # return value[item_name]
        return value.get(item_name)


class Config:
    """
    Holds all the settings of your framework
    """

    def __init__(self, config_providers) -> None:
        self.config_providers = config_providers

        self.conf_dict = {}
        self._register("BASE_URL_API")
        self._register("BASE_URL_UI")
        self._register("SQL_CONNECTION_STRING")
        self._register("NOSQL_CONNECTION_STRING")
        self._register("SHARED_USER_NAME")
        self._register("SHARED_USER_PASSWORD")
        self._register("BROWSER")

    def get(self, item_name: str) -> Any:
        return self.conf_dict[item_name]

    # python way
    def __getattr__(self, item):
        if item not in self.conf_dict:
            raise AttributeError("Please register var before usage")

        return self.conf_dict[item]

    def _register(self, item_name: str) -> None:
        for provider in self.config_providers:
            value = provider.get(item_name)
            if value is not None:
                self.conf_dict[item_name] = value
                return

        raise ValueError(f"{item_name} name is missing in config providers")


dict_confprovider = DictConfigProvider({'BROWSER': 'chrome'})
config = Config([OSConfigProvider, JSONConfigProvider, dict_confprovider])
