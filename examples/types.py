from dataclasses import dataclass
from typing import NewType

TaskID = NewType("TaskID", int)


@dataclass(frozen=True)
class Task:
    smth: str
    b: int
