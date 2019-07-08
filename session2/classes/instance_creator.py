from importlib import import_module


def create_instance(name, *args, **kwargs):
    module_name, class_name = name.rsplit('.', 1)
    module = import_module(module_name)
    class_ = getattr(module, class_name)
    instance = class_(*args, **kwargs)
    return instance
