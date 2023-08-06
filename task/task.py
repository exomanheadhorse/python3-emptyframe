class Task(object):
    def __init__(self, **args) -> None:
        self.task_id: int = args.get('task_id', 0)
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

    