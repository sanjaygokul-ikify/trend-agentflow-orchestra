from typing import Dict
from dataclasses import dataclass

@dataclass
class Task:
    id: int
    data: Dict[str, str]

@dataclass
class Node:
    id: int
    tasks: list[Task]