from . import app_types
from logus import LogOption
from typing import Dict, Any


def TaskID(value: app_types.TaskID) -> LogOption:
    def wrapper(params: Dict[str, Any]) -> None:
        params["task_id"] = str(value)

    return wrapper


def Task(value: app_types.Task) -> LogOption:
    def wrapper(params: Dict[str, Any]) -> None:
        params.update(value.__dict__)

    return wrapper
