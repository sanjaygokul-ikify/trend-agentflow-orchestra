import unittest
from packages.core.engine import Engine
from packages.core.tasks import Task
from packages.core.nodes import Node

class TestEngine(unittest.TestCase):
    def test_add_task(self):
        engine = Engine(1)
        task = Task(1, {})
        engine.add_task(task)
        self.assertEqual(len(engine.tasks), 1)

    def test_add_node(self):
        engine = Engine(1)
        node = Node(1)
        engine.add_node(node)
        self.assertEqual(len(engine.nodes), 1)

if __name__ == '__main__':
    unittest.main()