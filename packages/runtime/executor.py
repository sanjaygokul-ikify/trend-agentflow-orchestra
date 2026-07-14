from typing import List
from .types import Task
from ..core.engine import Engine, Node
from ..core.exceptions import EngineException


class Executor:
    def __init__(self):
        self.engine = Engine(10)
        self.tasks: List[Task] = []

    def execute(self):
        try:
            self.engine.assign_tasks()
            self.engine.execute_tasks()
            self.engine.monitor_tasks()
            self.engine.store_results()
            self.engine.log_results()
            self.engine.anomaly_detection()
            self.engine.metrics_aggregation()
        except EngineException as e:
            # handle engine exception
            print(f'Engine exception: {e}')

    def add_task(self, task: Task):
        self.tasks.append(task)
        self.engine.add_task(task)

    def add_node(self, node: Node):
        self.engine.add_node(node)