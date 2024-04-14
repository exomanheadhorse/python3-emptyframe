import uuid


def gen_task_id():
    return uuid.uuid4()


if __name__ == '__main__':
    gen_task_id()