import logging
from typing import List, Dict
from .types import Task, Node
from .exceptions import EngineException


class Engine:
    def __init__(self, num_nodes: int):
        self.num_nodes = num_nodes
        self.tasks: List[Task] = []
        self.nodes: List[Node] = []
        self.logger = logging.getLogger(__name__)

    def add_task(self, task: Task):
        self.tasks.append(task)
        self.logger.info(f'Task {task.id} added')

    def add_node(self, node: Node):
        self.nodes.append(node)
        self.logger.info(f'Node {node.id} added')

    def assign_tasks(self):
        for task in self.tasks:
            node = self.find_eligible_node(task)
            if node:
                node.assign_task(task)
                self.logger.info(f'Task {task.id} assigned to node {node.id}')
            else:
                self.logger.warning(f'No eligible node found for task {task.id}')

    def find_eligible_node(self, task: Task) -> Node:
        for node in self.nodes:
            if node.can_handle_task(task):
                return node
        return None

    def execute_tasks(self):
        for node in self.nodes:
            node.execute_tasks()
        self.logger.info('Tasks execution completed')

    def monitor_tasks(self):
        for node in self.nodes:
            node.monitor_tasks()
        self.logger.info('Tasks monitoring completed')

    def store_results(self):
        for node in self.nodes:
            node.store_results()
        self.logger.info('Results stored')

    def log_results(self):
        for node in self.nodes:
            node.log_results()
        self.logger.info('Results logged')

    def anomaly_detection(self):
        for node in self.nodes:
            node.anomaly_detection()
        self.logger.info('Anomaly detection completed')

    def metrics_aggregation(self):
        for node in self.nodes:
            node.metrics_aggregation()
        self.logger.info('Metrics aggregated')


class Node:
    def __init__(self, id: int):
        self.id = id
        self.tasks: List[Task] = []
        self.logger = logging.getLogger(__name__)

    def assign_task(self, task: Task):
        self.tasks.append(task)
        self.logger.info(f'Task {task.id} assigned to node {self.id}')

    def can_handle_task(self, task: Task) -> bool:
        # logic to determine if node can handle task
        return True

    def execute_tasks(self):
        for task in self.tasks:
            # logic to execute task
            self.logger.info(f'Task {task.id} executed on node {self.id}')

    def monitor_tasks(self):
        for task in self.tasks:
            # logic to monitor task
            self.logger.info(f'Task {task.id} monitored on node {self.id}')

    def store_results(self):
        for task in self.tasks:
            # logic to store results
            self.logger.info(f'Results of task {task.id} stored on node {self.id}')

    def log_results(self):
        for task in self.tasks:
            # logic to log results
            self.logger.info(f'Results of task {task.id} logged on node {self.id}')

    def anomaly_detection(self):
        for task in self.tasks:
            # logic to detect anomalies
            self.logger.info(f'Anomaly detection for task {task.id} completed on node {self.id}')

    def metrics_aggregation(self):
        for task in self.tasks:
            # logic to aggregate metrics
            self.logger.info(f'Metrics for task {task.id} aggregated on node {self.id}')