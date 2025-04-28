from importlib.metadata import version
ma_version = version("marshmallow")
ver_parts = ma_version.split(".")

if ver_parts[0] > "3":
    from .decorators_ma_4 import  accepts, responds  # noqa
else:
    from .decorators_ma_3 import accepts, responds  # noqa
