_registry = {}

def register(name):
    def decorator(cls):
        _registry[name.lower()] = cls
        return cls
    return decorator

def get(name):
    return _registry.get(name.lower())
