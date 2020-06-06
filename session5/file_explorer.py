import os


class MyError(Exception):
    pass


def create_dir(user_dir):
    if os.path.isdir(user_dir):
        return 'exists'
    else:
        try:
            os.mkdir(user_dir)
            return 'created'
        except MyError:
            return 'failed'
