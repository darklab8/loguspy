from . import types
from typelog import LogType
from typing import Dict, Any


def TaskID(value: types.TaskID) -> LogType:
    def wrapper(params: Dict[str, Any]) -> None:
        params["task_id"] = str(value)

    return wrapper


def Task(value: types.Task) -> LogType:
    def wrapper(params: Dict[str, Any]) -> None:
        params.update(value.__dict__)

    return wrapper
