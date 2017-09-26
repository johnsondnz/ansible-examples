from ansible import errors
from jinja2.filters import environmentfilter

class FilterModule(object):
    def filters(self):
        return {
            'iterable': self.iterable
        }
    def iterable(*args):
      if isinstance(args[1], list):
        return True
      else:
        return False