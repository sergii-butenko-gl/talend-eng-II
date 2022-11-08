from typing import Any


class BaseProviderClass:
    @staticmethod
    def get(item_name: str) -> Any:
        raise NotImplementedError("get method is not implemented")
