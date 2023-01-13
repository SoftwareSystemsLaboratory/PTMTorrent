# pylint: skip-file
from functools import wraps
from traceback import print_exc


def handle_errors(fn):
    """
    Exceptions aren't really raised within threads so this function makes sure some output is given
    """

    @wraps(fn)
    def res(*args, **kwargs):
        try:
            return fn(*args, **kwargs)

        except Exception as exc:
            print(f"[caught] {exc}")
            print_exc()

    return res
