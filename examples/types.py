from typing import NewType
from dataclasses import dataclass

TaskID = NewType("TaskID", int)


@dataclass(frozen=True)
class Task:
    smth: str
    b: int
