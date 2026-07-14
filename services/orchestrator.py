from packages.core.engine import Engine
from packages.core.nodes import Node
from packages.core.tasks import Task
import logging

logger = logging.getLogger(__name__)

class Orchestrator:
    def __init__(self, num_nodes: int):
        self.engine = Engine(num_nodes)

    def add_task(self, task: Task):
        self.engine.add_task(task)
        logger.info(f'Task {task.id} added')

    def add_node(self, node: Node):
        self.engine.add_node(node)
        logger.info(f'Node {node.id} added')

    def start(self):
        self.engine.assign_tasks()
        self.engine.execute_tasks()
        self.engine.monitor_tasks()
        self.engine.store_results()
        self.engine.log_results()
        self.engine.anomaly_detection()
        self.engine.metrics_aggregation()