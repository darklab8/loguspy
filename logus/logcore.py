import json
import logging
from typing import Dict

from . import settings
from .logtypes import LogOption, LogParams

log_levels_str_to_int: Dict[str, int] = {"": logging.WARN}
log_levels_str_to_int.update(logging._nameToLevel)

default_log_level = log_levels_str_to_int[settings.LOG_LEVEL]


class StructuredMessage:
    def __init__(
        self,
        message: str,
        *args: LogOption,
    ) -> None:
        self._message = message
        self._kwargs: LogParams = LogParams({})
        for add_option in args:
            add_option(self._kwargs)

    def __str__(self) -> str:
        if settings.LOG_JSON:
            return json.dumps(self.to_dict())

        if len(self._kwargs.keys()) == 0:
            return self._message

        return "%s >>> %s" % (
            self._message,
            " ".join([f"{key}={value}" for key, value in self._kwargs.items()]),
        )

    def to_dict(self) -> Dict:
        return {"message": self._message, **self._kwargs}


sm = StructuredMessage


class Logus:
    def __init__(self, name: str):
        """
        pass __file__ into file
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(default_log_level)

    def debug(self, message: str, *args: LogOption) -> None:
        self.logger.debug(StructuredMessage(message, *args))

    def info(self, message: str, *args: LogOption) -> None:
        self.logger.info(StructuredMessage(message, *args))

    def warn(self, message: str, *args: LogOption) -> None:
        self.logger.warning(StructuredMessage(message, *args))

    def error(self, message: str, *args: LogOption) -> None:
        self.logger.error(StructuredMessage(message, *args))

    def fatal(self, message: str, *args: LogOption) -> None:
        self.logger.fatal(StructuredMessage(message, *args))


def get_logger(file: str) -> Logus:
    return Logus(file)
