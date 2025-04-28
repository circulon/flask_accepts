from importlib.metadata import version

ma_version = version("marshmallow")
ver_parts = ma_version.split(".")

if ver_parts[0] > "3":
    from . import utils_ma_4 as utils
    from .utils_ma_4 import for_swagger
else:
    from . import utils_ma_3 as utils
    from .utils_ma_3 import for_swagger
