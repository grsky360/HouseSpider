from . import default_config

configs = {}
configs.update(default_config.configs)

try:
    from . import apply_config
    configs.update(apply_config.configs)
except ImportError:
    pass
