import unittest
import time
from packages.core.engine import Engine
from packages.core.tasks import Task
from packages.core.nodes import Node

class TestRuntime(unittest.TestCase):
    def test_runtime(self):
        engine = Engine(1)
        task = Task(1, {})
        node = Node(1)
        engine.add_task(task)
        engine.add_node(node)
        start_time = time.time()
        engine.assign_tasks()
        engine.execute_tasks()
        engine.monitor_tasks()
        engine.store_results()
        engine.log_results()
        engine.anomaly_detection()
        engine.metrics_aggregation()
        end_time = time.time()
        self.assertLess(end_time - start_time, 10)

if __name__ == '__main__':
    unittest.main()