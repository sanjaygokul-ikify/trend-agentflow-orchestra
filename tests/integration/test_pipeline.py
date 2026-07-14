import unittest
from cli.main import main
from packages.core.tasks import Task
from packages.core.nodes import Node
import logging
import sys

logger = logging.getLogger(__name__)

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        sys.argv = ['main.py', '--num-nodes', '1', '--tasks', '1', '--nodes', '1']
        main()
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()