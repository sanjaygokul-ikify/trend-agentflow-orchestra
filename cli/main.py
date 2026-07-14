import argparse
import sys
from services.orchestrator import Orchestrator
from packages.core.tasks import Task
from packages.core.nodes import Node
import logging

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description='Orchestrator CLI')
    parser.add_argument('--num-nodes', type=int, required=True)
    parser.add_argument('--tasks', type=str, nargs='+')
    parser.add_argument('--nodes', type=str, nargs='+')
    args = parser.parse_args()
    orchestrator = Orchestrator(args.num_nodes)
    for task_id in args.tasks:
        task = Task(int(task_id), {})
        orchestrator.add_task(task)
    for node_id in args.nodes:
        node = Node(int(node_id))
        orchestrator.add_node(node)
    orchestrator.start()

if __name__ == '__main__':
    sys.exit(main())