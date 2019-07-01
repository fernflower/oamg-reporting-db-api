import importlib

import config

module, name = config.ADAPTER.rsplit('.', 1)
mod = importlib.import_module(module, name)

def get_impl():
    # XXX FIXME keep all config reading here?
    return getattr(mod, name)()
