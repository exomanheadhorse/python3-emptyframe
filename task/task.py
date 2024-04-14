import subprocess
from typing import Dict
import src.common as common


class Task(object):
    def __init__(self, **args) -> None:
        self.task_id: str = args.get('task_id', '')
        self.target_viscosity: float = args.get('target_viscosity', 0)
        self.temperature: int = args.get('temperature', 0)
        self.coals_content = args.get('coals_content', {})
        self.task_name: str = args.get('task_name', '')
        self.task_status: int = args.get('task_status', 0)
        self.create_time: str = args.get('create_time', '')
        self.end_time: str = args.get('end_time', '')
        self.update_time: str = args.get('update_time', '')
        self.data: str = args.get('data', '{}')

    def update_status(self, status: int) -> None:
        self.task_status = status

    def update_status_in_db(self, status: int) -> None:
        pass

    def start(self) -> None:
        subprocess.run(["python3", "optimization.py", ], stdout=)
        pass


class TaskMgr:
    def __init__(self):
        self.tasks: Dict[str, Task] = {}
        self.db_ins = common.get_db_hander("task_info")

    def start(self) -> None:
        pass

    def create_task(self):
        pass

    def query_task(self, task_id: str) -> Task:
        pass
