from asyncio import get_event_loop, ensure_future
from functools import wraps


class Dispatch(object):

    def __init__(self, func):
        self.func = func
        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        LOOP = get_event_loop()
        obj = ensure_future(self.func(*args, **kwargs), loop=LOOP)
        if not LOOP.is_running():
            LOOP.run_forever()
        else:
            return obj
