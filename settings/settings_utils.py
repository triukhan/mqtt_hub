def bool_param(func):
    def wrapper(instance, value):
        value = (value == 'True') if isinstance(value, str) else value
        return func(instance, value)

    return wrapper
