import importlib

import config

module, name = config.DB_ADAPTER.rsplit('.', 1)
mod = importlib.import_module(module, name)

def get_impl():
    # XXX FIXME keep all config reading here?
    return getattr(mod, name)()
